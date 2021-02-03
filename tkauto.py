'''
tkauto.py
Python console program
Author: Michael Leidel
Description:
Builds a Python tkinter application shell from an xlsx file (layout.xlsx)
with these columns:
Widget, Variable, Text, Command/Textvariable, Row, Column, Rowspan, Colspan, Sticky, other attr
'''
import os
import sys
import argparse
import openpyxl

# path for tkauto_tpl.py code template
TPLPATH = "/home/ml/apps/python/projects/ttkauto/"  # change as desired

parser = argparse.ArgumentParser(description='tkauto build Python tkinter GUI')
parser.add_argument('-o', dest='outfile', action='store',
                    default='output.py', help='output Python file')
parser.add_argument('filename', help='Excel (xlsx) file to use as input')
args = parser.parse_args()

if os.path.exists(args.filename):
    if not args.filename.endswith("xlsx"):
        print("must be an Excel (xlsx) file.")
        sys.exit()
else:
    print("cannot find file: " + args.filename)
    sys.exit()

# list (flds) index names for the (row)column values
nop, wgt, var, txt, com, row, col, rsp, csp, sty, owa = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

sout = ""  # holds output for injection into template

# Menu Only: list (flds) index names for the (row)column values
nop, mid, lbl, cmd, acc, und = 0, 1, 2, 3, 4, 5
MN_VAR = ""  # holds the menu object variable found in column 1 os ss

def prt(s):
    ''' Adjust leading tabs/spaces for output here '''
    global sout
    # print("        " + s)
    sout += "        " + s + "\n"


def getRowSpan(val):
    ''' format rowspan option '''
    rowspan = ""
    if val != "":
        rowspan = ", rowspan=" + str(val)
    return rowspan


def getColSpan(val):
    ''' format colspan option '''
    colspan = ""
    if val != "":
        colspan = ", columnspan=" + str(val)
    return colspan


def getSticky(val):
    ''' format sticky option '''
    sticky = ""
    if val != "":
        sticky = ", sticky=" + "'" + val + "'"
    return sticky

def getAttrib(val):
    ''' format misc options '''
    atts = ""
    if val != "":
        # spreadsheets don't always use plain text
        atts = ", " + val.replace("’", "'").replace('”', '"')
    return atts

# PROCESS MENU ITEMS

def proc_menu_item():
    ''' Process one line of menu code '''
    global MN_VAR
    global domenu

    if flds[mid].lower() == "endmenu":
        prt("root.config(menu=menubar) # display the menu\n\n")  # here ends the menu code
        domenu = False
        return

    ROUT = ""  # holds output for each row of python/tkinter code

    if flds[mid] != MN_VAR:  # starts a new menu or submenu item
        if flds[mid] == "submenu":
            ROUT = "submenu = Menu(" + MN_VAR +", tearoff=False)"
            MN_VAR = flds[mid]
            prt(ROUT)
            # now continue to process the row
        elif MN_VAR == "submenu":  # finished with this submenu?
            ROUT = flds[mid] + ".add_cascade(label=\""
            ROUT += flds[lbl][1:] + "\", menu=submenu"
            if flds[und] != "":
                ROUT += ", underline=" + flds[und]
            ROUT += ")"
            prt(ROUT)
            MN_VAR = flds[mid]
            return
        else:
            ROUT = flds[mid] + " = Menu(menubar, tearoff=0)"
            MN_VAR = flds[mid]
            prt(ROUT)
            # now return to process the row

    if flds[lbl] == "separator":
        ROUT = flds[mid] + ".add_separator()"
        prt(ROUT)
        return

    if flds[lbl].startswith("_"):  # end of children this is the top label
        ROUT = "menubar.add_cascade(label=\""
        ROUT += flds[lbl][1:] + "\", menu=" + flds[mid] + ")"
        prt(ROUT)
        return

    # VAR + '.add_command(label="LBL", command=self.CMD, accelerator="ACC", underline=UND)'
    ROUT = flds[mid] + ".add_command(label=\""
    ROUT += flds[lbl] + "\", command=self."
    ROUT += flds[cmd]
    callbacks.append(flds[cmd])
    if flds[acc] != "":
        ROUT += ", accelerator=\"" + flds[acc] + "\""
    if flds[und] != "":
        ROUT += ", underline=" + flds[und]
    ROUT += ")"
    prt(ROUT)

'''
    Get the Excel workbook and spreadsheet.
    The Excel file is expected to be in the app's directory.
'''

