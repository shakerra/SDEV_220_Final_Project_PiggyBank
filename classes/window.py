from tkinter import *

class Window():
    #user's first name
    f_name = ''

    #user's last name
    l_name = ''

    def __init__(self, root, title, geometry, message, step):
        self.root = root
        self.step = step
        self.root.title(title)
        self.root.geometry(geometry)
        Label(self.root, text = message).pack()
        self.welcome_frame = LabelFrame(root, text='Welcome To BanKids', padx=5, pady=5)
        self.welcome_frame.pack()
        #Get user input for name
        self.name_input = Entry(self.welcome_frame)
        #Pack input
        self.name_input.pack()
        #frame
        self.root.mainloop()

    #increment step
    def inc_step(self):
        self.step += 1
        #Button to get user input
        name_input_button = Button(self.welcome_frame, text='Submit', command = self.get_user_input)
        name_input_button.pack()
        return

    #Store user input to name variable
    def get_user_input(self):
        print('User Input')
        if(self.name_input.get() != ''):
            self.f_name = self.name_input.get()
            print(f"Name: {self.f_name}")
            #self.inc_step()
            print(self.step)
            return
            
        else:
            print('Please enter your name')
            return
    
    def change_screen(self):
        if(self.f_name):
            self.name_input.pack_forget()
            return