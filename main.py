# basic user class
class User:
    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

# account class
class Account:
    balance = 0

    def __init__(self, balance):
        self.balance = 500.00
        print("Your account has been created")