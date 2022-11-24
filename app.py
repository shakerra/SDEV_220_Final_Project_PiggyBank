#import tkinter modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#import classes from relative files
from classes.user import User
from classes.account import Account

#styling variables
#colors
c_dark  = '#121212'
c_purp  = '#3700B3'
c_error = '#CF6679'
c_black = '#000000'
c_white = '#FFFFFF'

#global vars
#concat first and last name
name = ''

#bank of choice
bank = {}

#current user, object derived from "User" class in /classes/user.py and initialized in BankPage class
current_user = {}

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (WelcomePage, BankPage, YourAccountPage):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            print(current_user)

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame('WelcomePage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if(current_user != {}):
            print(current_user)
        else:
            print('No value assigned to current user yet')
        frame.tkraise()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def concat_name():
            f_name = f_name_input.get()
            l_name = l_name_input.get()
            if(f_name != ''):
                if(l_name != ''):
                    name = f"{f_name} {l_name}"
                    controller.show_frame('BankPage')
                else:
                    messagebox.showwarning(title = 'Nope', message = 'Please enter your last name')
            else:
                messagebox.showwarning(title = 'Nope', message = 'Please enter your first name')
            return

        label = tk.Label(self, text = 'Welcome To BanKids. Enter your name to get started!')
        label.pack(side = 'top', fill = 'x', pady = 10)

        #input boxes for first and last name
        f_name_label = tk.Label(self, text = 'First name')
        f_name_label.pack()

        f_name_input = tk.Entry(self)
        f_name_input.pack(pady = 10)

        #get user input for last name
        l_name_label = tk.Label(self, text = 'Last name')
        l_name_label.pack()

        l_name_input = tk.Entry(self)
        l_name_input.pack(pady = 10)

        #Button to fire concat_name function, store name for user and move to BankPage screen
        button = tk.Button(self, text = 'Submit', command = concat_name)
        button.pack(pady = 10)

#Select A Bank Account
#This frame will create the user and account objects
class BankPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #if user already exists, continue. Else, create new user with vars "name" and "bank"
        def sel_bank():
            selected_bank = select_bank_box.get()
            if(selected_bank):
                #if user selected a bank, continue, if not, prompt user to select
                #assign user input to global 'bank' variable
                bank = selected_bank
                #create instance of 'Account' class with a starting balance of 500.00
                checking_account = Account(float(500.00), 'checking', bank)
                global current_user
                current_user = User(name, checking_account)

                print(selected_bank)
                controller.show_frame('YourAccountPage')
            else:
                messagebox.showwarning(title = 'Error', message = 'Please select a bank to continue')

        #-----ERROR-----#
        #not concatenating but showing up in print statement
        welcome_msg = f'Hello {name}, pick a bank below to start your new account!'
        #-----ERROR-----#

        label = tk.Label(self, text = welcome_msg)
        label.pack(side = 'top', fill = 'x', pady = 10)

        #get user input for bank selection with dropdown
        choices = ['Chase', 'Fifth Third', 'First Midwest']
        select_bank_box = ttk.Combobox(self, values = choices)
        select_bank_box.pack()

        button = tk.Button(self, text = 'Select', command = sel_bank)
        button.pack(pady = 10)

class YourAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def transact(transaction):
            #amt = withdrawal_input.get()
            msg = ''
            if(transaction == 2):
                #msg = current_user.checking_account.get_balance()
                #tk.messagebox.showinfo(title = 'Your balance', message = msg)
                if(hasattr(current_user, 'account')):
                    print(current_user.account.get_balance())
                else:
                    print('Current user does not have attribute account')
                print('User selected balance check')
            #if user selected withdraw or depost
            else:
                if(hasattr(current_user, 'account')):
                    msg = current_user.account.set_balance(transaction, 20.50)
                    tk.messagebox.showinfo(title = 'You Made A Transaction!', message = f'Your new balance is {msg}')
                    print(current_user.account.get_balance())
                else:
                    print('Current user does not have attribute account')
                print('User selected something else')

        label = tk.Label(self, text = f'Hello {name}, what would you like to do with your account?')
        label.pack(side = 'top', fill = 'x', pady = 10)

        #withdraw button
        w_button = tk.Button(self, bg = '#3F51B5', foreground = '#ffffff', text = 'Withdraw', command = lambda: transact(1))
        w_button.pack()

        #deposit button
        d_button = tk.Button(self, pady = '10', text = 'Depost', command = lambda: transact(0))
        d_button.pack()

        #check balance button
        cb_button = tk.Button(self, pady = '10', text = 'Check Balance', command = lambda: transact(2))
        cb_button.pack()

        #label and input fields to enter withdrawal and deposit amounts
        withdrawal_label = tk.Label(self, text = f'How much would you like to withdraw from your account?')
        withdrawal_label.pack()
        withdrawal_input = tk.Entry(self)
        withdrawal_input.pack(pady = 10)
        withdrawal_confirm = tk.Button(self, pady = 10, text = 'Submit', command = lambda: transact(0))
        withdrawal_confirm.pack()

        deposit_label = tk.Label(self, text = f'How much would you like to deposit to your account?')
        deposit_label.pack()
        deposit_input = tk.Entry(self)
        deposit_input.pack(pady = 10)
        deposit_confirm = tk.Button(self, pady = 10, text = 'Submit', command = lambda: transact(1))
        deposit_confirm.pack()

if __name__ == '__main__':
    app = App()
    app.geometry('600x600')
    app.title('BanKids 💵')
    app.mainloop()