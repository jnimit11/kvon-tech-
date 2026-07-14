class bankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"rs{amount} deposited successfully.")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"rs{amount} withdrawn succesfully!")
        else:
            print("Insufficent balance!!")
            
    def checkBalance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"current balance: {self.balance}")    
        
account = bankAccount("Nimit", 150000)

account.checkBalance()
account.deposit(4000)
account.withdraw(30000)
account.checkBalance()