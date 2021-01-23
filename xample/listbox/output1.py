'''
output1.py
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        self.lst = Listbox(self, height=5)
        self.lst.grid(row=1, column=1, sticky='nse')

        self.lst.bind("<Double-Button-1>", self.on_dblclick_list)
        for i in range(100):
            self.lst.insert(i, str(i) + "Item")

        self.scroll = Scrollbar(self, orient=VERTICAL, command=self.lst.yview)
        self.scroll.grid(row=1, column=2, rowspan=2, sticky='nsw')  # use N+S+E
        self.lst['yscrollcommand'] = self.scroll.set

        self.vlbltext = StringVar()
        labelv = Label(self, text='…', textvariable=self.vlbltext)
        labelv.grid(row=3, column=1)
        self.vlbltext.set('…')

        buttonv = Button(self, text='Select', command=self.on_buttonv_clicked)
        buttonv.grid(row=4, column=1)

    def on_buttonv_clicked(self):
        ''' copy selected item to label '''
        if self.lst.curselection() == ():   # empty tuple means nothing selected
            return # nothing selected
        list_item = self.lst.curselection()
        fp = self.lst.get(list_item[0])
        self.vlbltext.set(str(fp))

    def on_dblclick_list(self, event):
        ''' action for double clicking the listbox item '''
        list_item = self.lst.curselection()
        fp = self.lst.get(list_item[0])
        print(str(fp) + " --> " + str(list_item[0]) +
              " of " + str(self.lst.size()))

# root = Tk()
# Requires ttkthemes module
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam', 'smog'
# 'kroc', 'black', 'clearlooks'
# 'radiance', 'blue' : https://wiki.tcl-lang.org/page/List+of+ttk+Themes
root = ThemedTk(theme="clam")

root.title("Listbox")
app = Application(root)
app.mainloop()
