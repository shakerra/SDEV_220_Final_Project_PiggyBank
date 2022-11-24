#user class
class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def printInfo(self):
        print('----------------')
        print(f'New User Created')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Account: {self.account}')