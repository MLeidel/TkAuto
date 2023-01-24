'''
list themes
'''
import os, sys
from tkinter.font import Font
from ttkbootstrap import *
from ttkbootstrap.constants import *

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        tms = root.style.theme_names()
        print(tms)


root = Window("themes", "superhero", size=(400,300))

Application(root)

root.mainloop()
