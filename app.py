import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#global vars
#concat first and last name
name = ''

#bank of choice
bank = ''

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

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame('WelcomePage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
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
                    print(name)
                    controller.show_frame('BankPage')
                else:
                    messagebox.showwarning(title = 'Nope', message = 'Please enter your last name')
            else:
                messagebox.showwarning(title = 'Nope', message = 'Please enter your first name')
            return

        label = tk.Label(self, text = 'Welcome To BanKids. Enter your name to get started!')
        label.pack(side = 'top', fill = 'x', pady = 10)

        f_name_label = tk.Label(self, text = 'First name')
        f_name_label.pack()

        f_name_input = tk.Entry(self)
        f_name_input.pack()

        #get user input for last name
        l_name_label = tk.Label(self, text = 'Last name')
        l_name_label.pack()

        l_name_input = tk.Entry(self)
        l_name_input.pack()

        #Button to fire concat_name function, store name for user and move to BankPage screen
        button = tk.Button(self, text = 'Submit', command = concat_name)
        button.pack()

#Select A Bank Account
class BankPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #if user already exists, continue. Else, create new user with vars "name" and "bank"
        #def check_current_user():

        def sel_bank():
            #if user selected a bank, continue, if not, prompt user
            selected_bank = select_bank_box.get()
            print(selected_bank)
            if(selected_bank):
                bank = selected_bank
                print(bank)
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
        button.pack()

class YourAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #placeholder value, replace when account and user classes are worked in
        self.balance = float(500)

        #show balance
        def check_balance():
            tk.messagebox.showinfo(title = 'Account Balance', message = f'Your account balance is {self.balance}')

        #withdraw
        def withdraw():
            tk.messagebox.showinfo(title = 'Withdraw', message = 'How much would you like to withdraw?')

        #deposit
        def deposit():
            tk.messagebox.showinfo(title = 'Depost', message = f'How much would you like to deposit?')

        label = tk.Label(self, text = f'Hello {name}, what would you like to do with your account?')
        label.pack(side = 'top', fill = 'x', pady = 10)

        #withdraw button
        w_button = tk.Button(self, text = 'Withdraw', command = withdraw).pack()

        #deposit button
        d_button = tk.Button(self, text = 'Depost', command = deposit).pack()

        #check balance button
        cb_button = tk.Button(self, text = 'Check Balance', command = check_balance).pack()

if __name__ == "__main__":
    app = App()
    app.geometry('600x600')
    app.title('BanKids 💵')
    app.mainloop()