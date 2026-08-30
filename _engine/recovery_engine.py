class RecoveryEngine:
    def __init__(self):
        self.max_retries = 2

    def attempt_recovery(self, action: str, current_retry: int) -> dict:
        """
        Returns a dict indicating if recovery is possible and the action to take.
        """
        print(f"[RecoveryEngine] Attempting recovery for {action}. Retry {current_retry}/{self.max_retries}")
        if current_retry < self.max_retries:
            return {"status": "RETRY", "retry_count": current_retry + 1}
        else:
            print("[RecoveryEngine] Max retries reached. Escalating.")
            return {"status": "ESCALATE", "reason": "Max retries reached in recovery"}
