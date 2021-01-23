'''
code file:
date:
commants:
    tkauto generated
    radio buttons and options menu demo
'''

from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets
from tkinter import messagebox

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        self.columnconfigure(1, weight=1, pad=10)
        self.rowconfigure(1, weight=1, pad=20)
        self.rowconfigure(2, weight=1, pad=20)
        self.rowconfigure(3, weight=1, pad=20)
        self.rowconfigure(4, weight=1, pad=20)
        self.rowconfigure(5, weight=1, pad=20)

        # customize widget style when using ttk...
        style = Style()
        style.configure("TButton", width=16)

        root.geometry("200x200")

        self.radvar = StringVar() # USE ONE VAR PER GROUP OF BUTTONS
        r1 = Radiobutton(self, variable=self.radvar, value='Fish', text='Fish')
        r1.grid(row=1, column=1)

        r2 = Radiobutton(self, variable=self.radvar, value='Ham', text='Ham')
        r2.grid(row=2, column=1)

        r3 = Radiobutton(self, variable=self.radvar, value='Beef', text='Beef')
        r3.grid(row=3, column=1)

        optionlist = ('1.0 lb', '1.5 lb', '2.0 lb', '0.5 lb')
        self.optv = StringVar()
        self.optv.set(optionlist[0])
        optionlist = OptionMenu(self, self.optv, *optionlist)
        optionlist.grid(row=4, column=1)
        optionlist.configure(width=15)  # can't use 'width' in the widget constructor

        btn = Button(self, text='Order', command=self.on_btn_clicked)
        btn.grid(row=5, column=1)


    def on_btn_clicked(self):
        ''' Show messagebox of meat order '''
        meat = self.radvar.get()
        weight = self.optv.get()
        print(meat, weight)
        messagebox.showinfo("Meat Order",meat + "\n" + weight)


# root = Tk()
# Requires ttkthemes module
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="scidsand")

root.title("Demo")
root.resizable(0,0) # no resize & removes maximize button
app = Application(root)
app.mainloop()