wb = openpyxl.load_workbook(args.filename)
# sheet = wb.get_sheet_by_name('layout')  # Must be a Sheet titled 'layout' !
sheet = wb.worksheets[0]  # first worksheet in the workbook
flds = []
callbacks = []
domenu = False


for rownum in range(3, sheet.max_row + 1):  # loop through each row

    flds.clear()  # clear list
    flds.append("nop")  # zero element not used
    # load up the flds list with this row's columns values
    for c in range(1, 11):  # columns align with list index
        val = sheet.cell(row=rownum, column=c).value
        if val is None:
            flds.append("")
        else:
            flds.append(val)

    # first check if processing menu
    if domenu is True:
        proc_menu_item()
        continue

    if flds[wgt].lower() == "begmenu":  # going to process a menu
        domenu = True
        prt("menubar = Menu(root)")  # the menu code starts here
        continue

    # Process this row/columns values

    print(flds[wgt])

    # These will be set to the formatted code or ""
    attribs = getAttrib(flds[owa])
    rowspan = getRowSpan(flds[rsp])
    colspan = getColSpan(flds[csp])
    sticky = getSticky(flds[sty])

    # BUTTON
    if flds[wgt].lower() == "button":
        line = "{0} = Button(self, text='{1}', command=self.{2}{3})"
        prt(line.format(flds[var], flds[txt], flds[com], attribs))
        callbacks.append(flds[com])
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))

    # LABEL
    elif flds[wgt].lower() == "label":
        if flds[com] != "":  # a StringVar was given
            prt("self." + flds[com] + " = StringVar()")
            line = "{0} = Label(self, text='{1}', textvariable=self.{2}{3})"
            prt(line.format(flds[var], flds[txt], flds[com], attribs))
            line = "{0}.grid(row={1}, column={2}{3}{4}{5})"
            prt(line.format(flds[var], flds[row],
                            flds[col], rowspan, colspan, sticky))
            line = "self.{}.set('{}')\n"
            prt(line.format(flds[com], flds[txt]))
        else:  # without StringVar
            line = "{0} = Label(self, text='{1}'{2})"
            prt(line.format(flds[var], flds[txt], attribs))
            line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
            prt(line.format(flds[var], flds[row],
                            flds[col], rowspan, colspan, sticky))

    # ENTRY
    elif flds[wgt].lower() == "entry":
        prt("self." + flds[com] + " = StringVar()")
        prt("# self." + flds[com] + ".trace(\"w\", self.eventHandler)")
        line = "{0} = Entry(self, textvariable=self.{1}{2})"
        prt(line.format(flds[var], flds[com], attribs))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))

    # TEXT
    elif flds[wgt].lower() == "text":
        line = "self.{0} = Text(self{1})"
        prt(line.format(flds[var], attribs))
        line = "self.{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
        line = '''
        # efont = Font(family="Helvetica", size=14)
        # self.EDITOR.configure(font=efont)
        # self.EDITOR.config(wrap = "word", # wrap = NONE
        #        undo = True, # Tk 8.4
        #        width = 80,
        #        tabs = (efont.measure(' ' * 4),))
        # self.EDITOR.focus()
        ## basic handler commands #
        # .get("1.0", END)
        # .delete("1.0", END)
        # .insert("1.0", "New text content ...")
        '''
        prt(line + "\n")

    # LIST
    elif flds[wgt].lower().startswith("list"):
        line = "self.{0} = Listbox(self, height=5{1})"
        prt(line.format(flds[var], attribs))
        rowspan = getRowSpan(flds[rsp])
        line = "self.{0}.grid(row={1}, column={2}{3}{4}{5})"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))

        line = '''
        # self.LISTBOX.bind("<Double-Button-1>", self.on_dblclick_list)
        # for i in range(100):
        #     self.LISTBOX.insert(i, str(i) + "Item")'''
        prt(line)

        line = '''
    ## Handler for List selection
    ## Make this a class method
    # def on_dblclick_list(self, event):
    #     list_item = self.LISTBOX.curselection()
    #     fp = self.LISTBOX.get(list_item[0])
    #     print(str(fp) + " --> " + str(list_item[0]) +
    #         " of " + str(self.LISTBOX.size()))
    #
    # FUNCS TO EDIT LISTBOX CONTENTS
    #
    # def delete_item(self):
    #     if self.listbox.curselection() == ():
    #         return # nothing selected
    #     print("Deleting: " + str(self.listbox.curselection()))
    #     self.listbox.delete(self.listbox.curselection())

    # def insert_item(self):
    #     if self.listbox.curselection() == ():
    #         return # nothing selected
    #     list_item = self.listbox.curselection()
    #     self.listbox.insert(list_item[0], self.txtfld.get())
    #     print("inserted at " + str(list_item[0]))
        '''
        prt(line + "\n")


    # VERT SCROLLBAR
    elif flds[wgt].lower() == "scrolly":
        line = "self.{0} = Scrollbar(self, orient=VERTICAL, command=self.{1}.yview)"
        if flds[com] == "":
            print("\n\nMISSING list object FOR SCROLLBAR WIDGET\n\n")
            sys.exit()
        prt(line.format(flds[var], flds[com]))
        line = "self.{0}.grid(row={1}, column={2}{3}{4}{5})  # use nse"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
        line = "self.{0}['yscrollcommand'] = self.{1}.set\n"
        prt(line.format(flds[com], flds[var]))

    # HORZ SCROLLBAR
    elif flds[wgt].lower() == "scrollx":
        line = "self.{0} = Scrollbar(self, orient=HORIZONTAL, command=self.{1}.xview)"
        if flds[com] == "":
            print("\n\nMISSING list/text object FOR SCROLLBAR WIDGET\n\n")
            sys.exit()
        prt(line.format(flds[var], flds[com]))
        line = "self.{0}.grid(row={1}, column={2}{3}{4}{5})"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
        line = "self.{0}['xscrollcommand'] = self.{1}.set\n"
        prt(line.format(flds[com], flds[var]))

    # CHECK BOX
    elif flds[wgt].lower().startswith("check"):
        prt("self.{0} = IntVar()".format(flds[com]))
        line = "{0} = Checkbutton(self, variable=self.{1}, text='{2}'{3})"
        prt(line.format(flds[var], flds[com], flds[txt], attribs))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
    # RADIO BUTTON
    elif flds[wgt].lower().startswith("radio"):
        prt("self." + flds[com] +
            " = StringVar() # USE ONE VAR PER GROUP OF BUTTONS")
        line = "{0} = Radiobutton(self, variable=self.{1}, value='{2}', text='{2}'{4})"
        prt(line.format(flds[var], flds[com], flds[txt], flds[txt], attribs))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
    # SPIN BOX
    elif flds[wgt].lower().startswith("spin"):
        prt("self." + flds[com] + " = StringVar()")
        line = "{0} = Spinbox(self, textvariable=self.{1}{2})"
        prt(line.format(flds[var], flds[com], attribs))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
    # OPTION MENU
    elif flds[wgt].lower().startswith("option"):
        prt("optionlist = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')")
        prt("self." + flds[com] + " = StringVar()")
        prt("self." + flds[com] + ".set(optionlist[0])")
        line = "{0} = OptionMenu(self, self.{1}, *optionlist)"
        prt(line.format(flds[var], flds[com]))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))

    # COMBOBOX (from tkinter.ttk import Combobox)
    elif flds[wgt].lower().startswith("combo"):
        prt("self." + flds[com] + " = StringVar()")
        line = "{0} = Combobox(self, textvariable=self.{1}{2})"
        prt(line.format(flds[var], flds[com], attribs))
        line = "{0}['values'] = ('value1', 'value2', 'value3')"
        prt(line.format(flds[var]))
        prt("# COMBO.bind('<<ComboboxSelected>>', self.ONCOMBOSELECT)")
        prt("%s.current(0)" % flds[var])
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))

    # PROGRESSBAR
    elif flds[wgt].lower().startswith("prog"):
        line = "{0} = Progressbar(self, orient='horizontal', mode='indeterminate', maximum=20 {1})"
        prt(line.format(flds[var], attribs))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
        line = ("# {0}.start() | {0}.stop() | {0}.grid_forget() | {0}.grid(self, ...) \n")
        prt(line.format(flds[var], flds[var], flds[var], flds[var]))

    # NOTEBOOK
    elif flds[wgt].lower().startswith("notebook"):
        line = "{0} = Notebook(self{1})"
        prt(line.format(flds[var], attribs))
        line = "tab1 = Frame({0}, width=200, height=200)"
        prt(line.format(flds[var]))
        line = "tab2 = Frame({0})"
        prt(line.format(flds[var]))
        line = "tab3 = Frame({0})"
        prt(line.format(flds[var]))
        line = "{0}.add(tab1, text = 'tab 1')"
        prt(line.format(flds[var]))
        line = "{0}.add(tab2, text = 'tab 2')"
        prt(line.format(flds[var]))
        line = "{0}.add(tab3, text = 'tab 3')"
        prt(line.format(flds[var]))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))
        line = '''
        Button(tab1, text='Exit',
               command=root.destroy).grid(row=1, column=1, padx=100, pady=100)
        Label(tab2, text='tab 2').pack(padx=50, pady=50)
        Label(tab3, text='tab 3').pack(padx=50, pady=50)
        '''
        prt(line + "\n")

    # FRAMES
    elif flds[wgt].lower().startswith("frame"):
        line = '''
        # lframe = LabelFrame(self, text="text",
        #                     width=100, height=100)
        # lframe.grid(row=1, column=1, sticky='nsew')
        #
        # fram = Frame(self, width=100, height=100)
        # fram.grid(row=1, column=1, sticky='nsew')
        '''
        prt(line + "\n")

    # MESSAGEBOX
    elif flds[wgt].lower() == "messagebox":
        line = '''
        # from tkinter import messagebox
        # messagebox.showerror("Error", "Error message")
        # messagebox.showwarning("Warning","Warning message")
        # messagebox.showinfo("Information","Informative message")
        # messagebox.askokcancel('Message title', 'Message content')
        # messagebox.askretrycancel('Message title', 'Message content')
        #     ok, yes, retry returns TRUE
        #     no, cancel returns FALSE
        '''
        prt(line + "\n")

    # FILEDIALOG
    elif flds[wgt].lower().startswith("file"):
        line = '''
        # from tkinter import filedialog
        # filename =  filedialog.askopenfilename(initialdir = "/",
        #             title = "Open file",
        #             filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        # filename = filedialog.asksaveasfilename(initialdir = "/",
        #             title = "Save file",
        #             filetypes = (("jpeg files","*.jpg"),("all files","*.*")))'''
        prt(line + "\n")

    # MESSAGE
    elif flds[wgt].lower() == "message":
        line = "{0} = Message(self, text='{1}'{2})"
        prt(line.format(flds[var], flds[txt], attribs))
        line = "{0}.grid(row={1}, column={2}{3}{4}{5})\n"
        prt(line.format(flds[var], flds[row],
                        flds[col], rowspan, colspan, sticky))

    # POPUP MENU
    elif flds[wgt].lower().startswith("pop"):
        line = '''
        # self.popup_menu = Menu(self, tearoff = 0)
        # self.popup_menu.add_command(label = "Copy",
        #                             command = lambda:self.function(1))
        # self.popup_menu.add_command(label = "Paste",
        #                             command = lambda:self.function(2))
        # self.popup_menu.add_separator()
        # self.popup_menu.add_command(label = "say bye", command = exit)
        # self.txt.bind("<Button-3>",self.do_popup)

    # def do_popup(self,event):
    #     try:
    #         self.popup_menu.tk_popup(event.x_root,
    #                                  event.y_root)
    #     finally:
    #         self.popup_menu.grab_release()
        '''
        prt(line + "\n")

    # CLIPBOARD ACCESS
    elif flds[wgt].lower().startswith("clip"):
        line = '''
    # def clipbrd(self,n):
    #     if n == 1:  # Copy
    #         pyperclip.copy(self.txt.selection_get())
    #     else:
    #         # n == 2:  # Paste
    #         inx = self.txt.index(INSERT)
    #         self.txt.insert(inx, pyperclip.paste())
        '''
        prt(line + "\n")

    # GEOMETRY FOR WINDOW
    elif flds[wgt].lower().startswith("geo"):
        line = "root.geometry(\"%s\")" % (flds[var])
        prt(line + "\n")

    else:
        if flds[wgt].startswith("Widget"):
            pass
        else:
            prt("\nNUNRECOGNIZED WIDGET IDENTIFIER: " + flds[wgt] + "\n\n")

fout = open(args.outfile, "w")

# location of master template
fin = open(TPLPATH + "tkauto_tpl.py", "r")

for line in fin:
    if line.find("INSERT TKAUTO OUTPUT") > 0:
        fout.write(sout)
        #  insert the callbacks
        for item in callbacks:
            fout.write("    def %s(self):\n" % (item))
            fout.write("        ''' docstring '''\n\n")
    else:
        fout.write(line)


fout.close()
fin.close()
print("\n\nFind new script in 'output.py'\n")
print("Some Widgets may need futher definition\n\n")
