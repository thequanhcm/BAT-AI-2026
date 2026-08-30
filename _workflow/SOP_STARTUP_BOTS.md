# SOP: Khởi động và Giám sát BOT_PDL

## 1. Mục đích
Đảm bảo hệ thống bot luôn chạy ngầm ổn định, tự động khôi phục khi mất mạng hoặc lỗi code.

## 2. Các bước thực hiện
- **B1:** Kiểm tra trạng thái tiến trình Python liên quan đến `run_all_bots_monolithic.py`.
- **B2:** Nếu chưa chạy, thực thi `run_all_bots.bat`.
- **B3:** Theo dõi log để phát hiện lỗi. Nếu bot crash, hệ thống Supervisor sẽ tự khởi động lại.
- **B4:** Cập nhật trạng thái hiển thị cho người dùng (Terminal hoặc UI).
