import os
from risk_engine import RiskEngine

class AuthorizationEngine:
    def __init__(self):
        self.risk_engine = RiskEngine()
        
    def check_authorization(self, agent_id: str, action: str, env_secret: str = None) -> dict:
        risk_level = self.risk_engine.assess_risk(action)
        
        # Deny R5 unconditionally
        if risk_level == "R5":
            return {"status": "DENY", "reason": "Action is FORBIDDEN (R5)"}
            
        # Deny if Unknown Agent (Simplified for Phase 1)
        valid_agents = ["AGENT_BOT_SUPERVISOR", "AGENT_V3_MAINTAINER", "AGENT_V4_ARCHITECT"]
        if agent_id not in valid_agents:
            return {"status": "DENY", "reason": "Unknown Agent"}
            
        # R0, R1 are fully autonomous
        if risk_level in ["R0", "R1"]:
            return {"status": "ALLOW", "reason": f"Autonomous execution allowed for {risk_level}"}
            
        # R2 is allowed (assuming validation is handled in task engine)
        if risk_level == "R2":
            return {"status": "ALLOW", "reason": "Autonomous execution allowed for R2 with validation"}
            
        # R3, R4 require Human Approval
        if risk_level in ["R3", "R4"]:
            return {"status": "APPROVAL_REQUIRED", "reason": f"Human Approval required for {risk_level}"}

        return {"status": "DENY", "reason": "Unknown risk level"}
        
    def approve_action(self, provided_secret: str) -> bool:
        # Simulate checking the Quanpt1 secret from env
        actual_secret = os.environ.get("QUANPT1_APPROVAL_SECRET", "NOT_SET")
        if actual_secret == "NOT_SET":
            return False # Fail closed
        return provided_secret == actual_secret
