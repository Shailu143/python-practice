class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted for the amount of ${amount:.2f}: {error}")

    def transfer(self,amount,account):
        try:
            print("\n*********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer from the account '{self.name}' to the account '{account.name}' complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer from the account '{self.name}' to the account '{account.name}' interrupted for the amount of ${amount:.2f}. ❌ {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit compelte.")
        self.getBalance()
        
class SaveingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount,acctName)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - amount + self.fee
            print("\nWitndraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
        