# Account class
class Account:
    def __init__(self, balance, options, user):
        self.balance = balance
        self.options = options
        self.user = user

    options = ['withdrawal', 'deposit', 'check_balance'];
    
    #method to withdraw
    def withdraw(self):
        wd_amount = float(input('How Much Money Would You Like To Withdraw? $'))
        if(self.balance < wd_amount):
            wd_amount = float(input('You do not have enough in your account for that transaction. How Much Money Would You Like To Withdraw? $'))
        else:
            new_bal = self.balance + wd_amount
            message = f"You've withdrawn {wd_amount} from your account, bring you to a new balance of {new_bal}"
            return message

    #method to deposit
    def set_balance(self):
        deposit_amount = float(input('How Much Would You Like To Deposit? $'))
        new_bal = self.balance + deposit_amount
        message = f"You've deposited {deposit_amount} into your account, bringing you to a new balance of {new_bal}"
        return message

    #method to check balance
    def get_balance(self):
        return self.balance

#checking account
class Checking_Account(Account):
    def __init__(self, balance, options, user):
        super().__init__(balance, options, user)

class Saving_Account(Account):
    def __init__(self, balance, options, user):
        super().__init__(balance, options, user)

#User class
#class User:
#    def __init__(self, first_name, last_name, accounts, age):
#        self.name = name
#        self.accounts = accounts
#        self.age = age

    #function to format name
#    def form_name():
#        name = first_name + last_name
#        return name;

    #function to choose account
#    def select_account():
        #get user input for first and last nameaccount
        #loop through static list of accounts and check for match with user input