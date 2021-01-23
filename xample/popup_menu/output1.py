'''
code file:
date:
commants:
    tkauto generated

'''

from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets
from tkinter.font import Font
    # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)
# import os, sys
# import webbrowser
import pyperclip
# from tkinter.filedialog import askopenfilename
# from tkinter import messagebox
# from functools import partial # action_w_arg = partial(self.proc_btns, n)

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
        # style.configure("TButton", width=10)

        root.geometry("300x300")

        self.txt = Text(self)
        self.txt.grid(row=1, column=1)

        efont = Font(family="Ubuntu Mono", size=14)
        self.txt.configure(font=efont)
        self.txt.config(wrap = "word", # wrap = NONE
               undo = True, # Tk 8.4
               width = 80,
               tabs = (efont.measure(' ' * 4),))
        self.txt.focus()

        self.txt.insert("1.0", "right click to Copy & Paste ...")

        self.popup_menu = Menu(self, tearoff = 0)
        self.popup_menu.add_command(label = "Copy",
                                    command = lambda:self.clipbrd(1))
        self.popup_menu.add_command(label = "Paste",
                                    command = lambda:self.clipbrd(2))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "say bye", command = exit)
        self.txt.bind("<Button-3>",self.do_popup)

    def do_popup(self,event):
        try:
            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)
        finally:
            self.popup_menu.grab_release()


    def clipbrd(self,n):
        if n == 1:  # Copy
            pyperclip.copy(self.txt.selection_get())
        else:
            # n == 2:  # Paste
            inx = self.txt.index(INSERT)
            self.txt.insert(inx, pyperclip.paste())

root = ThemedTk(theme="radiance")

root.title("popmenu demo")
root.resizable(0,0) # no resize & removes maximize button
app = Application(root)
app.mainloop()
