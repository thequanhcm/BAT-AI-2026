import random

class ValidationEngine:
    def __init__(self):
        pass

    def validate_action(self, action: str, mock_fail: bool = False) -> bool:
        """
        Returns True if validation passes, False otherwise.
        mock_fail can be used to simulate a validation failure for testing.
        """
        print(f"[ValidationEngine] Validating outcome of action: {action}")
        if mock_fail:
            print("[ValidationEngine] -> Validation FAILED (Mocked)")
            return False
        
        # In a real scenario, this would check process status, API health, etc.
        print("[ValidationEngine] -> Validation PASSED")
        return True
