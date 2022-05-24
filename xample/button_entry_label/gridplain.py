from tkinter import *

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        self.columnconfigure(1, weight=1, pad=100)
        self.rowconfigure(1, weight=1, pad=20)
        self.rowconfigure(2, weight=1, pad=20)
        self.rowconfigure(3, weight=1, pad=20)

        root.geometry("250x150")

        self.vlbl1 = StringVar()
        lbl1 = Label(self, text='…', textvariable=self.vlbl1, justify='right')
        lbl1.grid(row=1, column=1)

        self.vent1 = StringVar()
        ent1 = Entry(self, textvariable=self.vent1)
        ent1.grid(row=2, column=1 , sticky='ew')

        btn1 = Button(self, text='OK', command=self.on_btn1_clicked)
        btn1.grid(row=3, column=1 , sticky='ew')

    def on_btn1_clicked(self):
        ''' transfer Entry text to Lable text '''
        text = self.vent1.get()
        self.vlbl1.set(text)
root = Tk()

root.title("gridcustom.py")
app = Application(root)
app.mainloop()
