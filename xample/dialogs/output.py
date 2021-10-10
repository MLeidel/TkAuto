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

        # customize widget style when using ttk...
        style = Style()
        style.configure("TButton", width=10)

        # root.geometry("400x250")  # handled by template "save_location" code

        self.vlbl_text = StringVar()
        lbl_text = Label(self, padding='1i', textvariable=self.vlbl_text)
        lbl_text.grid(row=1, column=1)
        self.vlbl_text.set('Hit Ctrl-e to change this label')

        root.bind("<Control-e>", self.eventHandler)
        
        # from tkinter import simpledialog
        # tkinter.simpledialog.askfloat(title, prompt, **kw)
        # tkinter.simpledialog.askinteger(title, prompt, **kw)
        # tkinter.simpledialog.askstring(title, prompt, **kw)
        # if answer is not None:
        

    def eventHandler(self, event=None):
        s = simpledialog.askstring("Demo simpledialog",
                                "Enter a STRING for the label")
        if s is not None:
            self.vlbl_text.set(s)

    # def eventHandler(self):
    #     pass

#

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
def save_location(e=None):
    ''' executes at WM_DELETE_WINDOW event '''
    with open("winfo", "w") as fout:
        fout.write(root.geometry())
    root.destroy()

# ttkthemes
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="default")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
if os.path.isfile("winfo"):
    with open("winfo") as f:
        lcoor = f.read()
    root.geometry(lcoor.strip())
else:
    root.geometry("350x200") # WxH+left+top


root.title("simpledialog demo")
root.protocol("WM_DELETE_WINDOW", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO
# Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
# root.resizable(w, h) # no resize & removes maximize button
# root.minsize(w, h)  # width, height
# root.maxsize(w, h)
# root.overrideredirect(True) # removed window decorations
# root.iconphoto(False, PhotoImage(file='icon.png'))
# root.attributes("-topmost", True)  # Keep on top of other windows
app = Application(root)
app.mainloop()
