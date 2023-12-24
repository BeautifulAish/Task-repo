# OOps - Public, private and protected

def __init__(self):
    self.balance = 0  # Instance variable (you can access it via only object)


def deposit(self.amount)  # Public function
# self.balance = self.balance + amount
self.balance += amount

def_withdrawl (self.amount):
self.balance -= amount

def __show_balance(Self):  # Private
    print("Your Balance", self.balance)

def is_Auth_True_show_bal(self, isAuth)
 If is Auth:
 self.__show_balance()
 else:
 print("You are not Auth")

SBI_KBL = BankAccount()
SBI_KBL.deposit(1000)
SBI_KBL.withdrawl(500)  # Directed protected is not good practice
# jp_chase.__ show balance()

# write code to Auth
SBI_KBL.is_Auth_True(True)
