import json

class EvidenceEngine:
    def __init__(self):
        pass

    def build_evidence(self, task_id: str, task_data: dict, exec_result: dict) -> dict:
        """
        Transforms raw task execution data into a standardized Evidence schema.
        """
        evidence = {
            "evidence_id": f"EVID-{task_id}",
            "task_ref": task_id,
            "agent": {
                "agent_id": task_data.get("agent_id"),
                "authorized_role": "SYSTEM_AGENT"
            },
            "risk_assessment": {
                "risk_level": task_data.get("risk_level"),
                "auto_approved": task_data.get("risk_level") in ["R0", "R1", "R2"]
            },
            "execution": {
                "action": task_data.get("action"),
                "final_status": task_data.get("status"),
                "detail": exec_result.get("message") or exec_result.get("reason", "No details")
            }
        }
        return evidence
