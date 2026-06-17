from abc import ABC, abstractmethod


def format_money(amount):
    return f"{amount:,.0f} VND"


def input_money(message):
    while True:
        value = input(message).replace(",", "").strip()

        try:
            amount = float(value)

            if amount <= 0:
                print("Số tiền phải lớn hơn 0.")
                continue

            return amount

        except ValueError:
            print("Vui lòng nhập số hợp lệ.")


class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = " ".join(value.upper().split())

    def _increase_balance(self, amount):
        self.__balance += amount

    def _decrease_balance(self, amount):
        self.__balance -= amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented

        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented

        return self.balance < other.balance

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name


class SavingsAccount(BaseAccount):
    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._increase_balance(amount)
        print("Nạp tiền thành công!")
        print(f"Số dư mới: {format_money(self.balance)}")

    def withdraw(self, amount):
        penalty_fee = amount * 0.02
        total_amount = amount + penalty_fee

        if total_amount > self.balance:
            print("Số dư không đủ để rút tiền và trả phí phạt.")
            return False

        self._decrease_balance(total_amount)

        print("Rút tiền thành công!")
        print(f"Số tiền rút: {format_money(amount)}")
        print(f"Phí phạt rút trước hạn 2%: {format_money(penalty_fee)}")
        print(f"Số dư còn lại: {format_money(self.balance)}")

        return True

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self._increase_balance(interest)

        print(f"Số dư trước tính lãi: {format_money(self.balance - interest)}")
        print(f"Lãi suất năm: {self.interest_rate * 100:.1f}%")
        print(f"Tiền lãi nhận được: +{format_money(interest)}")
        print(f"Số dư mới: {format_money(self.balance)}")


