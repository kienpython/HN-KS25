from tabulate import tabulate

class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self._price = price
        self.is_available = True
    @property 
    def price(self):
        return self._price
    
    def get_status(self):
        if self.is_available:
            return "Đang bán"
        return "Ngừng bán"
    
    def toggle_available(self):
        self.is_available = not self.is_available

def display_drink(menu):
    drinks = list()
    for drink in menu:
        drinks.append([drink.code, drink.name, drink.price, drink.get_status()])
    print("-- DANH SÁCH ĐỒ UỐNG ---")
    table = tabulate(
        drinks, 
        ["Mã món","Tên món","Giá bán","Trạng thái"], 
        tablefmt='pipe'
    )
    print(table)

def check_exits(menu, drink_id):
    for drink in menu:
        if drink.code == drink_id:
            return drink
    return False

def validate_price():
    try :
        price = float(input("Nhập giá bán: "))
        if price <= 0 :
            print("Giá bán không hợp lệ!")
            return False
        return price
    except ValueError as err:
        print("Giá bán không hợp lệ!")
        return False
    
def add_drink(menu):
    drink_id = input("Nhập mã món: ").strip().upper()
    drink = check_exits(menu, drink_id)
    if drink:
        print("Mã món đã tồn tại trong hệ thống!")
        return
    drink_name = input("Nhập tên món: ")
    drink_price = validate_price()
    menu.append(Drink(drink_id,drink_name,drink_price))

def update_status(menu):    
    drink_id = input("Nhập mã món: ").strip().upper()
    drink = check_exits(menu,drink_id)
    if not drink:
        print("Không tìm thấy món có mã này!")
        return
    drink.toggle_available()
    print("""Đã cập nhật trạng thái món CF01.
        Trạng thái hiện tại: Ngừng bán""")

def main():    
    menu = [
        Drink("CF01", "Cà phê sữa", 35000),
        Drink("TS01", "Trà sữa matcha", 45000),
        Drink("TD01", "Trà đào cam sả", 40000)
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===
        1. Xem danh sách đồ uống
        2. Thêm đồ uống mới
        3. Cập nhật trạng thái kinh doanh
        4. Thoát chương trình
        ==============================================
        Chọn chức năng (1-4): """)
        match choice:
            case "1":
                display_drink(menu)
            case "2":
                add_drink(menu)
            case "3":
                update_status(menu)
            case "4":
                break

if __name__ == "__main__":
    main()