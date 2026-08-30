import os
import time

class EventWatcher:
    def __init__(self):
        self.log_dir = os.path.join(os.path.dirname(__file__), "mock_logs")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def scan_for_events(self) -> list:
        """
        Scans the mock_logs directory for any .log files.
        Parses them to extract actionable events.
        """
        events = []
        for filename in os.listdir(self.log_dir):
            if filename.endswith(".log"):
                filepath = os.path.join(self.log_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        # Very simple parser: Action: XXX, Agent: YYY
                        action = "UNKNOWN"
                        agent = "UNKNOWN"
                        for line in content.split('\n'):
                            if line.startswith("Action:"):
                                action = line.split(":")[1].strip()
                            if line.startswith("Agent:"):
                                agent = line.split(":")[1].strip()
                        
                        if action != "UNKNOWN" and agent != "UNKNOWN":
                            events.append({
                                "agent_id": agent,
                                "action": action,
                                "source_file": filename
                            })
                    # Remove the file after processing to avoid duplicate events
                    os.remove(filepath)
                except Exception as e:
                    print(f"[EventWatcher] Failed to process {filename}: {e}")
        return events
