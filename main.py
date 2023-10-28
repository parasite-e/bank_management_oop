class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []
        self.loan_amount = 0
        self.loan_eligibility = True

    def deposit(self, amount):
        if amount <0:
            raise ValueError("Deposit amount can not be a negative number")
        
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
        else:
            print("Bank is bankrupt.")

    def check_balance(self):
        return f"{self.name}, you have {self.balance} Tk."

    def transfer(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"Transferred ${amount} to {receiver.name}")
        else:
            print("Insufficient balance.")

    def transaction_history(self):
        return self.transactions

    def take_loan(self):
            if self.loan_eligibility  == True:
                self.loan_amount = 2 * self.balance
                self.balance += self.loan_amount
                self.transactions.append(f"Loan: ${self.loan_amount}")
            else:
                print(f'currently Loan is not available')


class Admin:
    def __init__(self):
        self.users = []

    def create_acc(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def Bank_total_balance(self):
        total_balance = 0
        for user in self.users:
            total_balance+= user.balance
        return f"Total available balance in the bank: ${total_balance}"

    def check_total_loan(self):
        total_loan = 0
        for user in self.users:
            total_loan+= user.loan_amount
        return f"Total loan in the bank: ${total_loan}"

    def loan_activation(self, enable):
        for user in self.users:
            if enable == True:
                user.loan_eligibility  = True
            else:
                user.loan_eligibility  = False  


# Example usage:

admin = Admin()
user1 = admin.create_acc("Alice")
user2 = admin.create_acc("Bob")

user1.deposit(800)
user2.deposit(500)

user1.transfer(user2, 300)
user1.withdraw(200)

print(user1.check_balance())
print(user2.check_balance())

print(user1.transaction_history())
print(user2.transaction_history())

user1.take_loan()
print(user1.check_balance())

print(admin.Bank_total_balance())
print(admin.check_total_loan())

admin.loan_activation(False)
user1.take_loan()
print(user1.check_balance())


