'''
tkauto_tpl.py
Used with tkauto.py and tkmenu.py
'''

from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets
# from tkinter.font import Font
# import requests, sys, os, csv, webbrowser
# from tkinter.filedialog import askopenfilename
# from tkinter import messagebox

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
        self.rowconfigure(2, weight=1, pad=20)
        self.rowconfigure(3, weight=1, pad=20)

        root.geometry("250x150")

        self.vlbl1 = StringVar()
        lbl1 = Label(self, text='…', textvariable=self.vlbl1, justify='right')
        lbl1.grid(row=1, column=1)

        self.vent1 = StringVar()
        # self.vent1.trace("w", self.eventHandler)
        ent1 = Entry(self, textvariable=self.vent1)
        ent1.grid(row=2, column=1 , sticky='ew')

        btn1 = Button(self, text='OK', command=self.on_btn1_clicked)
        btn1.grid(row=3, column=1 , sticky='ew')

    def on_btn1_clicked(self):
        ''' transfer Entry text to Lable text '''
        text = self.vent1.get()
        self.vlbl1.set(text)



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

# root = Tk()  # use this for when no theme
#
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam'
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
# root.overrideredirect(True) # removed window decorations
# root.resizable(0,0) # no resize & removes maximize button
# root.iconphoto(False, PhotoImage(file='icon.png'))
# root.attributes("-topmost", True)  # Keep on top of other windows
app = Application(root)
app.mainloop()
