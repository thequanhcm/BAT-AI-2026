import os
import json

class LearningEngine:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), "risk_matrix.json")
        
    def learn(self, action: str, assigned_risk: str):
        print(f"[LearningEngine] Learning new rule: {action} -> {assigned_risk}")
        
        # Load existing
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                try:
                    matrix = json.load(f)
                except:
                    matrix = {}
        else:
            matrix = {}
            
        # Update
        matrix[action.upper()] = assigned_risk.upper()
        
        # Save
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(matrix, f, indent=4)
        print(f"[LearningEngine] Rule successfully persisted to knowledge base.")
