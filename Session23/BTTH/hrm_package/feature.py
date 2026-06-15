def check_exits(attendance_book, employee_id):
    for attendance in attendance_book:
        if attendance['id'] == employee_id:
            return attendance
    return False