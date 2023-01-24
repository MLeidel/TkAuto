'''
code file: demo1.py
    Modified code from output.py
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os, sys
from tkinter.font import Font
from tkinter import messagebox
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill="both", expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        self.style = Style()
        self.style.configure("TButton", width=15)

        btn = Button(self, text='Close', command=self.exit)
        btn.grid(row=1, column=1)

        self.vent = StringVar()
        # self.vent.trace("w", self.eventHandler)
        ent = Entry(self, textvariable=self.vent)
        ent.grid(row=2, column=1)

        optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
        self.vopt = StringVar()
        self.vopt.set(optionlist[0])
        opt = OptionMenu(self, self.vopt, *optionlist)
        opt.grid(row=3, column=1)

        self.vcombo = StringVar()
        combo = Combobox(self, textvariable=self.vcombo)
        combo['values'] = ('value1', 'value2', 'value3')
        #combo.current(0)
        combo.grid(row=4, column=1)
        combo.bind('<<ComboboxSelected>>', self.combo1selected)

        self.vlbl = StringVar()
        lbl = Label(self, text='', textvariable=self.vlbl)
        lbl.grid(row=5, column=1)
        self.vlbl.set('label')

        self.vbar = DoubleVar()
        bar = Scale(self, variable=self.vbar)
        bar.grid(row=6, column=1)
        # str(self.var.get())

        self.vchk = IntVar()
        chk = Checkbutton(self, variable=self.vchk, text='check me out')
        chk.grid(row=7, column=1)

        
        frm = LabelFrame(self, text="label frame",
                            width=100, height=100)
        frm.grid(row=8, column=1, sticky='nsew')

        btn2 = Button(frm, text='Hello', command=self.proc)
        btn2.grid(row=1, column=1)

        self.vlbl2 = StringVar()
        lbl2 = Label(frm, text='Hello', textvariable=self.vlbl2)
        lbl2.grid(row=2, column=1)
        self.vlbl2.set('Hello')

        self.txt = Text(self, width=16)
        self.txt.grid(row=1, column=2, rowspan=6, padx=(5,0), pady=5)
        efont = Font(family="Helvetica", size=14)
        self.txt.configure(font=efont)
        self.txt.config(wrap="word", # wrap=NONE
                           undo=True, # Tk 8.4
                           height=12,
                           insertbackground='#000',   # cursor color
                           tabs=(efont.measure(' ' * 4),))
        self.txt.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")
        self.sctxt = Scrollbar(self, orient="vertical", command=self.txt.yview)
        self.sctxt.grid(row=1, column=3, rowspan=6, sticky='nsw')  # use nse
        self.txt['yscrollcommand'] = self.sctxt.set

        sep = Separator(self)
        sep.grid(row=7, column=2, columnspan=4, sticky='ew')

        menubar = Menu(root)
        mn_file = Menu(menubar, tearoff=0)
        mn_file.add_command(label="New", command=self.mn_file_new, accelerator="Ctrl-n", underline=1)
        mn_file.add_command(label="Open", command=self.nm_file_open)
        mn_file.add_command(label="Save", command=self.nm_file_save, accelerator="Ctrl-s", underline=1)
        mn_file.add_command(label="Save-As", command=self.nm_file_saveas)
        mn_file.add_separator()
        mn_file.add_command(label="Exit", command=self.nm_file_exit, accelerator="Ctrl-q")
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
        root.config(menu=menubar) # display the menu

        self.lst = Listbox(self, width=10, exportselection=False)
        self.lst.grid(row=1, column=4, rowspan=6, sticky='nsew')

        self.lst.bind("<<ListboxSelect>>", self.on_select_list)
        for i in range(100):
            self.lst.insert("end", "Item-" + str(i))

    # HANDLER FOR LIST SELECTION
    # def on_select_list(self, event):
    #     list_item = self.LISTBOX.get(ANCHOR)
    #     list_inx = self.LISTBOX.index(ANCHOR)
    #     print(list_item, str(list_inx) +
    #           " of " + str(self.LISTBOX.size()))
    #
    # HANDLERS FOR EDITING LISTBOX
    #
    # def delete_item(self):
    #     if self.LISTBOX.curselection() == ():
    #         return  # nothing selected
    #     print("Deleting: " + self.LISTBOX.get(ANCHOR))
    #     self.LISTBOX.delete(self.LISTBOX.index(ANCHOR))
    #
    # def insert_item(self):
    #     if self.LISTBOX.curselection() == ():
    #         return  # nothing selected
    #     list_item = self.LISTBOX.get(ANCHOR)
    #     list_inx = self.LISTBOX.index(ANCHOR)
    #     self.LISTBOX.insert(list_inx, "Inserted this")
    #     print("inserted at " + str(list_inx))



        self.sclst = Scrollbar(self, orient="vertical", command=self.lst.yview)
        self.sclst.grid(row=1, column=5, rowspan=6, sticky='nsw')  # use nse
        self.lst['yscrollcommand'] = self.sclst.set

        self.vcmbx = StringVar()
        cmbx = Combobox(self, textvariable=self.vcmbx, width=6)
        cmbx['values'] = ('alt', 'scidsand', 'classic', 'scidblue',
                          'scidmint', 'scidgreen', 'default', 'scidpink',
                          'arc', 'scidgrey', 'scidpurple', 'clam', 'smog',
                          'kroc', 'black', 'clearlooks',
                          'radiance', 'blue')
        cmbx.current(0)
        cmbx.grid(row=8, column=2, sticky='ew', padx=4)
        cmbx.bind('<<ComboboxSelected>>', self.comboselected)

        frm2 = Frame(self)
        frm2.grid(row=8, column=3, columnspan=3, sticky='nsew')

        self.vrad = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        radyes = Radiobutton(frm2, variable=self.vrad, value='Yes', text='Yes')
        radyes.grid(row=1, column=1, sticky='ew', padx=10)
        radno = Radiobutton(frm2, variable=self.vrad, value='No', text='No')
        radno.grid(row=2, column=1, sticky='ew', padx=10)


    ## Handler for List selection
    ## Make this a class method
    def on_select_list(self, event):
        list_item = self.lst.get("anchor")
        list_inx = self.lst.index("anchor")
        print(list_item, str(list_inx) +
              " of " + str(self.lst.size()))


    def comboselected(self, event):
        thame = self.vcmbx.get()
        print(thame)
        self.style.theme_use(thame)
        self.style.configure("TButton", width=15)


    def combo1selected(self, event):
        val = self.vcombo.get()
        print(val)


    def exit(self):
        ''' docstring '''
        sys.exit()

    def proc(self):
        ''' Hello button clicked '''
        messagebox.showinfo("Hello", "H E L L O")

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
        exit()

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


# ttkthemes
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="scidmint")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))


root.title("Tkinter Demo")
app = Application(root)
app.mainloop()
