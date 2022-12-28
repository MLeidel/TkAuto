'''
code file:
date:
comments:
    tkauto generated

'''
from tkinter import *
import ttkbootstrap as bs
from ttkbootstrap.constants import *
import os, sys
from tkinter.font import Font
# from tkcalendar import *
# from time import gmtime, strftime
# import sys
# import webbrowser
# import pyperclip
# from tkinter import filedialog
# from tkinter import messagebox
from tkinter import simpledialog
# from functools import partial # action_w_arg = partial(self.proc_btns, n)

class Application(bs.Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        bs.Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)

        ''' ONLY OPTIONS FOR 'grid' FUNCTIONS:
                column  row
                columnspan  rowspan
                ipadx and ipady
                padx and pady
                sticky="nsew"
        -------------------------------------------------------- '''

        notebk = bs.Notebook(self)
        tab1 = bs.Frame(notebk, width=99, height=99)  # need W & H
        tab2 = bs.Frame(notebk, width=99, height=99)
        tab3 = bs.Frame(notebk, width=99, height=99)
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
TkAuto just creates a 3 tab notebook.
It is obvious just by looking at the
generated code what can be done to modify it.
        '''
        msg = Message(tab1, text=msgtext, width=360)
        msg.grid(row=1, column=1, sticky='nwew', padx=20, pady=20)

        btn1 = bs.Button(tab2, text='Open Toplevel',
                         command=self.create_toplevel)
        btn1.grid(row=1, column=1, pady=10)

        self.vspn = bs.StringVar(value=0)
        spn = bs.Spinbox(tab2, textvariable=self.vspn,
                         from_=0, to=10,
                         command=self.procspin)
        spn.grid(row=2, column=1, pady=10)

        btn2 = bs.Button(tab2, text='Open Simple Dialog', command=self.open_dialog)
        btn2.grid(row=3, column=1, pady=5)

        self.vspn = bs.StringVar(value=0)
        spn = bs.Spinbox(tab2, textvariable=self.vspn, from_=0, to=10)
        spn.grid(row=2, column=1)

    def create_toplevel(self):
        t = bs.Toplevel(self)
        t.wm_title("Toplevel")
        t.geometry("200x100") # WxH+left+top
        l = Label(t, text="This is a Toplevel Window")
        l.grid(row=0, column=0, padx=2, pady=20)
        tvbtn = Button(t, text=" Exit ", command=t.destroy)
        tvbtn.grid(row=2, column=0, sticky='w', padx=2, pady=4)

    def open_dialog(self):
        ''' Demo a simpledialog '''
        s = simpledialog.askstring("Demo", "Enter something")
        print(s)

    def procspin(self):
        ''' The Spinbox value changed '''
        print(self.vspn.get())

    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass

#

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
# def save_location(e=None):
#     ''' executes at WM_DELETE_WINDOW event - see below '''
#     with open("winfo", "w") as fout:
#         fout.write(app.geometry())
#     app.destroy()

app = bs.Window("tkbauto template", "solar")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
# if os.path.isfile("winfo"):
#     with open("winfo") as f:
#         lcoor = f.read()
#     app.geometry(lcoor.strip())
# else:
#     app.geometry("400x300") # WxH+left+top


# app.protocol("WM_DELETE_WINDOW", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO
bs.Sizegrip(app).place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
# app.resizable(0, 0) # no resize & removes maximize button
# app.minsize(w, h)  # width, height
# app.maxsize(w, h)
# app.overrideredirect(True) # removed window decorations
# app.iconphoto(False, PhotoImage(file='icon.png'))
# app.attributes("-topmost", True)  # Keep on top of other windows

Application(app)

app.mainloop()
