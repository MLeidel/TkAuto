# TkAuto

TkAuto is a system for rapidly designing and coding a GUI desktop
program using Python and tkinter.  

TkAuto uses an Excel spreadsheet, a Python-tkinter template, and  
the tkinter grid layout to help get your design coded up quickly.


## Overview

![overview](images/tkauto.jpg)
 

## Setup Using Spreadsheet

![Spreadsheet](images/layout1.png)

`layout_tpl.xlsx' is a spreadsheet used to indicate which widgets  
your application will use, where they'll be located, and some of  
their essential options. Save-As to a different name.

Some columns are commented to further define their purpose.  
Here's a little more already filled in.  

![Spreadsheet](images/layout2.png)

This sheet to serves as a guide for filling in the cells for each widget.

![Spreadsheet](images/layout3.png)

This sheet called `menus` is an example of how to fill out a menu system  
in the `layout` sheet.

![Spreadsheet](images/layout4.png)

## Dev Process in a Nutshell
1. **Create a layout with Excel and save to `layout.xlsx`**  
2. **Run `python tkauto.py layout.xlsx` - by default this will create `output.py`**  
3. **Make any corrections and add business logic to `output.py`**

Tkauto reads in a template file called `tkauto_tpl.py` along with the layout.xlsx file.  
`tkauto.py` produces an output script called `output.py`.  
When `output.py` is satisfactory you rename it and start editing the code  
to finish the application.  

Usually you will not run `tkauto.py` more than a couple time. If you need to add  
some widgets, or options, usually you can just edit them in.  
Sometimes you may want to run `tkauto.py` several times.  

**_BE CAREFUL_**  
  RUNNING `tkauto.py` A SECOND TIME OVER-WRITES THE `output.py` FILE.  

```
usage: tkauto.py [-h] [-o OUTFILE] filename

tkauto build Python tkinter GUI

positional arguments:
  filename    Excel (xlsx) file to use as input

optional arguments:
  -h, --help  show this help message and exit
  -o OUTFILE  output Python file

```

## Working with the generated source code

This process is only one step away from coding everything by hand.  
I've found that thinking in "GRID" fashion helps me speed up the  
prototyping and development process. I always start on paper to draw  
in a ruff sketch of what the GUI should look like. This gives me an idea  
of how the grid will work. From there it is a quick hop to the spreadsheet  
to begin filling the essential tkinter elements. After one, two, or three  
generations using tkauto I can usually keep the output and begin final editing.  
Since the tkinter-design-code is bound in together with the business logic  
any further changes to the tkinter-design-code must take place in the source file itself.

Unless one has been coding in tkinter for many years, and tkinter syntax has become  
second nature, this tkauto process does serve its goal of speeding up Python-Tkinter  
application development.  

Currently these widgits are supported:  
button
entry
label
scrollx
scrolly
list
text
check
radio  
spin
options
combo
notebook
geometry
progress  
beginmenu endmenu
messagebox
filedialog
popup
clip


---
