# AGENT SCORECARD

Tài liệu này cung cấp template Scorecard chuẩn cho từng AI Worker trong hệ thống. Dữ liệu trong Scorecard phải lấy từ Task Evidence thực tế, không hard-code số liệu giả.

## 1. Scorecard Template
```yaml
agent_identity: ""
role: ""
skill_level: "" # L0-L5
authorization_level: ""
risk_level: "" # R0-R5

dimensions:
  quality:
    score: 0
    trend: stable # improving/declining/stable
  speed:
    score: 0
    trend: stable
  adaptability:
    score: 0
    trend: stable
  autonomy:
    score: 0
    trend: stable

overall_score: 0

metrics:
  task_success_rate: 0%
  human_intervention_rate: 0%
  incident_rate: 0%
  failure_rate: 0%
  recovery_rate: 0%
  escalation_rate: 0%

policy_violation: 0
data_safety: "Secure"
```

## 2. Agent-Specific KPIs

### AGENT_BOT_SUPERVISOR
- **Ưu tiên:** Bot availability, Failure detection, Recovery success, Mean Time To Recovery (MTTR), False positive/negative, Process stability, Autonomous recovery.

### AGENT_V3_MAINTAINER
- **Ưu tiên:** Data integrity, Zero destructive action, Legacy stability, Database safety, Compatibility, Recovery success, Regression rate.

### AGENT_V4_ARCHITECT
- **Ưu tiên:** UI correctness, Build success, Regression rate, UX consistency, Performance, CSS/theme integrity, React tree integrity.
