# basic user class
class User:
    def __init__(self, firstname, lastname, age, account):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.account = account

# account class


class Account:
    balance = 0

    def __init__(self, balance):
        balance = 500.00
        print("Your account has been created")