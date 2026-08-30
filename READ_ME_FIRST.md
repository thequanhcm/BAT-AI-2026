# SKILL_BAT_AI - AUTONOMOUS AI WORKFORCE OS
**Version:** 1.0 (Production Ready)
**Architect:** Quanpt1 & Antigravity AI

## 1. TỔNG QUAN HỆ THỐNG
`SKILL_BAT_AI` không phải là một tập hợp các script đơn lẻ. Đây là một **Hệ điều hành Chạy ngầm (Daemon)** quản trị toàn bộ vòng đời làm việc của các AI Agent. 
Cốt lõi của nó là **Core Engine** gồm 6 module kết nối chặt chẽ với nhau:
- **TaskEngine**: Trái tim điều phối vòng đời của 1 công việc (Task).
- **RiskEngine**: Bộ não đánh giá rủi ro (R0 - R5) dựa trên file `risk_matrix.json`.
- **AuthzEngine**: Hàng rào bảo mật. Phân tích quyền hạn của Agent dựa trên file `authorization.json`.
- **ExecutionEngine**: Bàn tay thực thi. Có khả năng tự Retry, tự Validation.
- **EscalationEngine**: Tổng đài cấp cứu. Sinh Ticket gọi Quanpt1 khi hệ thống kẹt ở R4/R5 hoặc Lỗi không thể khắc phục.
- **LearningEngine**: Tế bào tiến hóa. Tự động học rule mới từ quyết định của Quanpt1.

## 2. CÁCH VẬN HÀNH (VÒNG LẶP SỰ KIỆN)
Hệ thống hoạt động theo mô hình **Zero-Touch (Không cần chạm)**.
1. Bạn chạy `start_daemon.bat` (Hoặc chạy ngầm SupervisorDaemon trên Linux).
2. Khi có 1 sự kiện hoặc file log quăng vào thư mục `mock_logs` (sau này là Webhook thực tế).
3. `EventWatcher` sẽ bắt lấy nó, giải mã và gửi cho `TaskEngine`.
4. AI sẽ tự đánh giá rủi ro -> tự kiểm tra quyền -> tự thực thi -> tự lưu log vào `ai_workforce.db` (SQLite).
5. Bạn KHÔNG PHẢI LÀM GÌ CẢ. Mọi thứ hoàn toàn tự động.

## 3. CƠ CHẾ LEO THANG (ESCALATION) & MÃ BẢO MẬT (SECRET)
Hệ thống cực kỳ an toàn. 
- Nó cấm tuyệt đối các hành động R5. 
- Nó sẽ ngưng lại và chờ bạn duyệt đối với R4 hoặc lỗi mới (Zero-day).
Khi đó, Task sẽ chuyển sang trạng thái `PENDING_HUMAN`. 
Để phê duyệt, bạn phải truyền mã bảo mật qua biến môi trường:
```bash
set QUANPT1_APPROVAL_SECRET=YOUR_SECRET_HERE
```
Và gọi hàm `resolve_ticket` trong `EscalationEngine`. Nếu bạn truyền sai, Ticket lập tức bị từ chối.

## 4. CƠ CHẾ TỰ HỌC (SELF-LEARNING)
Chỉ duy nhất Quanpt1 (người có mã Secret) mới có quyền dạy hệ thống.
Khi bạn giải quyết 1 Ticket, bạn có thể truyền thêm `learned_action` và `learned_risk` vào hàm `resolve_ticket`. Hệ thống sẽ tự động cập nhật `risk_matrix.json` và lần sau sẽ không làm phiền bạn nữa!

---
*Chúc mừng bạn đã sở hữu một Cỗ máy Vận hành AI tự chủ và an toàn tuyệt đối!*
