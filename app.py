import tkinter as tk
from classes.account import Account, Checking_Account

window = tk.Tk()
#styling
window.geometry("650x650")

name = tk.Entry(window)
name.pack()

greeting = tk.Label(text='Hello World')
greeting.pack()

def get_input():
    username = name.get()
    print(username)

def print_shalom():
    print('Shalom')

get_input_button = tk.Button(window, text = 'Submit', command = print_shalom())

get_input_button.pack()
greeting.pack()

window.mainloop()