import uuid
from telemetry_db import TelemetryDB
from learning_engine import LearningEngine

class EscalationEngine:
    def __init__(self):
        self.telemetry = TelemetryDB()
        self.learning_engine = LearningEngine()

    def raise_ticket(self, task_id: str, reason: str) -> str:
        ticket_id = f"TICKET-{str(uuid.uuid4())[:8].upper()}"
        print(f"[EscalationEngine] Raising Ticket {ticket_id} for Task {task_id}. Reason: {reason}")
        self.telemetry.create_ticket(ticket_id, task_id, reason)
        return ticket_id

    def check_ticket_status(self, ticket_id: str) -> str:
        ticket = self.telemetry.get_ticket(ticket_id)
        if not ticket:
            return "UNKNOWN"
        return ticket["status"]

    def resolve_ticket(self, ticket_id: str, action: str, secret: str = None, learned_action: str = None, learned_risk: str = None) -> bool:
        import os
        # Verify Quanpt1 secret
        actual_secret = os.environ.get("QUANPT1_APPROVAL_SECRET", "NOT_SET")
        if actual_secret == "NOT_SET" or secret != actual_secret:
            print(f"[EscalationEngine] Resolution for {ticket_id} failed due to invalid secret.")
            return False
            
        if action.upper() not in ["APPROVED", "REJECTED"]:
            return False
            
        print(f"[EscalationEngine] Ticket {ticket_id} resolved as {action.upper()} by Quanpt1")
        self.telemetry.update_ticket(ticket_id, action.upper(), f"Resolved by Quanpt1 as {action.upper()}")
        
        # PHASE 6: Self-Learning (Only authorized by Quanpt1)
        if action.upper() == "APPROVED" and learned_action and learned_risk:
            print("[EscalationEngine] Quanpt1 provided knowledge extraction parameters. Triggering LearningEngine...")
            self.learning_engine.learn(learned_action, learned_risk)
            
        return True
