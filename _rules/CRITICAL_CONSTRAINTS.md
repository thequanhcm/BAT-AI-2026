# ⚖️ QUY TẮC CỐT LÕI (CRITICAL CONSTRAINTS)

> [!CAUTION]
> Đây là những ranh giới cấm kỵ mà các AI Agent KHÔNG ĐƯỢC PHÉP vi phạm dưới mọi hình thức.

1. **Bảo toàn Dữ liệu:** Tuyệt đối KHÔNG xóa, DROP TABLE, hoặc ghi đè dữ liệu lịch sử của V3.
2. **Phê duyệt (Approval):** Bất kỳ thay đổi nào liên quan đến cấu hình mạng (IP, Port) của `BOT_PDL` phải dừng lại và hỏi ý kiến người dùng.
3. **Dependencies:** Không tự ý `npm install` hoặc cập nhật thư viện lõi của React trong V4 nếu chưa được lệnh rõ ràng, tránh gây crash build.
4. **Giao diện:** Luôn giữ tính nhất quán của theme sáng DCIM. Không được tự ý đưa các màu chói lóa ngoài bộ màu Viettel (Xanh lá, Xanh dương) vào hệ thống.
