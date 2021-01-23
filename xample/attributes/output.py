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

        lbl = Label(self, text='I’m a Label', relief=SUNKEN, padding=4)
        lbl.grid(row=2, column=1)

        self.tbVar = StringVar()
        # self.tbVar.trace("w", self.eventHandler)
        tb = Entry(self, textvariable=self.tbVar, width=10, show='*')
        tb.grid(row=3, column=1)

        self.tx = Text(self, width=40, bg='#eee', height=5)
        self.tx.grid(row=4, column=1)

        
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
        

        self.radVar = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad = Radiobutton(self, variable=self.radVar, value='Radio 1', text='Radio 1', cursor='hand1', padding=2)
        rad.grid(row=5, column=1)

        self.radVar = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad = Radiobutton(self, variable=self.radVar, value='Radio 2', text='Radio 2', cursor='hand1', padding=2)
        rad.grid(row=6, column=1)

        self.chkVar = IntVar()
        chk = Checkbutton(self, variable=self.chkVar, text='Check1', onvalue=1)
        chk.grid(row=7, column=1)

        self.spnVar = StringVar()
        spn = Spinbox(self, textvariable=self.spnVar, from_=5, to=25, increment=5, width=5)
        spn.grid(row=8, column=1)

        optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
        self.optVar = StringVar()
        self.optVar.set(optionlist[0])
        opt = OptionMenu(self, self.optVar, *optionlist)
        opt.grid(row=9, column=1)

        self.cbxVar = StringVar()
        cbx = Combobox(self, textvariable=self.cbxVar, width=15)
        cbx['values'] = ('value1', 'value2', 'value3')
        # COMBO.bind('<<ComboboxSelected>>', self.ONCOMBOSELECT)
        cbx.current(0)
        cbx.grid(row=10, column=1)

        nbook = Notebook(self, cursor='hand1')
        tab1 = Frame(nbook, width=200, height=200)
        tab2 = Frame(nbook)
        tab3 = Frame(nbook)
        nbook.add(tab1, text = 'tab 1')
        nbook.add(tab2, text = 'tab 2')
        nbook.add(tab3, text = 'tab 3')
        nbook.grid(row=11, column=1)

        
        Button(tab1, text='Exit',
               command=root.destroy).grid(row=1, column=1, padx=100, pady=100)
        Label(tab2, text='tab 2').pack(padx=50, pady=50)
        Label(tab3, text='tab 3').pack(padx=50, pady=50)
        

        self.scrx = Scrollbar(self, orient=HORIZONTAL, command=self.tx.xview)
        self.scrx.grid(row=12, column=1, sticky='ew')
        self.tx['xscrollcommand'] = self.scrx.set

        
        # self.popup_menu = Menu(self, tearoff = 0)
        # self.popup_menu.add_command(label = "Copy",
        #                             command = lambda:self.function(1))
        # self.popup_menu.add_command(label = "Paste",
        #                             command = lambda:self.function(2))
        # self.popup_menu.add_separator()
        # self.popup_menu.add_command(label = "say bye", command = exit)
        # self.txt.bind("<Button-3>",self.do_popup)

    # def do_popup(self,event):
    #     try:
    #         self.popup_menu.tk_popup(event.x_root,
    #                                  event.y_root)
    #     finally:
    #         self.popup_menu.grab_release()
        



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
