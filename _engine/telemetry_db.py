import sqlite3
import os
import json
from datetime import datetime

class TelemetryDB:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), "db", "ai_workforce.db")
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                agent_id TEXT,
                action TEXT,
                status TEXT,
                risk_level TEXT,
                timestamp TEXT,
                approver TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evidences (
                task_id TEXT PRIMARY KEY,
                evidence_json TEXT,
                timestamp TEXT,
                FOREIGN KEY(task_id) REFERENCES tasks(task_id)
            )
        ''')
        # PHASE 4: TICKETS TABLE
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id TEXT PRIMARY KEY,
                task_id TEXT,
                reason TEXT,
                status TEXT,
                resolution TEXT,
                timestamp TEXT,
                FOREIGN KEY(task_id) REFERENCES tasks(task_id)
            )
        ''')
        conn.commit()
        conn.close()

    def insert_task(self, task_data: dict):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO tasks (task_id, agent_id, action, status, risk_level, timestamp, approver) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                task_data.get("task_id"),
                task_data.get("agent_id"),
                task_data.get("action"),
                task_data.get("status"),
                task_data.get("risk_level"),
                datetime.now().isoformat(),
                task_data.get("approver", "None")
            )
        )
        conn.commit()
        conn.close()
        
    def insert_evidence(self, task_id: str, evidence_data: dict):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO evidences (task_id, evidence_json, timestamp) VALUES (?, ?, ?)",
            (
                task_id,
                json.dumps(evidence_data),
                datetime.now().isoformat()
            )
        )
        conn.commit()
        conn.close()

    def create_ticket(self, ticket_id: str, task_id: str, reason: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (ticket_id, task_id, reason, status, resolution, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            (ticket_id, task_id, reason, "OPEN", "", datetime.now().isoformat())
        )
        conn.commit()
        conn.close()

    def update_ticket(self, ticket_id: str, status: str, resolution: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tickets SET status = ?, resolution = ? WHERE ticket_id = ?",
            (status, resolution, ticket_id)
        )
        conn.commit()
        conn.close()

    def get_ticket(self, ticket_id: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {
                "ticket_id": result[0],
                "task_id": result[1],
                "reason": result[2],
                "status": result[3],
                "resolution": result[4]
            }
        return None

    def get_task(self, task_id: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
        result = cursor.fetchone()
        conn.close()
        return result
        
    def get_evidence(self, task_id: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT evidence_json FROM evidences WHERE task_id = ?", (task_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return json.loads(result[0])
        return None
