'''
code file: outtest.py
date:
commants:
    test for demo2
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os, sys
from tkinter.font import Font
# import sys
# import webbrowser
# import pyperclip
# from tkinter import filedialog
# from tkinter import messagebox
from tkinter import simpledialog
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

        # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)

        # customize widget style when using ttk...
        # style = Style()
        # style.configure("TButton", width=10) # global
        # style.configure("my.TButton", width=10) # 'style' option

        ''' ONLY OPTIONS FOR 'grid' FUNCTIONS:
                column  row
                columnspan  rowspan
                ipadx and ipady
                padx and pady
                sticky="nsew"
        -------------------------------------------------------- '''

        root.geometry("500x300")

        notebk = Notebook(self)
        tab1 = Frame(notebk, width=488, height=260)  # W & H are necessary
        tab2 = Frame(notebk, width=488, height=260)
        tab3 = Frame(notebk, width=488, height=260)
        notebk.add(tab1, text='Message Widget')
        notebk.add(tab2, text='Other Widgets')
        notebk.add(tab3, text='Nothing Yet')
        notebk.grid(row=1, column=1)

        msgtext = '''
Hello, this is a 'Message' widget.
tkinter provides this for multi-line
read-only text display. Note the
Message widget does not seem to be
supported by ttkbootstrap.

The Notebook widget is quite simple.
TkbAuto just creates a 3 tab notebook.
It is obvious just by looking at the
generated code what can be done to modify it.
        '''
        msg = Message(tab1, text=msgtext, width=360)
        msg.grid(row=1, column=1, sticky='nwew', padx=20, pady=20)

        btn1 = Button(tab2, text='Open Toplevel', command=self.create_toplevel)
        btn1.grid(row=1, column=1, pady=10)

        self.vspn = StringVar(value=0)
        spn = Spinbox(tab2, textvariable=self.vspn,
                      from_=0, to=10,
                      command=self.procspin)
        spn.grid(row=2, column=1, pady=10)

        btn2 = Button(tab2, text='Open Simple Dialog', command=self.open_dialog)
        btn2.grid(row=3, column=1, pady=5)



    def create_toplevel(self):
        t = Toplevel(self)
        t.wm_title("Toplevel")
        t.geometry("200x100") # WxH+left+top
        l = Label(t, text="This is a Toplevel Window")
        l.grid(row=0, column=0, padx=2, pady=20)
        tvbtn = Button(t, text=" Exit ", command=t.destroy)
        tvbtn.grid(row=2, column=0, sticky='w', padx=2, pady=4)

        # # from tkinter import simpledialog
        # simpledialog.askfloat(title, prompt)
        # simpledialog.askinteger(title, prompt)
        # simpledialog.askstring(title, prompt)
        # if answer is not None:

    def open_dialog(self):
        ''' Demo a simpledialog '''
        s = simpledialog.askstring("Demo", "Enter something")
        print(s)

    def procspin(self):
        ''' The Spinbox value changed '''
        print(self.vspn.get())

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
