from tkinter import *
from BusinessLogicLayer.MenuItemInfo import menuItems

class homeForm:
    def formLoad(self):
        # region Form
        homeForm = Tk()
        homeForm.title('Accounting Book - Login')
        homeForm.geometry('350x180')
        homeForm.iconbitmap('Files/Images/wallet.ico')
        homeForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=homeForm)
        #endregion

        # region Info
        lblUserName = Label(homeForm, text='hi: ', fg='Indigo', font=('Calibri', 12, 'bold'), bg='#F3E5F5')
        lblUserName.grid(row=0, column=0)
        # endregion

        homeForm.mainloop()
