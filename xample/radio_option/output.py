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

        root.geometry("200x200")

        self.radvar = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        r1 = Radiobutton(self, variable=self.radvar, value='Fish', text='Fish')
        r1.grid(row=1, column=1)

        self.radvar = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        r2 = Radiobutton(self, variable=self.radvar, value='Ham', text='Ham')
        r2.grid(row=2, column=1)

        self.radvar = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        r3 = Radiobutton(self, variable=self.radvar, value='Beef', text='Beef')
        r3.grid(row=3, column=1)

        optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
        self.optv = StringVar()
        self.optv.set(optionlist[0])
        optionlist = OptionMenu(self, self.optv, *optionlist)
        optionlist.grid(row=4, column=1)

        btn = Button(self, text='Order', command=self.on_btn_clicked)
        btn.grid(row=5, column=1)

        
        # from tkinter import messagebox
        # messagebox.showerror("Error", "Error message")
        # messagebox.showwarning("Warning","Warning message")
        # messagebox.showinfo("Information","Informative message")
        # messagebox.askokcancel('Message title', 'Message content')
        # messagebox.askretrycancel('Message title', 'Message content')
        #     ok, yes, retry returns TRUE
        #     no, cancel returns FALSE
        

    def on_btn_clicked(self):
        ''' docstring '''



    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass

#

# def save_location():
#     ''' executes at WM_DELETE_WINDOW event '''
#     with open("winfoxy", "w") as fout:
#         fout.write(str(root.winfo_x()) + "\n" + str(root.winfo_y() - 24))
#     root.destroy()

# root = Tk()
# Requires ttkthemes module
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="clam")

# root.geometry("200x120") # WxH+left+top
#   or the following:
#   the following repositions the window from last time '''
# if os.path.isfile("winfoxy"):
#     lcoor = tuple(open("winfoxy", 'r'))  # no relative path for this
#     root.geometry('350x200+%d+%d'%(int(lcoor[0].strip()),int(lcoor[1].strip())))
# else:
#     root.geometry("350x200") # WxH+left+top

root.title("Tkinter Demo")
# Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
# root.resizable(0,0) # no resize & removes maximize button
# root.overrideredirect(True) # removed window decorations
# root.iconphoto(False, PhotoImage(file='icon.png'))
# root.attributes("-topmost", True)  # Keep on top of other windows
# root.call("wm", "attributes", ".", "-alpha", "0.9") # Window Opacity 0.0-1.0
app = Application(root)
app.mainloop()
