import logging

def find_ticket_by_id(tickets, ticket_id):
    for ticket in tickets:
        if ticket_id == ticket['ticket_id']:
            return ticket
    return False

def change_seat(tickets):
    ticket_id = input("Nhập mã vé: ").strip().upper()
    ticket = find_ticket_by_id(tickets, ticket_id)
    if not ticket:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")
        return
    new_seat_zone = input("Nhập khu vực ghế mới: ").strip().upper()
    new_seat_quantities = input_positive_int("Nhập số ghế mới: ")
    new_seat = (new_seat_zone,new_seat_quantities)
    ticket['seat'] = new_seat
    print(f"Thành công: Đã đổi chỗ vé {ticket_id} sang {new_seat_zone}-{new_seat_quantities}.")
    logging.info(f"Seat changed for ticket {ticket_id} to {new_seat_zone}-{new_seat_quantities}")

def cancel_ticket(tickets):
    ticket_id = input("Nhập mã vé: ").strip().upper()
    ticket = find_ticket_by_id(tickets,ticket_id)
    if not ticket:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")
    
    if ticket['status'] == "Cancelled":
        print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
    
    ticket["status"] = "Cancelled"
    logging.warning(f"Ticket {ticket_id} has been cancelled.")

def book_ticket(tickets):
    ticket_id = input("Nhập mã vé: ").strip().upper()
    if find_ticket_by_id(tickets,ticket_id):
            print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
            logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
            return
    buyer_name = input("Nhập tên khách hàng: ").strip().title()
    price = input_positive_float("Nhập giá vé: ")
    seet_zone = input("Nhập khu vực ghế: ").strip().upper()
    seat_quantities = input_positive_int("Nhập khu vực ghế: ")
    seat = (seet_zone,seat_quantities)
    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": seat
    }
    tickets.append(new_ticket)
    print(f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")

def input_positive_float(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0 :
                print("Giá vé phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Giá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")


def input_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0 :
                print("Số ghế phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            return value
        except ValueError:
            print("Số ghế phải là số nguyên. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

        

def display_tickets(tickets):
    if not tickets:
        print("Hiện chưa có vé nào trong hệ thống.")
        return
    
    print("--- DANH SÁCH VÉ ---\n",
          f"Mã Vé | Tên Khách Hàng  | Giá Vé  | Chỗ Ngồi | Trạng Thái\n",
          "-----------------------------------------------------------")
    
    for ticket in tickets:
        try:
            ticket_code = ticket["ticket_id"]
            ticket_name = ticket["buyer_name"]
            ticket_price = ticket["price"]
            ticket_seat = ticket["seat"]
            seat_text = f"{ticket_seat[0]}-{ticket_seat[1]}"
            ticket_status = ticket["status"]
            if ticket_status == "Cancelled":
                ticket_status  += " [ĐÃ HỦY]"
            print(f"{ticket_code}   | {ticket_name}    | {ticket_price}   | {seat_text}      | {ticket_status}")
        except KeyError as error:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            logging.error(f"Missing key while displaying ticket: {error}")
            break
    print("-----------------------------------------------------------")

def calculate_revenue(tickets):
    total_revenue = 0.0
    count_ticket_booked = 0
    count_ticket_refunded = 0
    for ticket in tickets:
        try:
            if ticket['status'] == "Booked":
                total_revenue += ticket['price']
                count_ticket_booked += 1
            if ticket['status'] == "Cancelled":
                count_ticket_refunded +=1
        except KeyError as error:
            logging.error(f"Missing key while calculating revenue: 'price'")
    print("Tổng số vé đã đặt:",count_ticket_booked)
    print("Tổng số vé đã hủy:",count_ticket_refunded)
    print("Tổng doanh thu hợp lệ:",total_revenue)
    return total_revenue


def main():
    logging.basicConfig(
        filename="Session21/arena_tickets.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
        )
    ticket_db = [
        {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
        {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
        {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
    ]
    while True:
        choice = input("""=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===
            1. Xem danh sách vé đã bán
            2. Đặt vé mới
            3. Đổi chỗ ngồi (Cập nhật vé)
            4. Hủy vé
            5. Báo cáo doanh thu
            6. Thoát chương trình
            ======================================== 
            Chọn chức năng (1-6):""")
        match choice:
            case "1":
                display_tickets(ticket_db)
            case "2":
                book_ticket(ticket_db)
            case "3":
                change_seat(ticket_db)
            case "4":
                cancel_ticket(ticket_db)
            case "5":
                calculate_revenue(ticket_db)
            case "6":
                print(f"Cảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports.")
                logging.info("Ticket management system closed.")
                break
    


if __name__ == "__main__":
    main()