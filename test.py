# Việc lạm dụng from math import * lại được coi là một "Anti-pattern" (thực hành xấu) trong Python
# Dễ bị trùng tên hàm với hàm tự viết
# Khó đọc code vì không biết hàm đến từ đâu
# Khó bảo trì khi dự án lớn
# Nêu dùng import math


# Đánh dấu thư mục là Package Python
# Cho phép import các module bên trong thư mục đó

#rikkei_logistics
# - main.py
# - core
# +__init__.py
# + geo_calculator.py
# + time_estimator.py
# - utils
# + __init__.py
# + file_helper.py
# - logs

from datetime import datetime
# from utils.file_helper import create_log_dir
# from core.geo_calculator import calculate_distance
# from core.time_estimator import predict_eta

shipments = [
    {
        "id": "TRK-001",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 10.8231,
        "to_lon": 106.6297,
        "depart": "2026-06-10 08:00:00",
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002",
        "from_lat": 21.0285,
        "from_lon": 105.8542,
        "to_lat": 16.0544,
        "to_lon": 108.2022,
        "depart": "2026-06-10 09:30:00",
        "deadline": "2026-06-10 15:00:00"
    }
]

print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
# create_log_dir("logs")
print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
print("-" * 75)
for shipment in shipments:
    # distance = calculate_distance(
    #     shipment["from_lat"],
    #     shipment["from_lon"],
    #     shipment["to_lat"],
    #     shipment["to_lon"])
    # eta = predict_eta(shipment["depart"],distance)
    deadline = datetime.strptime(
        shipment["deadline"],"%Y-%m-%d %H:%M:%S")
    print(f'[CHUYẾN XE {shipment['id']}]')
    # print(f'+ Khoảng cách vận chuyển: {distance:.2f} km')
    print(f'+ Thời gian khởi hành: {shipment['depart']}')
    # print(f' + Dự kiến cập bến (ETA): {eta}')
    # if eta <= deadline:
    #     print(f'+ Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)')
    # else:
    #     print(f'+ Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline.time()})')
    # print()
print("=" * 56)