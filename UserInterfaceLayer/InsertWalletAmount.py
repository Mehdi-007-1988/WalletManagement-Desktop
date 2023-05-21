from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.WicDAL import CrudWIC
from Model.AmountModel import AmountsModel
from BusinessLogicLayer.AmountBLL import AmountLogic
from BusinessLogicLayer.MenuItemInfo import menuItems

class walletAmount:
    def formLoad(self):
        # -------<< Insert Wallet Amount Method >> :
        def insertAmount():
            amount = AmountValue.get()
            wallet = WalletItemValue.get()
            type = 'W'
            x = AmountsModel(Price=amount, WicId=wallet, UserId=1)
            items = AmountLogic()
            message = items.validateForm(Amount=x, Type=type)
            fillComboBox()
            labelMessage = Label(walletAmountFrame, text=message, fg='black', font=('Calibri', 10, 'bold'),
                                 bg='#F3E5F5')
            labelMessage.grid(row=5, column=0, padx=10, pady=5, columnspan=2)
            labelMessage.after(1500, lambda: labelMessage.destroy())

        # -------<< Empty Entries Method >> :
        def fillComboBox():
            entAmountValue.delete(0, END)
            entWalletItemValue.delete(0, END)
            a = CrudWIC()
            walletItemList = a.getAllSingleTypeItems(wicType='W')
            entWalletItemValue['values'] = walletItemList

        # region Form
        walletAmountForm = Tk()
        walletAmountForm.title('Accounting Book - Wallet Amount')
        positionRight = int(walletAmountForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(walletAmountForm.winfo_screenheight() / 2 - 300 / 2)
        walletAmountForm.geometry("+{}+{}".format(positionRight, positionDown))
        walletAmountForm.resizable(0, 0)
        # walletAmountForm.geometry('400x180')
        walletAmountForm.iconbitmap('Files/Images/wallet.ico')
        walletAmountForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=walletAmountForm)
        # endregion

        # region WalletAmountFrame
        walletAmountFrame = LabelFrame(walletAmountForm, text=' Wallet : ', bg='#F3E5F5')
        walletAmountFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region WalletItem
        # -------<< Wallet Item Label >> :
        lblWalletItem = Label(walletAmountFrame, text='Wallet Name: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblWalletItem.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        # -------<< Wallet Item Entry >> :
        WalletItemValue = StringVar()
        entWalletItemValue = Combobox(walletAmountFrame, width=20, font=('Calibri', 10), textvariable=WalletItemValue,
                                 state="readonly")
        entWalletItemValue.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        # endregion

        # region Amount
        # -------<< Amount Label >> :
        lblWalletAmount = Label(walletAmountFrame, text='Amount: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                                bg='#F3E5F5')
        lblWalletAmount.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        # -------<< Amount Entry >> :
        AmountValue = StringVar()
        entAmountValue = Entry(walletAmountFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                              textvariable=AmountValue)
        entAmountValue.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        fillComboBox()
        # endregion

        # region Button
        # -------<< Submit Button >> :
        buttonRegister = Button(walletAmountFrame, text='Register Amount', width=14, height=1, font=('Calibri', 10, 'bold'),
                                bg='#FFFFFF', fg='#33691E', command=insertAmount)
        buttonRegister.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        walletAmountForm.mainloop()