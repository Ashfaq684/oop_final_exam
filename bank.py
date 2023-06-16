class Bank:
    def __init__(self) -> None:
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True
    
    def create_account(self, email, password):
        account = User(email, password)
        self.accounts.append(account)
        return account
    
    def get_total_balance(self):
        return self.total_balance
    
    def get_total_loan_amount(self):
        return self.total_loan_amount
    
    def enable_loan(self):
        self.loan_enabled = True
    
    def disable_loan(self):
        self.loan_enabled = False
    

class User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount, bank):
        self.balance += amount
        bank.total_balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")
    
    def withdraw(self, amount, bank):
        if bank.total_balance >= amount:
            if self.balance >= amount:
                self.balance -= amount
                bank.total_balance -= amount
                self.transaction_history.append(f"Withdrawal: -{amount}")
            else:
                print("Insufficient funds!")
        else:
            print("Bank is bankrupt")
        
    def check_balance(self):
        return self.balance
    
    def transfer(self, amount, recipient_account, bank):
        if self.balance >= amount:
            self.balance -= amount
            bank.total_balance -= amount
            recipient_account.deposit(amount, bank)
            self.transaction_history.append(f"Transfer: -{amount}")
        else:
            print("Insufficient funds!")
    
    def get_transaction_history(self):
        return self.transaction_history
    
    def take_loan(self, amount, bank):
        if bank.loan_enabled and amount <= (self.balance * 2):
            self.balance += amount
            bank.total_balance -= amount
            bank.total_loan_amount += amount
            self.transaction_history.append(f"Loan: +{amount}")
            print(f"Loan given {amount}")
        else:
            print("Loan not available or exceeds loan limit!")

class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank
    
    def create_account(self, email, password):
        return self.bank.create_account(email, password)
    
    def get_total_balance(self):
        return self.bank.get_total_balance()
    
    def get_total_loan_amount(self):
        return self.bank.get_total_loan_amount()
    
    def enable_loan(self):
        self.bank.enable_loan()
    
    def disable_loan(self):
        self.bank.disable_loan()

bank = Bank()
admin = Admin(bank)

jack = bank.create_account("jack@gmail.com", 3246)
ariana = bank.create_account("ariana@gmail.com", 6242)
robert = admin.create_account("robert@gamil.com", 4262)

jack.deposit(8000, bank)
ariana.deposit(6000, bank)
ariana.withdraw(2000, bank)
jack.transfer(1500, ariana, bank)
jack.take_loan(500, bank)

print("jack's Balance:", jack.check_balance())
print("ariana's Balance:", ariana.check_balance())

total_bank_balance = admin.get_total_balance()
print("Total Bank Balance:", total_bank_balance)

total_loan_amount = admin.get_total_loan_amount()
print("Total Loan Amount:", total_loan_amount)

admin.disable_loan()
jack.take_loan(500, bank)

print("jack's Transaction History:", jack.get_transaction_history())
print("ariana's Transaction History:", ariana.get_transaction_history())