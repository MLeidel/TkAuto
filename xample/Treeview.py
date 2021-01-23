from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk

csvdata = [
    ("IP","CODE","NAME","CITY","LAT","LON","KNOWN"),
    ("85.167.251.194","NO","Norway","Bergen",60.39299,5.32415,"YES"),
    ("217.170.205.14","NO","Norway","Oslo",59.91273,10.74609,"YES"),
    ("203.99.60.214","PK","Pakistan","Islamabad",33.72148,73.04329,"YES"),
    ("201.226.239.98","PA","Panama","Panama",8.9936,-79.51973,"YES"),
    ("190.128.239.146","PY","Paraguay","Fernando de la Mora",-25.31667,-57.6,"YES"),
    ("203.177.71.253","PH","Philippines","Davao City",7.07306,125.61278,"YES"),
    ("122.53.59.59","PH","Philippines","Mandaluyong City",14.5832,121.0409,"YES"),
    ("83.12.171.68","PL","Poland","Nowy Sacz",49.62177,20.69705,"YES"),
    ("83.15.127.73","PL","Poland","Gdansk",54.35205,18.64637,"YES"),
    ("62.28.217.62","PT","Portugal","Lisbon",38.71667,-9.13333,"YES"),
    ("195.254.135.76","RO","Romania","Craiova",44.31667,23.8,"NO")
]

root = Tk()


table = Treeview(root)

table["columns"]=csvdata[0]
table.column("#0", width=0, stretch=NO)  # phantom column
table.heading("#0", text="")

# Column Headings (tuple 0 of csvdata)
x = 0
for h in csvdata[0]:
    table.column(str(x), width=128)
    table.heading(str(x), text=h)
    x += 1

# Row data
x = 1
for row in csvdata[1:]:
    table.insert("", "end", iid=x, values=(row))
    x += 1

table.pack()
root.mainloop()
