#account class - temporary
class Account:
    def __init__(self, balance, type, bank):
        self.balance = balance
        self.bank = bank
        self.type = type
    
    #set balance of account, used for both withdrawals and deposits
    #deposit = 0
    #withdraw = 1
    def set_balance(self, e, amount):
        #if 0, deposit : else withdraw
        if(e == 0):
            self.balance += amount
            print('-------')
            print("You've completed a deposit")
            print(f'Your new balance is {self.balance}')
        else:
            self.balance -= amount
            print('-------')
            print("You've completed a withdrawal")
            print(f'Your new balance is {self.balance}')
        #return balance after transaction
        return self.get_balance()

    #get current balance
    def get_balance(self):
        return self.balance