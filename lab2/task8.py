class BankAccount:
    balance: float

    def __init__(self, balance):
        self.balance = balance

    def addMoney(self, amount: int):
        self.balance += amount

    def removeMoney(self, amount: int):
        self.balance -= amount

    def changeCurrency(self, isUSD: bool):
        if isUSD:
            print("Your amount in KZT: " + str(self.balance * 470))
        else:
            print("Your amount in USD: " + str(self.balance / 470))
    
    def getBalance(self):
        return self.balance

myAccount = BankAccount(0)
print("Initial balance: " + str(myAccount.getBalance()))
myAccount.addMoney(5000)
print("Balance after addition: " + str(myAccount.getBalance()))
myAccount.removeMoney(3000)
print("Balance after removal: " + str(myAccount.getBalance()))
myAccount.changeCurrency(True)
myAccount.changeCurrency(False)