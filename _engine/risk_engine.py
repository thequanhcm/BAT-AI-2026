import os
import json

class RiskEngine:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), "risk_matrix.json")
        self._init_defaults()

    def _init_defaults(self):
        default_matrix = {
            "READ_LOG": "R0",
            "HEALTH_CHECK": "R0",
            "ANALYZE_METRICS": "R0",
            "RESTART_PROCESS": "R1",
            "CLEAR_CACHE": "R1",
            "UPDATE_CONFIG_SAFE": "R2",
            "DEPLOY_NEW_CODE": "R3",
            "CHANGE_IP": "R4",
            "DELETE_DB_V4": "R4",
            "MODIFY_SECURITY_POLICY": "R4",
            "DELETE_V3_HISTORY": "R5",
            "SELF_PROMOTION": "R5",
            "BYPASS_APPROVAL": "R5"
        }
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(default_matrix, f, indent=4)

    def load_matrix(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def assess_risk(self, action: str) -> str:
        matrix = self.load_matrix()
        # Default fallback is R4 (High Risk / Human Approval Required) if action is unknown
        return matrix.get(action.upper(), "R4")
