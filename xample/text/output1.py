'''
code file:
date:
commants:
    tkauto generated
    Text widget and filedialog
'''

from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets
from tkinter.font import Font
# from tkinter import messagebox
from tkinter import filedialog
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
        # style.configure("TButton", width=12)

        self.textedit = Text(self)
        self.textedit.grid(row=1, column=1, columnspan=3)

        efont = Font(family="Helvetica", size=14)
        self.textedit.configure(font=efont)
        self.textedit.config(wrap = NONE, # wrap = NONE
               undo = True, # Tk 8.4
               width = 80,
               tabs = (efont.measure(' ' * 4),))
        self.textedit.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")


        self.scry = Scrollbar(self, orient=VERTICAL, command=self.textedit.yview)
        self.scry.grid(row=1, column=4, sticky='wns')  # use N+S+E
        self.textedit['yscrollcommand'] = self.scry.set

        self.scrx = Scrollbar(self, orient=HORIZONTAL, command=self.textedit.xview)
        self.scrx.grid(row=2, column=1, columnspan=3, sticky='wen')
        self.textedit['xscrollcommand'] = self.scrx.set

        btnOpen = Button(self, text='Open', command=self.on_btn_open_clicked)
        btnOpen.grid(row=3, column=1, pady=8)

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
        ''' Pick a file to open into the Text widget '''
        fname = filedialog.askopenfilename(initialdir = "./",
                    title = "Open Text File",
                    filetypes = (("text files","*.txt"),("all files","*.*")))
        text = ""
        with open(fname, 'r') as f:
            text = f.read()
        print(text)
        self.textedit.delete("1.0", END)
        self.textedit.insert("1.0", text)

    def on_btn_save_clicked(self):
        ''' Save the open file as some other file name '''
        fname = filedialog.asksaveasfilename(initialdir = "./",
                    title = "Save file As",
                    filetypes = (("text files","*.txt"),("all files","*.*")))
        # file Save follows
        text = self.textedit.get(1.0, END)
        with open(fname, "w") as f:
            f.write(text)

    def on_btn_close_clicked(self):
        ''' Exit the program '''
        root.destroy()


# root = Tk()
# Requires ttkthemes module
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="clearlooks")

root.title("Text & filedialog")
app = Application(root)
app.mainloop()
