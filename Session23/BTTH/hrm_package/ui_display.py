from tabulate import tabulate

def display_records(attendance_book):
    attendance_list = list()
    for attendance in attendance_book:
        attendance_time = attendance['times']
        open_time = attendance_time[0]
        break_time = attendance_time[1]
        if not break_time:
            break_time = "[Đang làm việc]"
        attendance_list.append([attendance['id'],attendance['name'],open_time,break_time])
             
    table = tabulate(
        attendance_list, 
        headers=["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"], 
        tablefmt="grid"
    )

    print(table)