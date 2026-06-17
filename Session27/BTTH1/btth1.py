from abc import ABC, abstractmethod

class BaseAccount(ABC):
    bank_name = "Vietcombank"
    def __init__(self, balance, account_number, account_name):
        self.__balance = balance
        self.account_number = account_number
        self.account_name = account_name
    
    @property
    def balance(self):
        return self.__balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        return self.balance + other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def _increase_balance(self, amount):
        self.__balance += amount
    
    def _decrease_balance(self, amount):
        self.__balance -= amount

    @staticmethod
    def validate_account_number(account_number):
        if account_number.isdigit() and len(account_number)==10:
            return True
        return False

    @classmethod
    def update_bank_name(cls, new_name):
        pass

class SavingsAccount(BaseAccount):
    def __init__(self, interest_rate, account_number, account_name, balance=0):
        super().__init__(balance, account_number, account_name)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self._increase_balance(amount)
        print("Nạp tiền thành công!")
        print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({float(amount)*0.01} VND) vào tài khoản!")
        print(f"Số dư hiện tại là {self.balance:,.0f} VND")

    def withdraw(self, amount):
        if self.balance <= 0:
            print("Ban khong con tien de rut")
            return
        penalty_fee = amount * 0.02
        total_amount = amount + penalty_fee
        self._decrease_balance(total_amount)
        print("Rút tiền thành công!")
        print(f"Số tiền rút: {amount:,.0f} VND")
        print(f"Phí phạt rút trước hạn (2%): {amount*0.2} VND")
        print(f"Số dư còn lại: {self.balance} VND")
    
    def apply_interest(self):
        print(f"Số dư trước tính lãi: {self.balance} VND")
        print(f"Lãi suất năm: {self.interest_rate*100}%")
        print(f"Tiền lãi nhận được: +{self.balance * self.interest_rate} VND")
        self._increase_balance(self.balance * self.interest_rate)
        print(f"Số dư mới sau khi cộng lãi: {self.balance} VND")

class CreditAccount(BaseAccount):
    def __init__(self,credit_limit, account_number, account_name, balance = 0):
        super().__init__(balance, account_number, account_name)
        self.credit_limit = credit_limit
    
    def deposit(self, amount):
        self._increse_balance(amount)
        print("Nạp tiền thành công!")
        print(f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({float(amount)*0.01} VND) vào tài khoản!")
        print(f"Số dư hiện tại là {self.balance:,.0f} VND")

    def withdraw(self, amount):
        BaseAccount._decrease_balance
        if float(self.balance) - float(amount) < - self.credit_limit:
            print("Vượt quá hạn mức thấu chi cho phép.")
            return False
        self._decrease_balance(amount)
        print(f"Nhập số tiền cần rút: ")
        print("Rút tiền thành công! (Sử dụng hạn mức thấu chi)")
        print(f"Số tiền rút: {amount:,.0f} VND")
        print(f"Số dư hiện tại: {self.balance} VND")
        

class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        pass

class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass

class VNPayGateway:
    def execute_pay(self, account, amount):
        print(f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}...")
        print(f"Xác thực thanh toán bằng Duck Typing thành công!")
        print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,.0f} VND.")
        account.withdraw(amount)
        print(f"Số dư mới: {account.balance} VND.")

class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        print(f"[Hệ thống ViettelMoney]: Đang kết nối tới tài khoản {account.account_number}...")
        print(f"Xác thực thanh toán bằng Duck Typing thành công!")
        print(f"Tài khoản đã thanh toán hóa đơn giá trị: {float(amount):,.0f} VND.")
        account.withdraw(amount)
        print(f"Số dư mới: {account.balance} VND.")

def open_account(accounts, current_account):
    print("--- CHỌN LOẠI TÀI KHOẢN ---")
    choice_type_account = input("""
1. Savings Account (Tài khoản Tiết kiệm)
2. Credit Account (Tài khoản Tín dụng)
3. Hybrid Account (Tài khoản Đa năng)
Chọn loại tài khoản (1-3): """)
    account_number = input("Nhập số tài khoản 10 chữ số: ")
    if not BaseAccount.validate_account_number(account_number):
        print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
        return
    account_name = input("Nhập tên chủ tài khoản: ")
    if choice_type_account == "1":
        interest_rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
        current_account = SavingsAccount(interest_rate,account_number,account_name)
        accounts.append(current_account)
    if choice_type_account == "2":
        credit_limit = float(input("Nhập hạn mức tín dụng: "))
        current_account = CreditAccount(credit_limit,account_number,account_name)
        accounts.append(current_account)
    if choice_type_account == "3":
        interest_rate = float(input("Nhập lãi suất năm (ví dụ 0.05): "))
        current_account = HybridAccount(interest_rate,account_number,account_name)
        accounts.append(current_account)
    print("Mở tài khoản Tiết kiệm thành công!")
    print(f"Chủ tài khoản: {account_name}")
    return current_account

