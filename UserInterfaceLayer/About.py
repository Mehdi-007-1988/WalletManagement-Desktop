from tkinter import *
from BusinessLogicLayer.MenuItemInfo import menuItems

class about:
    def formLoad(self):
        # region Form
        aboutForm = Tk()
        aboutForm.title('Accounting Book - About')
        positionRight = int(aboutForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(aboutForm.winfo_screenheight() / 2 - 300 / 2)
        aboutForm.geometry("+{}+{}".format(positionRight, positionDown))
        aboutForm.resizable(0, 0)
        # aboutForm.geometry('400x180')
        aboutForm.iconbitmap('Files/Images/wallet.ico')
        aboutForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=aboutForm)
        # endregion

        # region AboutFrame
        aboutFrame = LabelFrame(aboutForm, bg='#F3E5F5')
        aboutFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region About
        # -------<< About Text >> :
        version = "Version: 1.0.0"
        date = "1402/02/30"
        name = "-------------By Mehdi Khodarahmi"
        # -------<< Versio Label >> :
        versionLabel = Label(aboutFrame, text=version, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10, 'bold'))
        versionLabel.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        # -------<< Date Label >> :
        dateLabel = Label(aboutFrame, text=date, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10, 'bold'))
        dateLabel.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        # -------<< Name Label >> :
        nameLabel = Label(aboutFrame, text=name, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10, 'bold'))
        nameLabel.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        # endregion

        aboutForm.mainloop()
