# Hệ thống quản lý kho máu

def display_inventory(inventory):
    if not inventory:
        print("Kho máu hiện chưa có túi máu nào.")
        return
    print("--- DANH SÁCH KHO MÁU ---")
    print(f"{"Mã Túi":<8}|{"Người Hiến":<15}|{"Nhóm Máu":<10}|{"Thể Tích":<15}|{"Ngày Hết Hạn":<15}")
    print("--------------------------------------------------------------")
    blood_inventory_stock = 0
    for blood in inventory:
        blood_replace = blood.replace("-","|")
        blood_replace = blood_replace.replace("||","-|")
        blood_split = blood_replace.split("|")
        blood_inventory_stock += int(blood_split[3])
        print(f"{blood_split[0]:<8}|{blood_split[1]:<15}|{blood_split[2]:<10}|{blood_split[3]:<12} ml|{blood_split[4]:<15}")
    print("--------------------------------------------------------------")
    print(f'Tổng thể tích máu trong kho: {blood_inventory_stock} ml.')

def add_blood_bag(inventory):
    blood_bag_id = input("Nhập mã túi máu mới: ")
    donor_name = input("Nhập tên người hiến: ")
    blood_type = input("Nhập nhóm máu: ")
    blood_volume = input("Nhập thể tích (ml): ")
    expiry_date = input("Nhập ngày hết hạn (DD/MM/YYYY): ")
def main():
    blood_inventory = [
        "BL001-Nguyen Van A-O+-250-31/12/2026",
        "BL002-Tran Thi B-A--350-15/11/2026",
        "BL003-Le Van C-AB+-250-20/10/2026"
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===
    1. Xem danh sách túi máu trong kho
    2. Nhập túi máu mới
    3. Gia hạn / Sửa ngày hết hạn
    4. Xuất / Hủy túi máu
    5. Thoát chương trình 
    ======================================== 
    Chọn chức năng (1-5): """)
        match choice:
            case "1":
                display_inventory(blood_inventory)
            case "1":
                pass
            case "1":
                pass
            case "1":
                pass
            case "5":
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            case _:
                print("Vui lòng chọn từ 1-5")

main()