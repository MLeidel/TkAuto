from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
from ttkthemes import ThemedTk  # module applied to all widgets
                                # pip install ttkthemes

class Application(Frame):
    ''' use oop format for GUI program '''
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        ''' define widgets and show '''
        style = Style()
        style.configure('TButton', width=14, font='Purisa 15')

        btn1 = Button(self, text="Close App", command=exit)
        btn1.grid(row=0,column=0, padx=5, pady=5)

        btn2 = Button(self, text="Ok", command=exit)
        btn2.grid(row=1,column=0, padx=5, pady=5)

# 'alt', 'scidsand', 'classic', 'scidblue',
# 'scidmint', 'scidgreen', 'default', 'scidpink',
# 'arc', 'scidgrey', 'scidpurple', 'clam'
root = ThemedTk(theme="scidsand")
root.title("ThemedTk (scidsand) W/Style config")
app = Application(master=root)
app.mainloop()
