# SOP: Bảo trì Giao diện V4 (UI Maintenance)

## 1. Mục đích
Duy trì giao diện ánh sáng (Light Theme) chuẩn DCIM cho toàn bộ Dashboard V4 (React & HTML).

## 2. Các bước thực hiện
- **B1:** Khi có yêu cầu thay đổi màu sắc, không sửa trực tiếp mã nguồn React nếu không cần thiết.
- **B2:** Sử dụng CSS Injection (ví dụ trong `index.html`) để override bằng `!important`.
- **B3:** Luôn đảm bảo độ tương phản: nền sáng (`#f1f5f9`), khung trắng (`#ffffff`), chữ đậm (`#1e293b`).
