import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

app = ttk.Window()
colors = app.style.colors

coldata = [
    # {"text": "LicenseNumber", "stretch": False},
    # "CompanyName",
    # {"text": "UserCount", "stretch": False},
    # {"text": "key", "stretch": False},
    " key "
]

rowdata = [
    ('IzzyCo',),
    ('Kimdee',),
    ('Farmadding',)
]

# coldata = [
#     {"text": "LicenseNumber", "stretch": False},
#     "CompanyName",
#     {"text": "UserCount", "stretch": False},
# ]

# rowdata = [
#     ('A123', 'IzzyCo', 12),
#     ('A136', 'Kimdee Inc.', 45),
#     ('A158', 'Farmadding Co.', 36)
# ]


dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=False,
    searchable=False,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)


def showit():
    print(dt.get_rows(selected=True).view())

btn = ttk.Button(text="select", command=showit)
btn.pack(side=RIGHT, padx=5, pady=10)

app.mainloop()
