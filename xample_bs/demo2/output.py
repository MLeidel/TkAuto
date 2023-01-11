'''
code file:
date:
comments:
    tkauto generated
'''
import os, sys
from tkinter.font import Font
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import Message
# from tkinter import Listbox
# from tkinter import filedialog
# from tkinter import simpledialog
# from tkdate import date_pick
# import webbrowser
# from functools import partial # action_w_arg = partial(self.proc_btns, n)
# from time import gmtime, strftime

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        self.columnconfigure(1, weight=1, pad=100)
        self.rowconfigure(1, weight=1, pad=20)

        # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)

        ''' ONLY OPTIONS FOR 'grid' FUNCTIONS:
                column  row
                columnspan  rowspan
                ipadx and ipady
                padx and pady
                sticky="nsew"
        -------------------------------------------------------- '''

        notebk = Notebook(self)
        tab1 = Frame(notebk, width=99, height=99)  # need W & H
        tab2 = Frame(notebk, width=99, height=99)
        tab3 = Frame(notebk, width=99, height=99)
        notebk.add(tab1, text='tab 1')
        notebk.add(tab2, text='tab 2')
        notebk.add(tab3, text='tab 3')
        notebk.grid(row=1, column=1)

        msg = Message(tab1, text='')
        msg.grid(row=1, column=1, sticky='nwew')

        btn1 = Button(tab2, text='Open Toplevel', command=self.create_toplevel)
        btn1.grid(row=1, column=1)

        
    # def create_window(self):
    #     t = Toplevel(self)
    #     t.wm_title("Toplevel")
    #     t.geometry("200x100") # WxH+left+top
    #     l = Label(t, text="This is a Toplevel Window")
    #     l.grid(row=0, column=0, padx=2, pady=20)
    #     tvbtn = Button(t, text=" Exit ", command=t.destroy)
    #     tvbtn.grid(row=2, column=0, sticky='w', padx=2, pady=4)
    

        self.vspn = StringVar(value=0)
        spn = Spinbox(tab2, textvariable=self.vspn, from_=0, to=10)
        spn.grid(row=2, column=1)

        
        # # from tkinter import simpledialog
        # simpledialog.askfloat(title, prompt)
        # simpledialog.askinteger(title, prompt)
        # simpledialog.askstring(title, prompt)
        # if answer is not None:
        

        btn2 = Button(tab2, text='Open Simple Dialog', command=self.open_dialog)
        btn2.grid(row=3, column=1)

    def create_toplevel(self):
        ''' docstring '''

    def open_dialog(self):
        ''' docstring '''


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

root = Window("tkbauto template", "superhero")

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


# root.protocol("WM_DELETE_WINDOW", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO
Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
# root.resizable(0, 0) # no resize & removes maximize button
# root.minsize(w, h)  # width, height
# root.maxsize(w, h)
# root.overrideredirect(True) # removed window decorations
# root.iconphoto(False, PhotoImage(file='icon.png'))
# root.attributes("-topmost", True)  # Keep on top of other windows

Application(root)

root.mainloop()