def display_info(current_account):
    if not current_account:
        print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return
    print(
        f"Loại tài khoản: {current_account.__class__.__name__}\n"
        f"Ngân hàng: {current_account.bank_name}\n"
        f"Số tài khoản: {current_account.account_number}\n"
        f"Chủ tài khoản: {current_account.account_name}\n"
        f"Số dư: {current_account.balance}"        
    )
    if current_account.__class__.__name__ == "SavingsAccount": 
        print(f"Lãi suất:: {float(current_account.interest_rate)*100}% / năm")

def transaction(current_account):
    if not current_account:
        print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return
    print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
    choice = input("""1. Nạp tiền
2. Rút tiền
Chọn giao dịch (1-2): """)
    if choice == "1":
        amount = float(input("Nhập số tiền cần nap: "))
        current_account.deposit(amount)
    if choice == "2":
        amount = float(input("Nhập số tiền cần rút: "))
        current_account.withdraw(amount)

def choice_other_accounts(accounts, current_account):
    position_current = 0
    for index, account in enumerate(accounts,1):
        if account.account_number == current_account.account_number:
            print(f"{index}.{account.account_number}-{account.account_name} [Tài khoản đang sử dụng]")
            position_current = index
            continue
        print(f"{index}.{account.account_number}-{account.account_name}")
    choice = input("Vui lòng chọn 1 account: ")
    if choice == position_current:
        print("Vui lòng chọn tài khoản khác với tài khoản đã mở!")
        return False
    return accounts[int(choice)-1]

def compare_accounts(accounts, current_account):
    print("--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING) ---")
    if not accounts:
        print("Hien chua co tai khoan nao!")
        return
    if not current_account:
        print("Bạn cần mở tài khoản ở bước 1 trước!")
        return
    print(f"Tài khoản hiện tại (A): {current_account.bank_name} (Số dư: {current_account.balance:,.0f} VND)")
    other_account = choice_other_accounts(accounts, current_account)
    if not other_account:
        return
    print(f"Chọn tài khoản đối ứng (B) từ danh sách hệ thống: {other_account.account_number} ({other_account.account_name} - Số dư: {other_account.balance} VND)")
    if current_account < other_account:
        print(f"[Kết quả So sánh (__lt__)]: Số dư tài khoản {current_account.account_number} NHỎ HƠN số dư tài khoản {other_account.account_number}.")
    else:
        print(f"[Kết quả So sánh (__lt__)]: Số dư tài khoản {current_account.account_number} LỚN HƠN số dư tài khoản {other_account.account_number}.")

    print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền sở hữu của cả 2 tài khoản là: {current_account + other_account} VND.")

def process_payment(payment_gateway, account, amount):
    payment_gateway.execute_pay(account, amount)

def payment_feature(current_account):
    print("--- THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN ---")
    choice = input("""1. Thanh toán qua VNPay
2. Thanh toán qua Viettel Money
Chọn cổng thanh toán (1-2): """)
    amount = float(input("Nhập số tiền hóa đơn: "))
    if choice == "1":
        payment_gateway = VNPayGateway()
    if choice == "2":
        payment_gateway = ViettelMoneyGateway()
    process_payment(payment_gateway, current_account, amount)
def main():
    accounts = [
        SavingsAccount(0.05, "0405030504", "Kien1", 100000),
        HybridAccount(0.05, "0405030504", "Kien2", 300000),
        CreditAccount(200000, "0405030504", "Kien3", 200000),
    ]
    current_account = None
    while True:
        choice = input("""===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====
            1. Mở tài khoản mới (Chọn loại tài khoản)
            2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)
            3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)
            4. Tích lũy / Áp dụng lãi suất định kỳ
            5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)
            6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)
            7. Thoát chương trình
            ==============================================
            Chọn chức năng (1-7): """)
        match choice:
            case "1":
                current_account = open_account(accounts, current_account)
            case "2":
                display_info(current_account)
            case "3":
                transaction(current_account)
            case "4":
                current_account.apply_interest()
            case "5":
                compare_accounts(accounts, current_account)
            case "6":
                payment_feature(current_account)
            case "7":
                pass
        
if __name__ == "__main__":
    main()