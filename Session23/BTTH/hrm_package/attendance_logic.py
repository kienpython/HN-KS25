from Session23.BTTH.hrm_package.feature import check_exits
def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()
    attendance_finded = check_exits(attendance_book, employee_id)
    if attendance_finded:
        print("Mã nhân viên không được trùng!")
        return
    employee_name = input("Nhập tên nhân viên: ")
    open_time = input("Nhập giờ vào (HH:MM): ")
    attendance_book.append(
        {
            "id": employee_id, 
            "name": employee_name, 
            "times": (open_time, None)
        }
        )
    print("Thành công: Đã ghi nhận NV04 chấm công vào lúc 09:00!")