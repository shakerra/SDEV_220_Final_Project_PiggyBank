#import tkinter modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

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
        for F in (WelcomePage, BankPage, YourAccountPage, AddFeatures, Flashcards, CompoundInterest):
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
            amt = 0
            msg = ''
            if(transaction == 2):
                #msg = current_user.checking_account.get_balance()
                #tk.messagebox.showinfo(title = 'Your balance', message = msg)
                if(hasattr(current_user, 'account')):
                    msg = current_user.account.get_balance()
                    tk.messagebox.showinfo(title = 'Check Balance', message = f'Your balance is {msg}')
                else:
                    print('Current user does not have attribute account')
                print('User selected balance check')
            #if user selected withdraw or deposit
            else:
                #check to see if user has entered value for withdrawal_input variable
                if(withdrawal_input.get()):
                    amt = float(withdrawal_input.get())
                    print(amt)
                    print('Got user value for amount')
                else:
                    print('Error with user entered amount')
                #check to see if user object has attribute 'account'
                if(hasattr(current_user, 'account')):
                    msg = current_user.account.set_balance(transaction, amt)
                    tk.messagebox.showinfo(title = 'You Made A Transaction!', message = f'Your new balance is {msg}')
                    print(current_user.account.get_balance())
                else:
                    print('Current user does not have attribute account')
                print('User selected something else')

        #header label
        header_label = tk.Label(self, text=f"Would you like to make a transaction {name}?")
        header_label.pack(pady=10)

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

        label = tk.Label(self, text = f'Go To Additional Learning Activities')
        label.pack(side = 'top', fill = 'x', pady=25)

        activies_button = tk.Button(self, text = 'Learning Activites',
                                    command = lambda: controller.show_frame("AddFeatures"))
        activies_button.pack()

         
#Additional Learning Features
class AddFeatures(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        label = tk.Label(self, text="Learning Activities", font=("Helvetica", 20))
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="Please Select An Activity")
        label2.pack(side="top", fill="x", pady=10)

        #open flashcard game
        fc_button = tk.Button(self, text="Financial Literacy Flashcards", command= lambda: controller.show_frame("Flashcards"))
        fc_button.pack()

        #open compound interest simulator
        CompIntb = tk.Button(self, text="Compound Interest Simulator", command= lambda: controller.show_frame("CompoundInterest"))
        CompIntb.pack()

        #return to your account
        returnb = tk.Button(self, text = 'Go Back to Your Account',
                                    command = lambda: controller.show_frame("YourAccountPage"))
        returnb.pack(pady=100)

#Flashcards Feature
class Flashcards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        words = [
            (("Savings"), ("Money set aside for a specific financial goal")),
            (("Budget"), ("A plan that you can make to keep track of your money")),
            (("Loan"), ("Something that is borrowed, usually money, which has to be paid back with interest")),
            (("Deposit"), ("Money placed into an account")),
            (("Interest"), ("The cost of borrowing money, which means you end up paying back more than you borrowed")),
            (("Credit"), ("Money given to you by a bank under the agreement that you will pay it back")),
            (("Investment"), ("Setting aside money for future income or profit to meet long-term goals")),
            (("Stock"), ("An investment that makes the investor a part owner of a company")),
            (("Credit Score"), ("Your report card for how well you handle money and whether you pay your bills on time")),
            (("Bank"), ("A for-profit company that provides saving and checking accounts and other financial services to its customers")),
        ]

        #get a count of our word list
        count = len(words)

        def next():
            #clear the screen 
            answer_label.config(text="")
            my_entry.delete(0, END)

            #create random selection
            global random_word
            random_word = randint(0, count-1)
            #update label with literacy word
            literacy_word.config(text=words[random_word][1])

        def answer():
            ent = my_entry.get()
            if(ent != ''):
                if my_entry.get().capitalize() == words[random_word][0]:
                    answer_label.config(text=f"Correct! {words[random_word][1]} is {words[random_word][0]}", wraplength=500, justify="center")
                else:
                    answer_label.config(text=f"Incorrect! {words[random_word][1]} is not {my_entry.get().capitalize()}", wraplength=500, justify="center")
            else:
                messagebox.showwarning(title = 'Nope', message = 'Please enter an answer')
                       
            
        instructions = Label(self, text="Please match the following words with the correct definition ", font=("Helvetica", 16), wraplength=700, justify="center")
        instructions.pack(pady=10)
        
        word_bank = Label(self, text="Savings, Budget, Loan, Deposit, Interest, Credit, Investment, Stock, Credit score, Bank", font=("Helvetica", 10), justify="center")
        word_bank.pack()
        
        literacy_word = Label(self, text="", font=("Helvetica", 12), wraplength=500, justify="center")
        literacy_word.pack(pady=80)

        my_entry = Entry(self, font=("Helvetica", 18))
        my_entry.pack()

        answer_label = Label(self, text="")
        answer_label.pack()

        #create buttons
        button_frame = Frame(self)
        button_frame.pack()

        answer_button = Button(button_frame, text="Answer", command=answer)
        answer_button.grid(row=0, column=0, padx=20)

        next_button = Button(button_frame, text="Next", command=next)
        next_button.grid(row=0, column=1)

        #run next function when program starts
        next()

        #return to your account
        returnb = tk.Button(self, text = 'Go Back to Learning Activities',
                                    command = lambda: controller.show_frame("AddFeatures"))
        returnb.pack(pady=25)

#Compound Interest Feature
class CompoundInterest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        #return to your account
        returnb = tk.Button(self, text = 'Go Back to Learning Activities',
                                    command = lambda: controller.show_frame("AddFeatures"))
        returnb.pack(pady=25)

if __name__ == '__main__':
    app = App()
    app.geometry('600x600')
    app.title('BanKids 💵')
    app.mainloop()
