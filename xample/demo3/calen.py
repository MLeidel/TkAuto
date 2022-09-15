'''
code file: calen.py
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os, sys
from tkinter.font import Font
from tkcalendar import *
from time import gmtime, strftime
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''

        self.calen = Calendar(self)
        self.calen.grid(row=1, column=1, sticky='nsew')

        # self.cal = Calendar(self, selectmode="day",
        #                     year=int(strftime('%Y')),
        #                     month=int(strftime('%m')),
        #                     day=int(strftime('%d')),
        #                     width=400,
        #                     cursor="hand1",
        #                     date_pattern='yyyy-mm-dd')
        ###
        root.bind("<<CalendarSelected>>", self.calselected)
        #  self.calselected(None)
        #  date_key = self.cal.get_date()
        ###
        
    def calselected(self, e=None):
        print(self.calen.get_date())

root = ThemedTk(theme="scidmint")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))


root.title("Tkinter Demo")
app = Application(root)
app.mainloop()
