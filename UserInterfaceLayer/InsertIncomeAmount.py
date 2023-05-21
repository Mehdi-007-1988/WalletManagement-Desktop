from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.WicDAL import CrudWIC
from Model.AmountModel import AmountsModel
from BusinessLogicLayer.AmountBLL import AmountLogic
from BusinessLogicLayer.MenuItemInfo import menuItems

class incomeAmount:
    def formLoad(self):
        # -------<< Insert Income Amount Method >> :
        def insertAmount():
            amount = amountValue.get()
            income = incomeItemValue.get()
            type = 'I'
            x = AmountsModel(Price=amount, WicId=income, UserId=1)
            items = AmountLogic()
            message = items.validateForm(Amount=x, Type=type)
            fillComboBox()
            labelMessage = Label(incomeAmountFrame, text=message, fg='black', font=('Calibri', 10, 'bold'),
                                 bg='#F3E5F5')
            labelMessage.grid(row=5, column=0, padx=10, pady=5, columnspan=2)
            labelMessage.after(1500, lambda: labelMessage.destroy())

        # -------<< Empty Entries Method >> :
        def fillComboBox():
            entAmountValue.delete(0, END)
            entIncomeItemValue.delete(0, END)
            a = CrudWIC()
            incomeItemList = a.getAllSingleTypeItems(wicType='I')
            entIncomeItemValue['values'] = incomeItemList

        # region Form
        incomeAmountForm = Tk()
        incomeAmountForm.title('Accounting Book - Income Amount')
        positionRight = int(incomeAmountForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(incomeAmountForm.winfo_screenheight() / 2 - 300 / 2)
        incomeAmountForm.geometry("+{}+{}".format(positionRight, positionDown))
        incomeAmountForm.resizable(0, 0)
        # incomeAmountForm.geometry('400x180')
        incomeAmountForm.iconbitmap('Files/Images/wallet.ico')
        incomeAmountForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=incomeAmountForm)
        # endregion

        # region IncomeAmountFrame
        incomeAmountFrame = LabelFrame(incomeAmountForm, text=' Income : ', bg='#F3E5F5')
        incomeAmountFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region IncomeItem
        # -------<< Income Item Label >> :
        lblIncomeItem = Label(incomeAmountFrame, text='Income Name: ', fg='Indigo', font=('Calibri', 10, 'bold'),
                              bg='#F3E5F5')
        lblIncomeItem.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        # -------<< Income Item Entry >> :
        incomeItemValue = StringVar()
        entIncomeItemValue = Combobox(incomeAmountFrame, width=20, font=('Calibri', 10), textvariable=incomeItemValue,
                                      state="readonly")
        entIncomeItemValue.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        # endregion

        # region Amount
        # -------<< Amount Label >> :
        lblIncomeAmount = Label(incomeAmountFrame, text='Amount: ', fg='Indigo', font=('Calibri', 10, 'bold'),
                                bg='#F3E5F5')
        lblIncomeAmount.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        # -------<< Amount Entry >> :
        amountValue = StringVar()
        entAmountValue = Entry(incomeAmountFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                               textvariable=amountValue)
        entAmountValue.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        fillComboBox()
        # endregion

        # region Button
        # -------<< Submit Button >> :
        buttonRegister = Button(incomeAmountFrame, text='Register Amount', width=14, height=1,
                                font=('Calibri', 10, 'bold'),  bg='#FFFFFF', fg='#33691E', command=insertAmount)
        buttonRegister.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        incomeAmountForm.mainloop()