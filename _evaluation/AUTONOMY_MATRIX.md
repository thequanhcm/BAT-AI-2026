# AUTONOMY MATRIX

Xác định chính xác Agent được phép tự làm gì, phải xin phép việc gì và tuyệt đối không được làm gì dựa trên cấp độ rủi ro (Risk Levels).

## 1. Risk Levels (Cấp độ rủi ro)

- **R0 — READ ONLY / SAFE**: Tự động (Đọc log, health check, đọc metrics, kiểm tra process, kiểm tra API, phân tích dữ liệu).
- **R1 — LOW RISK**: Tự động (Restart process an toàn, retry, temporary recovery, clear temporary cache, xử lý lỗi chuẩn trong SOP).
- **R2 — MEDIUM RISK**: Được phép nếu có validation, có rollback, không ảnh hưởng dữ liệu quan trọng, đúng quyền Agent.
- **R3 — HIGH RISK**: Phải thực hiện quy trình: Prepare → Explain → Risk Assessment → Request Approval → Execute → Verify.
- **R4 — CRITICAL / HUMAN APPROVAL**: Bắt buộc Human Approval (Quanpt1).
- **R5 — FORBIDDEN**: Không Agent nào được thực hiện.

## 2. Critical Restrictions (Giới hạn tuyệt đối)
- DELETE V3 HISTORICAL DATA → **R5 FORBIDDEN**
- CHANGE CRITICAL IP → **R4 HUMAN APPROVAL**
- DATABASE DESTRUCTIVE OPERATION → **R4 HUMAN APPROVAL**
- ARCHITECTURE DESTRUCTION → **R4 HUMAN APPROVAL**
- PRODUCTION SCHEMA CHANGE → **R4 HUMAN APPROVAL**
- MASS DATA DELETE → **R5 hoặc R4 tùy policy, mặc định R5**
- CHANGE CORE SECURITY POLICY → **R4 HUMAN APPROVAL**
- SELF-PROMOTION → **R5 FORBIDDEN**

*Lưu ý: Không được để Agent tự cấp quyền cho chính nó.*

## 3. Human Approval Workflow
`Agent detects task` → `Classify Risk` → `Check Authority`
- **If autonomous:** `Execute` → `Verify`
- **If approval required:** `Create Approval Request` → `Quanpt1 reviews` → `APPROVE / REJECT`
  - *If APPROVE:* `Execute` → `Verify` → `Evidence`

### Approval Request Requirements:
Task ID, Agent, Requested action, Reason, Risk, Affected systems, Expected impact, Rollback plan, Validation plan, Evidence, Timestamp, Approver, Approval status.

## 4. Emergency Override
Quy trình ghi đè khẩn cấp từ Human Owner (Quanpt1):
`EMERGENCY STOP` → `Disable Agent` → `Stop autonomous actions` → `Preserve evidence` → `Freeze changes` → `Human investigation`
*(Agent không được vô hiệu hóa Human Override).*

## 5. Escalation Policy (Chính sách Leo thang)
Nguyên tắc: **Khi không chắc chắn về quyền hạn hoặc an toàn, STOP + ESCALATE.**
Escalate khi:
- Vượt quyền.
- Risk Level vượt Autonomy Level.
- SOP không còn phù hợp.
- Có nguy cơ mất dữ liệu / phá production.
- Không xác định được root cause.
- Validation / Rollback thất bại.
- Phát hiện policy violation hoặc task ngoài phạm vi.
*Không được tự thử thêm nếu có thể gây hậu quả không thể đảo ngược.*
