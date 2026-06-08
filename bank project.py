class BankAccount:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def show_details(self):
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)


class BankAccount:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def show_details(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)



#  Taking input from user
name = input("Enter account holder name : ")
acc_no = int(input("Enter account number : "))
balance = float(input("Enter initial balance : "))

# Object creation
account = BankAccount(name, acc_no, balance)

# Deposit input
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

# Withdraw input
withdraw_amount = float(input("Enter withdraw amount: "))
account.withdraw(withdraw_amount)

# Show final details
account.show_details()

