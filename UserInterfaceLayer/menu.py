from tkinter import *
from BusinessLogicLayer.MenuItemInfo import MenuItems

def displayMenu(pageForm):
    MenuBar = Menu(pageForm)
    pageForm.config(menu=MenuBar, bg='#F3E5F5')

    fileMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
    MenuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Profile")
    fileMenu.add_command(label="About")
    fileMenu.add_command(label="Exit")

    dataMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
    MenuBar.add_cascade(label="Data", menu=dataMenu)
    dataMenu.add_command(label="Insert Data")

    reportMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
    MenuBar.add_cascade(label="Reports", menu=reportMenu)
    reportMenu.add_command(label="Wallet Report")
    reportMenu.add_command(label="Income Report")
    reportMenu.add_command(label="Cost Report")
    reportMenu.add_command(label="Total Report")

    editMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
    MenuBar.add_cascade(label="Basic Info", menu=editMenu)
    editMenu.add_command(label="Wallet Items")
    editMenu.add_command(label="Income Items")
    editMenu.add_command(label="Cost Items")