class CreditAccount(BaseAccount):
    def __init__(self, account_number, owner_name, credit_limit, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        self._increase_balance(amount)
        print("Nạp tiền thành công!")
        print(f"Số dư mới: {format_money(self.balance)}")

    def withdraw(self, amount):
        if self.balance - amount < -self.credit_limit:
            print("Vượt quá hạn mức thấu chi cho phép.")
            return False

        self._decrease_balance(amount)

        print("Rút tiền thành công! Có thể sử dụng hạn mức thấu chi.")
        print(f"Số tiền rút: {format_money(amount)}")
        print(f"Số dư hiện tại: {format_money(self.balance)}")

        return True


class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5_000_000:
            cashback = amount * 0.01
            self._increase_balance(cashback)

            print(
                f"[Ưu đãi Premium]: Bạn được hoàn tiền 1% "
                f"({format_money(cashback)}) vào tài khoản!"
            )


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    pass


class VNPayGateway:
    def execute_pay(self, account, amount):
        print(f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}...")

        success = account.withdraw(amount)

        if success:
            print("Xác thực thanh toán bằng Duck Typing thành công!")
            print(f"Tài khoản đã thanh toán hóa đơn: {format_money(amount)}")
            print(f"Số dư mới: {format_money(account.balance)}")


class ViettelMoneyGateway:
    def execute_pay(self, account, amount):
        print(f"[Viettel Money]: Đang kết nối tới tài khoản {account.account_number}...")

        success = account.withdraw(amount)

        if success:
            print("Xác thực thanh toán bằng Duck Typing thành công!")
            print(f"Tài khoản đã thanh toán hóa đơn: {format_money(amount)}")
            print(f"Số dư mới: {format_money(account.balance)}")


def process_payment(payment_gateway, account, amount):
    try:
        payment_gateway.execute_pay(account, amount)
    except AttributeError:
        print("Cổng thanh toán không hợp lệ hoặc chưa được tích hợp.")


def display_menu():
    print("""
===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin & Kiểm tra MRO
3. Giao dịch Nạp / Rút tiền
4. Tích lũy / Áp dụng lãi suất định kỳ
5. Gộp tài khoản & So sánh
6. Thanh toán hóa đơn qua Cổng trung gian
7. Thoát chương trình
==============================================
""")


def open_account(accounts):
    print("--- CHỌN LOẠI TÀI KHOẢN ---")
    print("1. Savings Account")
    print("2. Credit Account")
    print("3. Hybrid Account")

    account_type = input("Chọn loại tài khoản (1-3): ").strip()

    account_number = input("Nhập số tài khoản 10 chữ số: ").strip()

    if not BaseAccount.validate_account_number(account_number):
        print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
        return None

    for account in accounts:
        if account.account_number == account_number:
            print("Số tài khoản đã tồn tại.")
            return None

    owner_name = input("Nhập tên chủ tài khoản: ")

    if account_type == "1":
        interest_rate = float(input("Nhập lãi suất năm VD 0.05: "))
        account = SavingsAccount(account_number, owner_name, interest_rate)

        print("Mở tài khoản Tiết kiệm thành công!")

    elif account_type == "2":
        credit_limit = input_money("Nhập hạn mức tín dụng: ")
        account = CreditAccount(account_number, owner_name, credit_limit)

        print("Mở tài khoản Tín dụng thành công!")

    elif account_type == "3":
        interest_rate = float(input("Nhập lãi suất năm VD 0.05: "))
        account = HybridAccount(account_number, owner_name, interest_rate)

        print("Mở tài khoản Hybrid thành công!")

    else:
        print("Loại tài khoản không hợp lệ.")
        return None

    accounts.append(account)

    print(f"Chủ tài khoản: {account.owner_name}")
    print(f"Số tài khoản: {account.account_number}")

    return account


def show_account_info(current_account):
    if current_account is None:
        print("Hệ thống chưa có thông tin tài khoản.")
        return

    print("--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
    print(f"Loại tài khoản: {current_account.__class__.__name__}")
    print(f"Ngân hàng: {current_account.bank_name}")
    print(f"Số tài khoản: {current_account.account_number}")
    print(f"Chủ tài khoản: {current_account.owner_name}")
    print(f"Số dư: {format_money(current_account.balance)}")

    if isinstance(current_account, SavingsAccount):
        print(f"Lãi suất: {current_account.interest_rate * 100:.1f}% / năm")

    if isinstance(current_account, CreditAccount):
        print(f"Hạn mức tín dụng: {format_money(current_account.credit_limit)}")

    print("--- MRO ---")
    for cls in current_account.__class__.mro():
        print(cls.__name__)


def transaction(current_account):
    if current_account is None:
        print("Vui lòng mở tài khoản trước.")
        return

    print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
    print("1. Nạp tiền")
    print("2. Rút tiền")

    choice = input("Chọn giao dịch (1-2): ").strip()

    if choice == "1":
        amount = input_money("Nhập số tiền nạp: ")
        current_account.deposit(amount)

        if isinstance(current_account, DigitalPremiumMixin):
            current_account.cashback_reward(amount)
            print(f"Số dư sau ưu đãi: {format_money(current_account.balance)}")

    elif choice == "2":
        amount = input_money("Nhập số tiền cần rút: ")
        current_account.withdraw(amount)

    else:
        print("Lựa chọn không hợp lệ.")


def apply_interest_feature(current_account):
    if current_account is None:
        print("Vui lòng mở tài khoản trước.")
        return

    if isinstance(current_account, SavingsAccount):
        print("--- TÍNH LÃI ĐỊNH KỲ ---")
        current_account.apply_interest()
    else:
        print("Tài khoản này không hỗ trợ tính lãi.")


def choose_other_account(accounts, current_account):
    available_accounts = [
        account for account in accounts
        if account is not current_account
    ]

    if not available_accounts:
        print("Không có tài khoản đối ứng để so sánh.")
        return None

    print("--- DANH SÁCH TÀI KHOẢN ĐỐI ỨNG ---")

    for index, account in enumerate(available_accounts, start=1):
        print(
            f"{index}. {account.account_number} - "
            f"{account.owner_name} - "
            f"{format_money(account.balance)}"
        )

    choice = input("Chọn tài khoản đối ứng: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ.")
        return None

    choice = int(choice)

    if choice < 1 or choice > len(available_accounts):
        print("Lựa chọn không hợp lệ.")
        return None

    return available_accounts[choice - 1]


def compare_accounts(accounts, current_account):
    if current_account is None:
        print("Vui lòng mở tài khoản trước.")
        return

    other_account = choose_other_account(accounts, current_account)

    if other_account is None:
        return

    print("--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN ---")
    print(
        f"Tài khoản A: {current_account.owner_name} "
        f"({format_money(current_account.balance)})"
    )
    print(
        f"Tài khoản B: {other_account.owner_name} "
        f"({format_money(other_account.balance)})"
    )

    if current_account < other_account:
        print("Số dư tài khoản A NHỎ HƠN tài khoản B.")
    else:
        print("Số dư tài khoản A KHÔNG NHỎ HƠN tài khoản B.")

    total = current_account + other_account

    print(f"Tổng số tiền của cả 2 tài khoản: {format_money(total)}")


def payment_feature(current_account):
    if current_account is None:
        print("Vui lòng mở tài khoản trước.")
        return

    print("--- THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN ---")
    print("1. Thanh toán qua VNPay")
    print("2. Thanh toán qua Viettel Money")

    choice = input("Chọn cổng thanh toán (1-2): ").strip()
    amount = input_money("Nhập số tiền hóa đơn: ")

    if choice == "1":
        gateway = VNPayGateway()
    elif choice == "2":
        gateway = ViettelMoneyGateway()
    else:
        print("Cổng thanh toán không hợp lệ.")
        return

    process_payment(gateway, current_account, amount)


def main():
    accounts = []
    current_account = None

    while True:
        display_menu()

        choice = input("Chọn chức năng (1-7): ").strip()

        try:
            if choice == "1":
                new_account = open_account(accounts)

                if new_account is not None:
                    current_account = new_account

            elif choice == "2":
                show_account_info(current_account)

            elif choice == "3":
                transaction(current_account)

            elif choice == "4":
                apply_interest_feature(current_account)

            elif choice == "5":
                compare_accounts(accounts, current_account)

            elif choice == "6":
                payment_feature(current_account)

            elif choice == "7":
                print("Cảm ơn đã trải nghiệm hệ thống Vietcombank Digibank Pro Simulator!")
                break

            else:
                print("Chức năng không hợp lệ.")

        except ValueError:
            print("Dữ liệu nhập không hợp lệ.")
        except TypeError:
            print("Thao tác không hợp lệ với kiểu dữ liệu hiện tại.")


if __name__ == "__main__":
    main()