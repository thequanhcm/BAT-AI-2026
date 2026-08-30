from validation_engine import ValidationEngine
from recovery_engine import RecoveryEngine

class ExecutionEngine:
    def __init__(self):
        self.validation_engine = ValidationEngine()
        self.recovery_engine = RecoveryEngine()

    def execute(self, task_id: str, action: str, mock_validation_fail: bool = False) -> dict:
        print(f"[ExecutionEngine] Executing {action} for task {task_id}")
        
        # Simulate execution success
        print(f"[ExecutionEngine] Execution command sent.")
        
        # Validate
        retry_count = 0
        while True:
            # Check if it passes validation
            # For testing, we mock fail only on the first few tries if requested
            current_mock_fail = mock_validation_fail and (retry_count < 2) 
            
            is_valid = self.validation_engine.validate_action(action, mock_fail=current_mock_fail)
            
            if is_valid:
                return {"status": "COMPLETED", "message": "Execution and Validation successful"}
            else:
                # Attempt recovery
                recovery_result = self.recovery_engine.attempt_recovery(action, retry_count)
                if recovery_result["status"] == "RETRY":
                    retry_count = recovery_result["retry_count"]
                    print(f"[ExecutionEngine] Retrying action {action}...")
                else:
                    return {"status": "FAILED", "reason": recovery_result["reason"]}
