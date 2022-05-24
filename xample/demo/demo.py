'''
code file:
date:
commants:
    tkauto generated

'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os
from tkinter.font import Font
import sys
# import webbrowser
# import pyperclip
# from tkinter import filedialog
from tkinter import messagebox
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

        self.style = Style()
        self.style.configure("TButton", width=15)

        root.geometry("670x340")

        self.lst = Listbox(self, height=5, borderwidth=0)
        self.lst.grid(row=1, column=1, sticky='nsew')
        self.lst.bind("<<ListboxSelect>>", self.on_select_list)
        for i in range(100):
            self.lst.insert(i, str(i) + "Item")
        self.sb_lst = Scrollbar(self, orient=VERTICAL, command=self.lst.yview)
        self.sb_lst.grid(row=1, column=2, sticky='nsw')  # use nse
        self.lst['yscrollcommand'] = self.sb_lst.set

        self.txt = Text(self, borderwidth=0, width=25)
        self.txt.grid(row=1, column=3, sticky='nsew')
        efont = Font(family="Helvetica", size=14)
        self.txt.configure(font=efont)
        self.txt.config(wrap="word", # wrap=NONE
                           undo=True, # Tk 8.4
                           height=12,
                           insertbackground='#000',   # cursor color
                           tabs=(efont.measure(' ' * 4),))
        self.sb_txt = Scrollbar(self, orient=VERTICAL, command=self.txt.yview)
        self.sb_txt.grid(row=1, column=4, sticky='nsw')  # use nse
        self.txt['yscrollcommand'] = self.sb_txt.set
        self.txt.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")

        self.prg_bar = Progressbar(self, orient='horizontal', mode='indeterminate', maximum=40)
        self.prg_bar.grid(row=2, column=1, columnspan=4, sticky='ew', pady=4)
        # prg_bar.start() | prg_bar.stop() | prg_bar.grid_forget() | prg_bar.grid(self, ...)

        btn_progress = Button(self, text='Progress Bar', command=self.progress)
        btn_progress.grid(row=3, column=1)

        btn_close = Button(self, text='Close', command=exit)
        btn_close.grid(row=3, column=3)

        # column 5 frame with widgets

        fram = Frame(self, padding=5)
        fram.grid(row=1, column=5, sticky='nsew')

        self.vrad = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad1 = Radiobutton(fram, variable=self.vrad,
                           value='1', text='choice 1')
        rad1.grid(row=1, column=1, padx=7)

        self.vrad2 = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad2 = Radiobutton(fram, variable=self.vrad,
                           value='2', text='choice 2')
        rad2.grid(row=2, column=1, padx=7)

        self.vrad3 = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        rad3 = Radiobutton(fram, variable=self.vrad,
                           value='3', text='choice 3')
        rad3.grid(row=3, column=1, padx=7)

        self.vchk1 = IntVar()
        chk1 = Checkbutton(fram, variable=self.vchk1, text='checkbox 1')
        chk1.grid(row=1, column=2)

        self.vchk2 = IntVar()
        chk2 = Checkbutton(fram, variable=self.vchk2, text='checkbox 2')
        chk2.grid(row=2, column=2)

        optionlist = ('black     ', 'default   ', 'alt       ', 'scidblue  ', 'radiance  ', 'clearlooks')
        self.vopts = StringVar()
        self.vopts.set(optionlist[0])
        opts = OptionMenu(fram, self.vopts, *optionlist)
        opts.grid(row=3, column=2)

        lbl = Label(fram, text='Below is an Entry field')
        lbl.grid(row=4, column=1, columnspan=2, sticky='ew', pady=5, padx=4)

        self.vtbx = StringVar()
        # self.vtbx.trace("w", self.eventHandler)
        tbx = Entry(fram, textvariable=self.vtbx)
        tbx.grid(row=5, column=1, columnspan=2, sticky='ew')

        self.vcombo = StringVar()
        combo = Combobox(fram, textvariable=self.vcombo)
        combo['values'] = ('black', 'default', 'alt', 'scidblue', 'radiance', 'clearlooks', 'scidgrey', 'scidpurple', 'clam', 'smog')
        combo.bind('<<ComboboxSelected>>', self.oncomboselect)
        combo.current(0)
        combo.grid(row=6, column=1, columnspan=2, sticky='ew', pady=5, padx=4)

        self.vsc = DoubleVar()
        sc = Scale(fram, variable=self.vsc)
        sc.grid(row=7, column=1, columnspan=2, sticky='ew')
        # str(self.vsc.get())

    # HANDLERS FOLLOW


    def progress(self):
        ''' work progress bar '''
        self.prg_bar.start()

    def oncomboselect(self, event):
        thame = self.vcombo.get()
        messagebox.showinfo("Hi", thame)
        self.style.theme_use(thame)
        self.style.configure("TButton", width=15)

    def on_select_list(self, event):
        list_item = self.lst.curselection()
        fp = self.lst.get(list_item[0])
        print(str(fp) + " --> " + str(list_item[0]) +
            " of " + str(self.lst.size()))

# ttkthemes
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="scidblue")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))


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
