'''
notebook of widget demos
'''
from ttkbootstrap import *
from ttkbootstrap.constants import *
import os, sys
from tkinter.font import Font
from tkinter import simpledialog
from tkinter import Message
from tkinter import Listbox


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
        tab2 = Frame(notebk, width=99, height=99)
        tab3 = Frame(notebk, width=99, height=99)
        notebk.add(tab2, text='Some Widgets')
        notebk.add(tab3, text='More Widgets')
        notebk.grid(row=1, column=1)

        msgtext = '''
Hello, this is a 'Message' widget.
tkinter provides this for multi-line
read-only text display. Note the
Message widget does not seem to be
supported by ttkbootstrap.

The Notebook widget is quite simple.
TkAuto just creates a 3 tab notebook.
It is obvious just by looking at the
generated code what can be done to modify it.
        '''
        msg = Message(tab2, text=msgtext, width=360)
        msg.grid(row=1, column=1, rowspan=3, sticky='nwew', padx=20, pady=20)

        btn1 = Button(tab2, text='Open Toplevel',
                         command=self.create_toplevel)
        btn1.grid(row=1, column=2, pady=10)

        self.vspn = StringVar(value=0)
        spn = Spinbox(tab2, textvariable=self.vspn,
                         from_=0, to=10,
                         command=self.procspin)
        spn.grid(row=2, column=2, pady=10)

        btn2 = Button(tab2, text='Open Simple Dialog', command=self.open_dialog)
        btn2.grid(row=3, column=2, pady=5)

        self.vspn = StringVar(value=0)
        spn = Spinbox(tab2, textvariable=self.vspn, from_=0, to=10)
        spn.grid(row=2, column=2)

        ############################
        ''' creates GUI for tab3 '''
        ############################

        btn = Button(tab3, text='Close', command=exit)
        btn.grid(row=1, column=1)

        tab3.vent =StringVar()
        # tab3.vent.trace("w", tab3.eventHandler)
        ent = Entry(tab3, textvariable=tab3.vent, width=10)
        ent.grid(row=2, column=1)

        optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')
        tab3.vopt =StringVar()
        tab3.vopt.set(optionlist[0])
        opt = OptionMenu(tab3, tab3.vopt, *optionlist)
        opt.grid(row=3, column=1)

        self.vcombo =StringVar()
        combo = Combobox(tab3, textvariable=self.vcombo, width=10)
        combo['values'] = ('value1', 'value2', 'value3')
        combo.bind('<<ComboboxSelected>>', self.combo1selected)
        combo.current(0)
        combo.grid(row=4, column=1, padx=6)

        tab3.vlbl=StringVar()
        lbl = Label(tab3, text='', textvariable=tab3.vlbl)
        lbl.grid(row=5, column=1)
        tab3.vlbl.set('')

        tab3.vbar =DoubleVar()
        bar = Scale(tab3, variable=tab3.vbar)
        bar.grid(row=6, column=1)
        # str(tab3.var.get())

        tab3.vchk = IntVar()
        chk = Checkbutton(tab3, variable=tab3.vchk, text='check me out')
        chk.grid(row=7, column=1, pady=10)


        frm = Frame(tab3, width=100, height=100)
        frm.grid(row=8, column=1)

        btn2 = Button(frm, text='Button', command=self.proc)
        btn2.grid(row=1, column=1)

        tab3.vlbl2 =StringVar()
        lbl2 = Label(frm, text='Label', textvariable=tab3.vlbl2)
        lbl2.grid(row=2, column=1)
        tab3.vlbl2.set('Label')

        tab3.txt = Text(tab3, width=16)
        tab3.txt.grid(row=1, column=2, rowspan=6)


        efont = Font(family="Helvetica", size=14)
        tab3.txt.configure(font=efont)
        tab3.txt.config(wrap="word", # wrap=NONE
                           undo=True, # Tk 8.4
                           width=40,
                           height=12,
                           padx=5, # inner margin
                           tabs=(efont.measure(' ' * 4),))
        tab3.txt.focus()


        tab3.sctxt = Scrollbar(tab3, orient=VERTICAL, command=tab3.txt.yview)
        tab3.sctxt.grid(row=1, column=3, rowspan=6, sticky='nsw')  # use nse
        tab3.txt['yscrollcommand'] = tab3.sctxt.set

        sep = Separator(tab3)
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
        self.lst = Listbox(tab3, exportselection=False)
        self.lst.grid(row=1, column=4, rowspan=6, sticky='nsew')

        self.lst.bind("<<ListboxSelect>>", self.on_select_list)
        for i in range(100):
            self.lst.insert(END, "Item-" + str(i))

        # self.sclst = Scrollbar(self, orient=VERTICAL, command=self.lst.yview)
        # self.sclst.grid(row=1, column=5, rowspan=6, sticky='nsw')  # use nse
        # self.lst['yscrollcommand'] = self.sclst.set

        # COMBOBOX
        self.vcmbx = StringVar()
        cmbx = Combobox(tab3, textvariable=self.vcmbx, width=6)
        cmbx['values'] = app.style.theme_names()

        cmbx.current(0)
        cmbx.grid(row=8, column=2, sticky='ew', padx=4)
        cmbx.bind('<<ComboboxSelected>>', self.comboselected)

        frm2 = Frame(tab3)
        frm2.grid(row=8, column=3, columnspan=3, sticky='nsew')

        tab3.vrad = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        radyes = Radiobutton(frm2, variable=tab3.vrad, value='Yes', text='Yes')
        radyes.grid(row=1, column=1, sticky='we', padx=10)
        radno = Radiobutton(frm2, variable=tab3.vrad, value='No', text='No')
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


    def create_toplevel(self):
        t = Toplevel(self)
        t.wm_title("Toplevel")
        t.geometry("200x100") # WxH+left+top
        l = Label(t, text="This is a Toplevel Window")
        l.grid(row=0, column=0, padx=2, pady=20)
        tvbtn = Button(t, text=" Exit ", command=t.destroy)
        tvbtn.grid(row=2, column=0, sticky='w', padx=2, pady=4)

    def open_dialog(self):
        ''' Demo a simpledialog '''
        s = simpledialog.askstring("Demo", "Enter something")
        print(s)

    def procspin(self):
        ''' The Spinbox value changed '''
        print(self.vspn.get())

    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass



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

app = Window("tkbauto template", "solar")

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
