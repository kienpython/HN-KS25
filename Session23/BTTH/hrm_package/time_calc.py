from datetime import datetime
def evaluate_flex_time(attendance_book):
    for attendance in attendance_book:
        time = attendance['times']
        clock_in = time[0]
        clock_out = time[1]
        if clock_in and clock_out:
            clock_in_format = datetime.strptime(clock_in,"%H:%M")
            clock_out_format = datetime.strptime(clock_out,"%H:%M")
            if  clock_in_format > datetime.strptime("10:00","%H:%M"):
                print(f"{attendance['id']} - Vi phạm: Đến muộn quá 90 phút.")
            elif (clock_out_format-clock_in_format).seconds / 3600 >= 9: 
                print(f"{attendance['id']} - Hợp lệ: Hoàn thành ca làm việc.")
            else:
                print(f"{attendance['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")