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

def check_exits(inventory, blood_bad_id):
    check = False
    for inv in inventory:
        if inv.split("-")[0] == blood_bad_id:
            check = True
    return check

def add_blood_bag(inventory):
    blood_bag_id = input("Nhập mã túi máu mới: ").strip().upper()
    if not blood_bag_id:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    if not check_exits(inventory,blood_bag_id):
        donor_name = input("Nhập tên người hiến: ").title()
        if not donor_name:
            print("Lỗi: Tên người hiến không được để trống!")
            return
        blood_type = input("Nhập nhóm máu: ").strip().upper()
        blood_volume = input("Nhập thể tích (ml): ")
        if not blood_volume.isdigit():
            print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
            return
        expiry_date = input("Nhập ngày hết hạn (DD/MM/YYYY): ")
        new_blood_bag = f"{blood_bag_id}-{donor_name}-{blood_type}-{blood_volume}-{expiry_date}"
        inventory.append(new_blood_bag)
        print(f"Thành công: Đã nhập túi máu {blood_bag_id} vào kho!")
        print("Sau khi chuẩn hóa, dữ liệu được lưu vào list là: ")
        print(new_blood_bag)
    else:
        print("Lỗi: Mã túi máu BL001 đã tồn tại! Vui lòng nhập mã khác.")


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
            case "2":
                add_blood_bag(blood_inventory)
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            case _:
                print("Vui lòng chọn từ 1-5")

main()