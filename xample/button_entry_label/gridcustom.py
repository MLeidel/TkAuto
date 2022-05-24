from tkinter import *
import customtkinter as ct

class Application(ct.CTkFrame):
    ''' main class docstring '''
    def __init__(self, parent):
        ct.CTkFrame.__init__(self, parent)
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
        lbl1 = ct.CTkLabel(self, text='type something',
                           textvariable=self.vlbl1,
                           corner_radius=10)
        lbl1.grid(row=1, column=1)

        self.vent1 = StringVar()
        ent1 = ct.CTkEntry(self, textvariable=self.vent1,
                           corner_radius=10)
        ent1.grid(row=2, column=1 , sticky='ew')

        btn1 = ct.CTkButton(self, text='OK',
                            corner_radius=10,
                            command=self.on_btn1_clicked)
        btn1.grid(row=3, column=1 , sticky='ew')

    def on_btn1_clicked(self):
        ''' transfer Entry text to Lable text '''
        text = self.vent1.get()
        self.vlbl1.set(text)

ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
ct.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = ct.CTk()

root.title("gridcustom.py")
app = Application(root)
app.mainloop()
