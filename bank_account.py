class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)
        print("Updated Balance:", self.balance)
        print("..........................................")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Amount Withdrawn:", amount)
        print("Updated Balance:", self.balance)
        print("..........................................")

    def check_balance(self):
        print("Account Number:", self.account_no)
        print("Current Balance:", self.balance)
        print("..........................................")


account1 = BankAccount("200718", 50000)

account1.check_balance()
account1.deposit(500)
account1.withdraw(100)
account1.check_balance()

        