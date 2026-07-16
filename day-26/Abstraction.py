from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")
    def viewhistroy(self):
        print("You can your transection")
    def userinfo(self):
        print("You can see your details")
    def transactions(self):
        print("You can transfer money through netbanking")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self):
        print("you can deposit - CA")
    def withdraw(self):
        print("You can withdraw - CA")

class SavingAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SA")
    def withdraw(self):
        print("You can withdraw - SA")

class FixedDeposit(BankAccount):
    def deposit(self):
        print("you can deposit - FD")
    def withdraw(self):
        print("You can withdraw - FD")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SAA")
    def withdraw(self):
        print("You can withdraw - SAA")
        

class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("you can deposit - ZBA")
    def withdraw(self):
        print("You can withdraw - ZBA")

chanu = ZeroBalanceAccount()
chanu.deposit()
chanu.withdraw()
chanu.checkbalance()
chanu.viewhistroy()
chanu.userinfo()
chanu.transactions()

pandu = SalaryAccount()
pandu.deposit()
pandu.withdraw()
pandu.checkbalance()
pandu.viewhistroy()
pandu.userinfo()
pandu.transactions()

kumar = ZeroBalanceAccount()
kumar.deposit()
kumar.withdraw()
kumar.checkbalance()
kumar.viewhistroy()
kumar.userinfo()
kumar.transactions()
        
        
        
