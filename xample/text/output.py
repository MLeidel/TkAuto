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

        self.textv = Text(self)
        self.textv.grid(row=1, column=1, columnspan=3)

        
        # efont = Font(family="Helvetica", size=14)
        # self.EDITOR.configure(font=efont)
        # self.EDITOR.config(wrap = "word", # wrap = NONE
        #        undo = True, # Tk 8.4
        #        width = 80,
        #        tabs = (efont.measure(' ' * 4),))
        # self.EDITOR.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")
        

        self.scry = Scrollbar(self, orient=VERTICAL, command=self.textv.yview)
        self.scry.grid(row=1, column=4, sticky='wns')  # use N+S+E
        self.textv['yscrollcommand'] = self.scry.set

        self.scrx = Scrollbar(self, orient=HORIZONTAL, command=self.textv.xview)
        self.scrx.grid(row=2, column=1, columnspan=3, sticky='wen')
        self.textv['xscrollcommand'] = self.scrx.set

        btnOpen = Button(self, text='Open', command=self.on_btn_open_clicked)
        btnOpen.grid(row=3, column=1)

        btnSave = Button(self, text='Save', command=self.on_btn_save_clicked)
        btnSave.grid(row=3, column=2)

        btnClose = Button(self, text='Close', command=self.on_btn_close_clicked)
        btnClose.grid(row=3, column=3)

        
        # from tkinter import filedialog
        # filename =  filedialog.askopenfilename(initialdir = "/",
        #             title = "Open file",
        #             filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        # filename = filedialog.asksaveasfilename(initialdir = "/",
        #             title = "Save file",
        #             filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    def on_btn_open_clicked(self):
        ''' docstring '''

    def on_btn_save_clicked(self):
        ''' docstring '''

    def on_btn_close_clicked(self):
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
