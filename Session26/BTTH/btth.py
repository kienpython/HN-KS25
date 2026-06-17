from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.employee = ""
    
    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: {self.employee}")

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus
        self.employee = "Full-time"

    def calculate_salary(self):
        return self.base_salary + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate
        self.employee = "Part-time"
    def calculate_salary(self):
        return self.working_hours * self.hourly_rate

class InternEmployee(Employee):
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance
        self.employee = "Intern"
    def calculate_salary(self):
        return self.allowance

def display_employees(employees):
    print("--- DANH SÁCH NHÂN VIÊN ---")
    for employee in employees:
        employee.display_info()

def display_salaries(employees):
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for employee in employees:
        print(f"{employee.employee_id} | {employee.name} | Lương: {employee.calculate_salary():,.0f} VND")

def main():
    while True:
        employees = [
            FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
            PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
            InternEmployee("E003", "Le Van C", 3000000)
        ]
        choice = input("""=== EMPLOYEE SALARY MANAGER ===
                1. Xem danh sách nhân viên
                2. Tính lương toàn bộ nhân viên
                3. Thoát chương trình
                ================================
                Chọn chức năng (1-3): """)
        match choice:
            case "1":
                display_employees(employees)
            case "2":
                display_salaries(employees)
            case "3":
                pass
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
                return

if __name__ == "__main__":
    main()