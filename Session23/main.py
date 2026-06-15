from hrm_package.ui_display import display_records
from hrm_package.attendance_logic import clock_in
from hrm_package.feature import check_exits
from hrm_package.time_calc import evaluate_flex_time

def clock_out(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()
    break_time = input("Nhập giờ ra: ")
    attendance = check_exits(attendance_book,employee_id)
    if not attendance:
        print("Nhân viên không tồn tại!")
        return
    attendance_time = attendance['times']
    open_in = attendance_time[0]
    attendance["times"] = (open_in,break_time)
    print("Chấm công thành công!")



def main():
    attendance_book = [
        {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
        {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, # Đang làm việc, chưa chấm công ra
        {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
    ]
    while True:
        choice = input("""=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===
            1. Xem bảng chấm công ngày
            2. Chấm công Vào (Clock-in)
            3. Chấm công Ra (Clock-out)
            4. Đánh giá vi phạm
            5. Thoát chương trình 
            ================================================= 
            Chọn chức năng (1-5):""")
        match choice:
            case "1":
                display_records(attendance_book)
            case "2":
                clock_in(attendance_book)
            case "3":
                clock_out(attendance_book)
            case "4":
                evaluate_flex_time(attendance_book)
            case "5":
                break

if __name__ == "__main__":
    main()