from enum import Enum, auto

class WalletType(Enum):
    KZT = auto()
    USD = auto()
    RUB = auto()

class BankAccount:
    name: str
    surname: str
    account: WalletType
    balance: int

    def __init__(self, name, surname, account, balance = 0):
        self.name = name
        self.surname = surname
        self.account = account
        self.balance = balance
    
    def addToBankAccount(self, amount: int):
        self.balance += amount

    def substractFromBankAccount(self, amount: int):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds!!!")

    def moneyConversion(self, newAccountType: WalletType):
        self.account = newAccountType

    def getBalance(self):
        return self.balance
    
    def __repr__(self):
        return f'{name} {surname} {account}'

accounts = []

while True:
    command = int(input("Choose:\n1. Create New Account\n2. Get Account\n0. Exit\n"))
    match command:
        case 1:
            name, surname, account_type = input("Enter: Name Surname KZT/RUB/USD\n").split()
            match account_type:
                case 'KZT':
                    account = WalletType.KZT
                case 'RUB':
                    account = WalletType.RUB
                case 'USD':
                    account = WalletType.USD
                case _:
                    print("Invalid account type!")
                    break
            new_account = BankAccount(name, surname, account)
            accounts.append(new_account)
        case 2:
            name, surname = input("Enter: Name Surname\n").split()
            for account in accounts:
                if account.name == name and account.surname == surname:
                    print(account)
        case 0:
            break
        case _:
            print("Invalid command!")

print(accounts)