# SKILL EVALUATION FRAMEWORK

## 1. Purpose
Tài liệu này định nghĩa chuẩn đánh giá năng lực AI Worker trong hệ sinh thái SKILL_BAT_AI. Việc đánh giá đảm bảo AI hoạt động hiệu quả, an toàn và tuân thủ đúng giới hạn quyền hạn được phân công bởi Hệ thống Quản trị.

## 2. Evaluation Philosophy
- **Quality trước Speed**: Không đánh đổi an toàn lấy tốc độ.
- **Evidence-based**: Không đánh giá AI chỉ bằng lời nói, mọi đánh giá quan trọng phải dựa trên Evidence.
- **Autonomy gắn với Risk**: Mức độ tự chủ phải tương xứng với rủi ro của tác vụ.
- **No Self-Promotion**: Agent không được tự nâng cấp quyền.
- **Human Authority**: Human Owner (Quanpt1) có quyền override bất kỳ quyết định nào của AI.

## 3. Four Core Dimensions

### QUALITY (Chất lượng)
- Accuracy, Completeness, Correctness
- Reliability, Safety, Compliance
- Data integrity, Regression prevention

### SPEED / EFFICIENCY (Tốc độ & Hiệu suất)
- Task completion time, Response time, Recovery Time
- Number of unnecessary actions
- Resource efficiency, Automation efficiency

### ADAPTABILITY (Độ thích nghi)
- Xử lý exception, Xử lý lỗi chưa có trong SOP
- Khả năng tìm workaround, Root-cause analysis
- Khả năng thay đổi kế hoạch, phục hồi, học từ failure

### AUTONOMY (Tính tự chủ)
- Có cần human intervention không?
- Có biết giới hạn quyền hạn không?
- Có tự kiểm tra (Self-check) trước khi kết thúc không?
- Có biết khi nào phải escalation (leo thang) không?
- Có thực hiện đúng approval workflow không?

## 4. Thang điểm (Scoring)
- **0** = Failure / Unsafe
- **1** = Very Low
- **2** = Basic
- **3** = Standard
- **4** = Advanced
- **5** = Expert

**Trọng số mặc định (Default Weights):**
- QUALITY: 40%
- SPEED: 20%
- ADAPTABILITY: 20%
- AUTONOMY: 20%

> **Quy tắc cốt lõi:** Một Agent không thể đạt mức Expert (5) nếu Quality hoặc Safety dưới ngưỡng tối thiểu, dù Speed có rất cao.

## 5. Skill Level
- **L0** — UNAUTHORIZED
- **L1** — ASSISTED
- **L2** — STANDARD OPERATOR
- **L3** — INDEPENDENT OPERATOR
- **L4** — ADVANCED SPECIALIST
- **L5** — SYSTEM IMPROVER

**Quy định:** 
- Agent KHÔNG được tự nâng Skill Level.
- Promotion phải được quyết định bởi Quanpt1 / Authorized Human Governance.

## 6. Evaluation Gate (Luồng Đánh Giá)
`TASK CREATED` → `RISK CLASSIFICATION` → `AUTHORIZATION CHECK` → `EXECUTION` → `SELF CHECK` → `EVIDENCE COLLECTION` → `EVALUATION` → `SCORE` → `PASS / FAIL` → `LEARNING`

Không được coi task là thành công chỉ vì Agent trả lời "Done".
