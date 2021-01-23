'''
code file:
date:
commants:
    tkauto generated

'''

from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets
# from tkinter.font import Font
    # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)
# import os, sys
# import webbrowser
# import pyperclip
# from tkinter import filedialog
from tkinter import messagebox
# from functools import partial # action_w_arg = partial(self.proc_btns, n)

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''

        # only difference from output1.py ...
        self.columnconfigure(1, weight=1, pad=85)
        self.rowconfigure(1, weight=1, pad=10)
        self.rowconfigure(2, weight=1, pad=10)
        self.rowconfigure(3, weight=1, pad=10)
        self.rowconfigure(4, weight=1, pad=10)
        self.rowconfigure(5, weight=1, pad=10)

        # customize widget style when using ttk...
        # style = Style()
        # style.configure("TButton", width=10)

        self.cv1 = IntVar()
        ck1 = Checkbutton(self, variable=self.cv1, text='ketchup', width=12)
        ck1.grid(row=1, column=1)

        self.cv2 = IntVar()
        ck2 = Checkbutton(self, variable=self.cv2, text='mustard', width=12)
        ck2.grid(row=2, column=1)

        self.cv3 = IntVar()
        ck2 = Checkbutton(self, variable=self.cv3, text='pickles', width=12)
        ck2.grid(row=3, column=1)

        lbl = Label(self, text='Quantity')
        lbl.grid(row=4, column=1)

        self.svar = StringVar()
        spn = Spinbox(self, textvariable=self.svar,
                      from_=1, to=9, width=2, font='Helvetica 12')
        spn.grid(row=5, column=1)

        btn = Button(self, text='Order', command=self.on_btn_clicked)
        btn.grid(row=6, column=1, pady=8)


    def on_btn_clicked(self):
        ''' action for button clicked '''
        msg = ""
        ketchup = self.cv1.get()  # checkbox var is 1 (checked)
        mustard = self.cv2.get()  #     or 0 (not checked)
        pickles = self.cv3.get()
        quan = self.svar.get()
        print(ketchup)
        print(mustard)
        print(pickles)
        print(quan)
        if ketchup:  # in Python 1 is true, 0 is false
            msg += "ketchup\n"
        if mustard:
            msg += "mustard\n"
        if pickles:
            msg += "pickles\n"
        msg += "quantity: " + str(quan)
        messagebox.showinfo("Order",msg)


# root = Tk()
# Requires ttkthemes module
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="default")


root.title("Demo")
app = Application(root)
app.mainloop()
