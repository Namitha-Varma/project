class DigitalWallet:

    
    company_name = "PayFlow"
    max_wallet_limit = 50000

    
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.balance = balance
        self.history = []

   
    def add_money(self, amount):

        if not DigitalWallet.is_valid_amount(amount):
            print("Invalid amount!")
            return

        if self.balance + amount > DigitalWallet.max_wallet_limit:
            print("Wallet limit exceeded!")
            return

        self.balance += amount
        self.history.append(f"Added ₹{amount}")

        print(f"₹{amount} added successfully")

    
    def pay(self, amount):

        if not DigitalWallet.is_valid_amount(amount):
            print("Invalid amount!")
            return

        if amount > 10000:
            print("Transaction limit exceeded!")
            return

        final_amount = DigitalWallet.apply_transaction_fee(amount)

        if final_amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= final_amount
        self.history.append(f"Paid ₹{final_amount}")

        print(f"Payment successful. ₹{final_amount} deducted")

    
    def check_balance(self):
        return f"Current Balance: ₹{self.balance}"

    
    def show_history(self):
        print("Transaction History:")
        for item in self.history:
            print(item)

    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    
    @staticmethod
    def apply_transaction_fee(amount):
        fee = amount * 0.02
        return amount + fee




user1 = DigitalWallet("Namitha", 5000)
user2 = DigitalWallet("Rahul", 10000)


user1.add_money(2000)


user1.pay(1000)


print(user1.check_balance())


DigitalWallet.change_company_name("QuickPay")

print("Company Name:", user1.company_name)
print("Company Name:", user2.company_name)


user1.show_history()