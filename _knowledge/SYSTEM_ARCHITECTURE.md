# Kiến trúc Hệ thống (System Architecture)

## 1. BATTERY_AI_V4
- Hệ thống hiện đại, giao diện ReactJS kết hợp HTML tĩnh, áp dụng giao diện DCIM (Light Theme).
- Đóng vai trò là Dashboard chính theo dõi 3D Digital Twin, Health Score, và AI Prediction.

## 2. BATTERY_AI_V3
- Phiên bản Legacy (cũ hơn), cần được duy trì sự ổn định.
- Không được phép tự ý thay đổi dữ liệu lịch sử hoặc xóa bỏ cấu trúc cũ.

## 3. BOT_PDL
- Chứa các kịch bản chạy BOT (ví dụ `bot_tb.py`, `bot_pauctt.py`).
- Sử dụng mô hình Monolithic Supervisor (`run_all_bots_monolithic.py`) để gom chung cửa sổ Terminal, theo dõi và tự động khởi động lại.
