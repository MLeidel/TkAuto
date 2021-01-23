from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # module applied to all widgets

# root = Tk()
# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam'
root = ThemedTk(theme="clam")
note = Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)


note.add(tab1, text = "Tab 1")
note.add(tab2, text = "Tab 2")
note.add(tab3, text = "Tab 3")

note.grid(row=1, column=1)

Button(tab1, text='Exit', command=root.destroy).grid(row=1, column=1, padx=100, pady=100)
Label(tab2, text='Hi - its tab 2.').pack(padx=100, pady=100)

root.mainloop()
exit()
