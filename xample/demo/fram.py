'''
code file:
date:
commants:
    tkauto generated

'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os
# from tkinter.font import Font
    # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)
# import sys
# import webbrowser
# import pyperclip
# from tkinter import filedialog
# from tkinter import messagebox
# from tkinter import simpledialog
# from functools import partial # action_w_arg = partial(self.proc_btns, n)
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        # customize widget style when using ttk...
        # style = Style()
        # style.configure("TButton", width=10) # global
        # style.configure("my.TButton", width=10) # 'style' option

        ''' OPTIONS FOR 'grid' FUNCTIONS:
                column and row
                columnspan and rowspan
                ipadx and ipady
                padx and pady
                sticky '''

        self.vrad1 = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad1 = Radiobutton(self, variable=self.vrad1, value='radio btn 1', text='radio btn 1')
        rad1.grid(row=1, column=1)

        self.vrad2 = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad2 = Radiobutton(self, variable=self.vrad2, value='radio btn 2', text='radio btn 2')
        rad2.grid(row=2, column=1)

        self.vrad3 = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad3 = Radiobutton(self, variable=self.vrad3, value='radio btn 3', text='radio btn 3')
        rad3.grid(row=3, column=1)

        self.vchk1 = IntVar()
        chk1 = Checkbutton(self, variable=self.vchk1, text='checkbox 1')
        chk1.grid(row=1, column=2)

        self.vchk2 = IntVar()
        chk2 = Checkbutton(self, variable=self.vchk2, text='checkbox 2')
        chk2.grid(row=2, column=2)

        optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
        self.vopts = StringVar()
        self.vopts.set(optionlist[0])
        opts = OptionMenu(self, self.vopts, *optionlist)
        opts.grid(row=3, column=2)

        lbl = Label(self, text='below is a Label')
        lbl.grid(row=4, column=1, columnspan=2, sticky='ew')

        self.vtbx = StringVar()
        # self.vtbx.trace("w", self.eventHandler)
        tbx = Entry(self, textvariable=self.vtbx)
        tbx.grid(row=5, column=1, columnspan=2, sticky='ew')

        self.vcombo = StringVar()
        combo = Combobox(self, textvariable=self.vcombo)
        combo['values'] = ('value1', 'value2', 'value3')
        # COMBO.bind('<<ComboboxSelected>>', self.ONCOMBOSELECT)
        combo.current(0)
        combo.grid(row=6, column=1, columnspan=2, sticky='ew')

        self.vsc = DoubleVar()
        sc = Scale(self, variable=self.vsc)
        sc.grid(row=7, column=1, columnspan=2, sticky='ew')
        # str(self.var.get())

        msg = Message(self, text='blah blah')
        msg.grid(row=8, column=1, columnspan=2, sticky='nsew')


    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass

#

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
# def save_location(e=None):
#     ''' executes at WM_DELETE_WINDOW event - see below '''
#     with open("winfo", "w") as fout:
#         fout.write(root.geometry())
#     root.destroy()

# ttkthemes
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="scidmint")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
# if os.path.isfile("winfo"):
#     with open("winfo") as f:
#         lcoor = f.read()
#     root.geometry(lcoor.strip())
# else:
#     root.geometry("400x300") # WxH+left+top


root.title("Tkinter Demo")
# root.protocol("WM_DELETE_WINDOW", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO
# Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
# root.resizable(0, 0) # no resize & removes maximize button
# root.minsize(w, h)  # width, height
# root.maxsize(w, h)
# root.overrideredirect(True) # removed window decorations
# root.iconphoto(False, PhotoImage(file='icon.png'))
# root.attributes("-topmost", True)  # Keep on top of other windows
app = Application(root)
app.mainloop()
