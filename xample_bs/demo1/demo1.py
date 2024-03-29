'''
demo1.py
no * import for tkinter
no need to preface functions for ttkbootstrap
'''
from tkinter import Listbox
from ttkbootstrap import *
from ttkbootstrap.constants import *
import os, sys
from tkinter.font import Font


class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        btn = Button(self, text='Close', command=exit)
        btn.grid(row=1, column=1)

        self.vent =StringVar()
        # self.vent.trace("w", self.eventHandler)
        ent = Entry(self, textvariable=self.vent, width=10)
        ent.grid(row=2, column=1)

        optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
        self.vopt =StringVar()
        self.vopt.set(optionlist[0])
        opt = OptionMenu(self, self.vopt, *optionlist)
        opt.grid(row=3, column=1)

        self.vcombo =StringVar()
        combo = Combobox(self, textvariable=self.vcombo, width=10)
        combo['values'] = ('value1', 'value2', 'value3')
        combo.bind('<<ComboboxSelected>>', self.combo1selected)
        combo.current(0)
        combo.grid(row=4, column=1, padx=6)

        self.vlbl =StringVar()
        lbl = Label(self, text='', textvariable=self.vlbl)
        lbl.grid(row=5, column=1)
        self.vlbl.set('')

        self.vbar =DoubleVar()
        bar = Scale(self, variable=self.vbar)
        bar.grid(row=6, column=1)
        # str(self.var.get())

        self.vchk = IntVar()
        chk = Checkbutton(self, variable=self.vchk, text='check me out')
        chk.grid(row=7, column=1, pady=10)


        frm = Frame(self, width=100, height=100)
        frm.grid(row=8, column=1)
        
        btn2 = Button(frm, text='Button', command=self.proc)
        btn2.grid(row=1, column=1)

        self.vlbl2 =StringVar()
        lbl2 = Label(frm, text='Label', textvariable=self.vlbl2)
        lbl2.grid(row=2, column=1)
        self.vlbl2.set('Label')

        self.txt = Text(self, width=16)
        self.txt.grid(row=1, column=2, rowspan=6)

        
        efont = Font(family="Helvetica", size=14)
        self.txt.configure(font=efont)
        self.txt.config(wrap="word", # wrap=NONE
                           undo=True, # Tk 8.4
                           width=40,
                           height=12,
                           padx=5, # inner margin
                           tabs=(efont.measure(' ' * 4),))
        self.txt.focus()
        

        self.sctxt = Scrollbar(self, orient=VERTICAL, command=self.txt.yview)
        self.sctxt.grid(row=1, column=3, rowspan=6, sticky='nsw')  # use nse
        self.txt['yscrollcommand'] = self.sctxt.set

        sep = Separator(self)
        sep.grid(row=7, column=2, columnspan=4, sticky='ew')

        menubar = Menu(app)
        mn_file = Menu(menubar, tearoff=0)
        mn_file.add_command(label="New", command=self.mn_file_new, accelerator="Ctrl-n", underline=1)
        mn_file.add_command(label="Open", command=self.nm_file_open)
        mn_file.add_command(label="Save", command=self.nm_file_save, accelerator="Ctrl-s", underline=1)
        mn_file.add_command(label="Save-As", command=self.nm_file_saveas)
        mn_file.add_separator()
        mn_file.add_command(label="Exit", command=exit, accelerator="Ctrl-q")
        menubar.add_cascade(label="File", menu=mn_file)
        mn_edit = Menu(menubar, tearoff=0)
        mn_edit.add_command(label="Undo", command=self.mn_edit_undo, accelerator="Ctrl-z")
        mn_edit.add_command(label="Select All", command=self.mn_edit_selall, accelerator="Ctrl-a")
        submenu = Menu(mn_edit, tearoff=False)
        submenu.add_command(label="Copy", command=self.mn_edit_copy, accelerator="Ctrl-c")
        submenu.add_command(label="Paste", command=self.mn_edit_paste, accelerator="Ctrl-v")
        mn_edit.add_cascade(label="Clipboard", menu=submenu, underline=2)
        menubar.add_cascade(label="Edit", menu=mn_edit)
        mn_help = Menu(menubar, tearoff=0)
        mn_help.add_command(label="Help Index", command=self.mn_help_index)
        mn_help.add_command(label="About…", command=self.mn_help_about)
        menubar.add_cascade(label="Help", menu=mn_help)
        app.config(menu=menubar) # display the menu


        # LISTBOX
        self.lst = Listbox(self, exportselection=False)
        self.lst.grid(row=1, column=4, rowspan=6, sticky='nsew')
        
        self.lst.bind("<<ListboxSelect>>", self.on_select_list)
        for i in range(100):
            self.lst.insert(END, "Item-" + str(i))

        self.sclst = Scrollbar(self, orient=VERTICAL, command=self.lst.yview)
        self.sclst.grid(row=1, column=5, rowspan=6, sticky='nsw')  # use nse
        self.lst['yscrollcommand'] = self.sclst.set
        
        # COMBOBOX
        self.vcmbx = StringVar()
        cmbx = Combobox(self, textvariable=self.vcmbx, width=6)
        cmbx['values'] = app.style.theme_names()

        cmbx.current(0)
        cmbx.grid(row=8, column=2, sticky='ew', padx=4)
        cmbx.bind('<<ComboboxSelected>>', self.comboselected)

        frm2 = Frame(self)
        frm2.grid(row=8, column=3, columnspan=3, sticky='nsew')

        self.vrad = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        radyes = Radiobutton(frm2, variable=self.vrad, value='Yes', text='Yes')
        radyes.grid(row=1, column=1, sticky='we', padx=10)
        radno = Radiobutton(frm2, variable=self.vrad, value='No', text='No')
        radno.grid(row=2, column=1, sticky='we', padx=10)

    def on_select_list(self, event):
        list_item = self.lst.get(ANCHOR)
        list_inx = self.lst.index(ANCHOR)
        print(list_item, str(list_inx) +
              " of " + str(self.lst.size()))

    def comboselected(self, event):
        thame = self.vcmbx.get()
        print(thame)
        Style(theme=thame)

    def combo1selected(self, event):
        val = self.vcombo.get()
        print(val)

    def exit(self):
        ''' docstring '''

    def proc(self):
        ''' docstring '''

    def mn_file_new(self):
        ''' docstring '''

    def nm_file_open(self):
        ''' docstring '''

    def nm_file_save(self):
        ''' docstring '''

    def nm_file_saveas(self):
        ''' docstring '''

    def nm_file_exit(self):
        ''' docstring '''

    def mn_edit_undo(self):
        ''' docstring '''

    def mn_edit_selall(self):
        ''' docstring '''

    def mn_edit_copy(self):
        ''' docstring '''

    def mn_edit_paste(self):
        ''' docstring '''

    def mn_help_index(self):
        ''' docstring '''

    def mn_help_about(self):
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
#         fout.write(app.geometry())
#     app.destroy()

app = Window("tkbauto template", "superhero")
app.configure(background="#2b3e50")  # superhero: bg

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
Sizegrip(app).place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
# app.resizable(0, 0) # no resize & removes maximize button
# app.minsize(w, h)  # width, height
# app.maxsize(w, h)
# app.overrideredirect(True) # removed window decorations
# app.iconphoto(False, PhotoImage(file='icon.png'))
# app.attributes("-topmost", True)  # Keep on top of other windows

Application(app)

app.mainloop()
