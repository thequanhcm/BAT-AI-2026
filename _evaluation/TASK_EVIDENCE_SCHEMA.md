# TASK EVIDENCE SCHEMA

Chuẩn hóa bằng chứng (Evidence) cho mọi task. Không cho phép đánh giá Agent chỉ dựa trên self-report.
Mọi task phải lưu lại Evidence tương thích định dạng YAML/JSON để hỗ trợ tự động hóa, Database, API, và Learning Loop.

## 1. Schema YAML Chuẩn
```yaml
task_id: TASK-YYYYMMDD-XXXX

agent:
  id: "" # AGENT_BOT_SUPERVISOR / AGENT_V3_MAINTAINER / AGENT_V4_ARCHITECT
  skill_level: "" # L0-L5

authority:
  owner: Quanpt1
  authorization_status: "" # authorized / unauthorized / pending

risk:
  level: "" # R0-R5
  classification_reason: ""

request:
  description: ""

execution:
  started_at: ""
  completed_at: ""
  planned_actions: []
  actual_actions: []

system:
  target: ""
  environment: ""

state:
  before: {}
  after: {}

validation:
  checks: []
  passed: false

result:
  status: "" # success / failed
  message: ""

errors: []

recovery:
  required: false
  actions: []

human_intervention:
  required: false
  approver: ""
  reason: ""

approval:
  required: false
  status: "" # not_required / approved / rejected
  approval_id: ""

rollback:
  available: false
  procedure: ""

performance:
  expected_duration: 0
  actual_duration: 0

evaluation:
  quality: 0
  speed: 0
  adaptability: 0
  autonomy: 0
  overall: 0

learning:
  lesson_learned: ""
  improvement_required: false
  suggested_update: ""
```

## 2. Failure Handling
Nếu task thất bại (status: failed), Evidence phải chứa:
- `failure_type` (Recoverable, Known, Unknown, Critical, Policy Violation)
- `failure_stage`
- `root_cause`
- `impact`
- `recovery_action` & `recovery_success`
- `human_intervention`
- `lesson_learned`

## 3. Anti-Gaming Rule
- `Agent SELF-CHECK` ≠ `Final Evaluation`
- Agent được tự kiểm tra nhưng Final Score = `Agent self-assessment` + `Objective telemetry` + `Validation result` + `Human review when required`.
