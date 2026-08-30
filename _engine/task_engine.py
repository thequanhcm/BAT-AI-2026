import uuid
from datetime import datetime
from authorization_engine import AuthorizationEngine
from risk_engine import RiskEngine
from execution_engine import ExecutionEngine
from evidence_engine import EvidenceEngine
from telemetry_db import TelemetryDB
from escalation_engine import EscalationEngine

class TaskEngine:
    def __init__(self):
        self.auth_engine = AuthorizationEngine()
        self.risk_engine = RiskEngine()
        self.exec_engine = ExecutionEngine()
        self.evidence_engine = EvidenceEngine()
        self.telemetry = TelemetryDB()
        self.escalation_engine = EscalationEngine()
        self.tasks = {}

    def create_task(self, agent_id: str, action: str) -> str:
        task_id = f"TASK-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
        self.tasks[task_id] = {
            "task_id": task_id,
            "agent_id": agent_id,
            "action": action,
            "status": "CREATED",
            "risk_level": "UNKNOWN",
            "ticket_id": None
        }
        return task_id

    def process_task(self, task_id: str, mock_validation_fail: bool = False):
        task = self.tasks.get(task_id)
        if not task:
            return {"error": "Task not found"}

        # If Task is already PENDING_HUMAN, check ticket status
        if task["status"] == "PENDING_HUMAN":
            ticket_status = self.escalation_engine.check_ticket_status(task["ticket_id"])
            if ticket_status == "OPEN":
                return {"task_id": task_id, "status": "PENDING_HUMAN", "message": "Still waiting for Quanpt1"}
            elif ticket_status == "APPROVED":
                task["status"] = "RUNNING"
                task["approver"] = "Quanpt1"
            elif ticket_status == "REJECTED":
                task["status"] = "DENY"
                task["approver"] = "Quanpt1"
                self._record_telemetry(task, {"reason": "Rejected by Quanpt1"})
                return {"task_id": task_id, "status": "DENY", "message": "Rejected by Quanpt1"}

        if task["status"] == "CREATED":
            # State: CLASSIFIED
            task["status"] = "CLASSIFIED"
            risk_level = self.risk_engine.assess_risk(task["action"])
            task["risk_level"] = risk_level
            
            # State: AUTHORIZED
            auth_result = self.auth_engine.check_authorization(task["agent_id"], task["action"])
            
            if auth_result["status"] == "ALLOW":
                task["status"] = "RUNNING"
                
            elif auth_result["status"] == "APPROVAL_REQUIRED":
                # PHASE 4: Create Ticket and wait
                ticket_id = self.escalation_engine.raise_ticket(task_id, auth_result["reason"])
                task["status"] = "PENDING_HUMAN"
                task["ticket_id"] = ticket_id
                self._record_telemetry(task, {"reason": auth_result["reason"]})
                return {"task_id": task_id, "status": "PENDING_HUMAN", "ticket_id": ticket_id}
                
            else: # DENY
                task["status"] = "DENY"
                self._record_telemetry(task, {"reason": auth_result["reason"]})
                return {"task_id": task_id, "status": "DENY", "reason": auth_result["reason"]}

        # If RUNNING
        if task["status"] == "RUNNING":
            exec_result = self.exec_engine.execute(task_id, task["action"], mock_validation_fail=mock_validation_fail)
            
            if exec_result["status"] == "COMPLETED":
                task["status"] = "COMPLETED"
            else:
                # Execution / Recovery failed -> Escalate instead of just FAILED
                ticket_id = self.escalation_engine.raise_ticket(task_id, exec_result.get("reason", "Execution/Recovery failure"))
                task["status"] = "PENDING_HUMAN"
                task["ticket_id"] = ticket_id
                self._record_telemetry(task, {"reason": "Execution/Recovery failure"})
                return {"task_id": task_id, "status": "PENDING_HUMAN", "ticket_id": ticket_id}
                
            # Completed successfully
            self._record_telemetry(task, exec_result)
            return {
                "task_id": task_id,
                "status": task["status"],
                "risk": task["risk_level"],
                "message": exec_result.get("message", "")
            }

    def _record_telemetry(self, task: dict, exec_result: dict):
        task_id = task["task_id"]
        self.telemetry.insert_task(task)
        evidence_doc = self.evidence_engine.build_evidence(task_id, task, exec_result)
        self.telemetry.insert_evidence(task_id, evidence_doc)
