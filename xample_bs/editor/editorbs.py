'''
code file: editorbs.py
date:
comments:
    tkauto generated

'''
from tkinter import *
import ttkbootstrap as bs
from ttkbootstrap.constants import *
import os, sys
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog # NOTE: will NOT be styled !!!
from tkinter.messagebox import showerror

class Application(bs.Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        bs.Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)

        ''' ONLY OPTIONS FOR 'grid' FUNCTIONS:
                column  row
                columnspan  rowspan
                ipadx and ipady
                padx and pady
                sticky="nsew"
        -------------------------------------------------------- '''

        #app.geometry("500x400")

        self.editor = Text(self)
        self.editor.grid(row=1, column=1, columnspan=2, sticky='nsew')
        self.editor.config(wrap=NONE    , # wrap=NONE
                           undo=True, # Tk 8.4
                           width=50,
                           height=20,
                           )
        self.editor.focus()

        # efont = Font(family="Helvetica", size=14)
        # self.EDITOR.configure(font=efont)
        # self.EDITOR.config(wrap="word", # wrap=NONE
        #                    undo=True, # Tk 8.4
        #                    width=50,
        #                    height=12,
        #                    padx=5, # inner margin
        #                    insertbackground='#000',   # cursor color
        #                    tabs=(efont.measure(' ' * 4),))
        # self.EDITOR.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")
        

        self.scr = bs.Scrollbar(self, orient=VERTICAL, command=self.editor.yview)
        self.scr.grid(row=1, column=3, sticky='nsw')  # use nse
        self.editor['yscrollcommand'] = self.scr.set

        # get font,size to be used with Text widget
        if os.path.isfile("font"):
            with open("font") as f:
                self.fontname = f.read().strip()
        else:
            self.fontname = "Monospace, 12"
        fnt = self.fontname.split(",")
        fnt = [i.strip() for i in fnt]
        efont = Font(family=fnt[0], size=fnt[1])
        self.editor.configure(font=efont, tabs=(efont.measure(' ' * 4),))

        self.vlbl = bs.StringVar()
        lblstat = bs.Label(self, text='status…', textvariable=self.vlbl)
        lblstat.grid(row=3, column=1, columnspan=3, sticky='ew')
        self.vlbl.set('status…')

        menubar = Menu(app)
        mn_file = Menu(menubar, tearoff=0)
        mn_file.add_command(label="New", command=self.mn_file_new, accelerator="Ctrl-n", underline=1)
        mn_file.add_command(label="Open", command=self.mn_file_open)
        mn_file.add_command(label="Save", command=self.mn_file_save, accelerator="Ctrl-s", underline=1)
        mn_file.add_command(label="Save-As", command=self.mn_file_saveas)
        mn_file.add_separator()
        mn_file.add_command(label="Exit", command=self.mn_file_exit, accelerator="Ctrl-q")
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


    def mn_edit_font(self):
        if os.path.isfile("font"):
            with open("font") as f:
                self.fontname = f.read().strip()
        self.fontname = simpledialog.askstring("Choose Font", "Current: " + self.fontname)
        if self.fontname is not None:
            with open("font", "w") as f:
                f.write(self.fontname)
            fnt = self.fontname.split(",")
            fnt = [i.strip() for i in fnt]
            efont = Font(family=fnt[0], size=fnt[1])
            self.editor.configure(font=efont)


    def do_popup(self,event):
        try:
            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)
        finally:
            self.popup_menu.grab_release()


    def clipbrd(self, n):
        ''' handle clipboard commands from context menu '''
        if n == 1:  # Copy
            if self.editor.tag_ranges("sel"):
                app.clipboard_clear()  # clear clipboard contents
                app.clipboard_append(self.editor.selection_get())  # copy to clipboard
        elif n == 3:  # Cancel
            inx = self.editor.index(INSERT)
            self.editor.insert(inx, "")
        else:
            # n == 2:  # Paste
            inx = self.editor.index(INSERT)
            self.editor.insert(inx, app.clipboard_get())  # paste


    def mn_file_new(self, event=None):
        ''' Create a New editor file '''
        if self.editor.edit_modified():  # modified
            response = messagebox.askyesnocancel(
                "Save?", "text was modified.\nsave changes?"
            )
            if response is True:
                self.mn_file_save()
        self.editor.delete("1.0", END)  # clear the Text widget
        self.editor.mark_set(INSERT, "1.0")  # place cursor at 1st character in file
        self.editor.edit_modified(False)
        self.editor.focus()
        self.infile = "untitled"
        self.vlbl.set(self.infile)


    def mn_file_open(self, event=None):
        ''' open a file from the system and put it in the editor '''
        f_name = filedialog.askopenfilename(
            filetypes=(("Text files", "*.txt"), ("all files", "*"))
        )
        if f_name:
            with open(f_name) as r_hand:
                file_text = r_hand.read()
            self.editor.delete("1.0", END)  # clear the Text widget
            self.editor.insert("1.0", file_text)
            self.editor.mark_set(INSERT, "1.0")  # place cursor at 1st character in file
            self.editor.edit_modified(False)
            self.editor.focus()
            self.infile = f_name
            self.vlbl.set(self.infile)


    def mn_file_save(self, event=None):
        ''' Save the current editor file '''
        if self.infile == "untitled":
            self.mn_file_saveas()  # This was a new file
            return
        with open(self.infile, "wb") as f_hand:
            file_text = self.editor.get(1.0, "end-1c")
            f_hand.write(bytes(file_text, "UTF-8"))
        self.editor.edit_modified(False)


    def mn_file_saveas(self, event=None):
        ''' Save current editor file as a different filename '''
        f_name = filedialog.asksaveasfilename(
            confirmoverwrite=True, initialdir=os.path.dirname(os.path.abspath(__file__))
        )
        if f_name:
            try:
                with open(f_name, "w") as f:
                    f.write(self.editor.get("1.0", END))
                self.infile = f_name
                self.vlbl.set(self.infile)
                self.editor.edit_modified(False)
            except:
                showerror("Save File", "Failed to save file\n'%s'" % f_name)
            return


    def mn_file_exit(self, event=None):
        ''' Exit the editor App '''
        if self.editor.edit_modified():  # modified
            response = messagebox.askyesnocancel(
                "Save?", "text was modified.\nsave changes?"
            )
            if response is True:
                self.mn_file_save()
        save_location()
        sys.exit()


    def mn_edit_undo(self):
        ''' docstring '''
        self.editor.edit_undo()


    def mn_edit_selall(self, event=None):
        ''' docstring '''
        self.editor.tag_add("sel", "1.0", "end")
        return "break"


    def mn_edit_copy(self, event=None):
        ''' copy selected from editor '''
        self.clipbrd(1)

    def mn_edit_paste(self, event=None):
        ''' paste clipboard to editor '''
        self.clipbrd(2)


    def mn_help_index(self):
        ''' docstring '''
        pass

    def mn_help_about(self):
        ''' docstring '''
        messagebox.showinfo("editor About", "Created by me for you.")


def save_location(e=None):
    ''' executes at WM_DELETE_WINDOW event - see below '''
    with open("winfo", "w") as fout:
        fout.write(app.geometry())
    app.destroy()


    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass

#

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
def save_location(e=None):
    ''' executes at WM_DELETE_WINDOW event - see below '''
    with open("winfo", "w") as fout:
        fout.write(app.geometry())
    app.destroy()

app = bs.Window("tkbauto template", "solar")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

# UNCOMMENT THE FOLLOWING TO SAVE GEOMETRY INFO
if os.path.isfile("winfo"):
    with open("winfo") as f:
        lcoor = f.read()
    app.geometry(lcoor.strip())
else:
    app.geometry("400x300") # WxH+left+top


# app.protocol("WM_DELETE_WINDOW", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO
bs.Sizegrip(app).place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
# app.resizable(0, 0) # no resize & removes maximize button
# app.minsize(w, h)  # width, height
# app.maxsize(w, h)
# app.overrideredirect(True) # removed window decorations
# app.iconphoto(False, PhotoImage(file='icon.png'))
# app.attributes("-topmost", True)  # Keep on top of other windows

Application(app)

app.mainloop()
