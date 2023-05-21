from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.WicDAL import CrudWIC
from Model.WicModel import WicModel
from BusinessLogicLayer.WicBLL import checkFormEntry
from BusinessLogicLayer.MenuItemInfo import menuItems

class walletItems:
    def formLoad(self):
        # -------<< Insert Wallet Items Method >> :
        def insertWalletItem():
            Name = WalletItemValue.get()
            Parent = ParentItemName.get()
            Type = 'W'
            x = WicModel(Name=Name, ParentId=Parent, Type=Type, UserId=1)
            items = checkFormEntry()
            message = items.CheckUniqueName(wic=x, wicType=x.type)
            fillComboBox()
            labelMessage = Label(walletItemFrame, text=message, fg='black', font=('Calibri', 10, 'bold'),
                                 bg='#F3E5F5')
            labelMessage.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
            labelMessage.after(1500, lambda: labelMessage.destroy())

        # -------<< Empty Entries Method >> :
        def fillComboBox():
            entWalletItem.delete(0, END)
            entParentItem.delete(0, END)
            a = CrudWIC()
            ParentList = a.getAllSingleTypeItems(wicType='W')
            entParentItem['values'] = ParentList

        # region Form
        walletForm = Tk()
        walletForm.title('Accounting Book - Wallet Items')
        positionRight = int(walletForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(walletForm.winfo_screenheight() / 2 - 300 / 2)
        walletForm.geometry("+{}+{}".format(positionRight, positionDown))
        walletForm.resizable(0, 0)
        # walletForm.geometry('400x180')
        walletForm.iconbitmap('Files/Images/wallet.ico')
        walletForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=walletForm)
        # endregion

        # region WalletItemFrame
        walletItemFrame = LabelFrame(walletForm, text=' Wallet Items : ', bg='#F3E5F5')
        walletItemFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region WalletItem
        # -------<< Wallet Item Label >> :
        lblWalletItem = Label(walletItemFrame, text='Item Name: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblWalletItem.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        # -------<< Wallet Item Entry >> :
        WalletItemValue = StringVar()
        entWalletItem = Entry(walletItemFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                            textvariable=WalletItemValue)
        entWalletItem.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        # endregion

        # region WalletParentItem
        # -------<< Wallet Parent Item Label >> :
        lblParentItem = Label(walletItemFrame, text='Parent: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblParentItem.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        # -------<< Wallet Parent Item Entry >> :
        ParentItemValue = StringVar()
        entParentItem = Combobox(walletItemFrame, width=20, font=('Calibri', 10), textvariable=ParentItemValue,
                                 state="readonly")
        if ParentItemValue == None:
            ParentItemName = ''
        else:
            ParentItemName = ParentItemValue
        fillComboBox()
        entParentItem.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        # endregion

        # region Button
        # -------<< Submit Button >> :
        buttonRegister = Button(walletItemFrame, text='Register Item', width=14, height=1, font=('Calibri', 10, 'bold'),
                                bg='#FFFFFF', fg='#33691E', command=insertWalletItem)
        buttonRegister.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        walletForm.mainloop()