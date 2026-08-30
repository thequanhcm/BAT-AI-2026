import time
import threading
from event_watcher import EventWatcher
from task_engine import TaskEngine

class SupervisorDaemon:
    def __init__(self):
        self.watcher = EventWatcher()
        self.task_engine = TaskEngine()
        self.running = False
        self._thread = None

    def start(self):
        print("[SupervisorDaemon] Starting daemon...")
        self.running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self):
        print("[SupervisorDaemon] Stopping daemon...")
        self.running = False
        if self._thread:
            self._thread.join()

    def _run_loop(self):
        print("[SupervisorDaemon] Daemon is active and watching for events.")
        while self.running:
            events = self.watcher.scan_for_events()
            for event in events:
                print(f"[SupervisorDaemon] Event detected! Agent: {event['agent_id']}, Action: {event['action']}")
                task_id = self.task_engine.create_task(event['agent_id'], event['action'])
                print(f"[SupervisorDaemon] Created Task {task_id}. Processing...")
                result = self.task_engine.process_task(task_id)
                print(f"[SupervisorDaemon] Task {task_id} result: {result['status']}")
            
            # Prevent high CPU usage in mock mode
            time.sleep(1)
