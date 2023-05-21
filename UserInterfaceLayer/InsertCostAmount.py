from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.WicDAL import CrudWIC
from Model.AmountModel import AmountsModel
from BusinessLogicLayer.AmountBLL import AmountLogic
from BusinessLogicLayer.MenuItemInfo import menuItems

class costAmount:
    def formLoad(self):
        # -------<< Insert Cost Amount Method >> :
        def insertAmount():
            amount = amountValue.get()
            cost = costItemValue.get()
            type = 'C'
            x = AmountsModel(Price=amount, WicId=cost, UserId=1)
            items = AmountLogic()
            message = items.validateForm(Amount=x, Type=type)
            fillComboBox()
            labelMessage = Label(costAmountFrame, text=message, fg='black', font=('Calibri', 10, 'bold'),
                                 bg='#F3E5F5')
            labelMessage.grid(row=5, column=0, padx=10, pady=5, columnspan=2)
            labelMessage.after(1500, lambda: labelMessage.destroy())

        # -------<< Empty Entries Method >> :
        def fillComboBox():
            entAmountValue.delete(0, END)
            entCostItemValue.delete(0, END)
            a = CrudWIC()
            costItemList = a.getAllSingleTypeItems(wicType='C')
            entCostItemValue['values'] = costItemList

        # region Form
        costAmountForm = Tk()
        costAmountForm.title('Accounting Book - Cost Amount')
        positionRight = int(costAmountForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(costAmountForm.winfo_screenheight() / 2 - 300 / 2)
        costAmountForm.geometry("+{}+{}".format(positionRight, positionDown))
        costAmountForm.resizable(0, 0)
        # costAmountForm.geometry('400x180')
        costAmountForm.iconbitmap('Files/Images/wallet.ico')
        costAmountForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=costAmountForm)
        # endregion

        # region CostAmountFrame
        costAmountFrame = LabelFrame(costAmountForm, text=' Cost : ', bg='#F3E5F5')
        costAmountFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region CostItem
        # -------<< Cost Item Label >> :
        lblCostItem = Label(costAmountFrame, text='Cost Name: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblCostItem.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        # -------<< Cost Item Entry >> :
        costItemValue = StringVar()
        entCostItemValue = Combobox(costAmountFrame, width=20, font=('Calibri', 10), textvariable=costItemValue,
                                 state="readonly")
        entCostItemValue.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        # endregion

        # region Amount
        # -------<< Amount Label >> :
        lblCostAmount = Label(costAmountFrame, text='Amount: ', fg='Indigo', font=('Calibri', 12, 'bold'), bg='#F3E5F5')
        lblCostAmount.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        # -------<< Amount Entry >> :
        amountValue = StringVar()
        entAmountValue = Entry(costAmountFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                               textvariable=amountValue)
        entAmountValue.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        fillComboBox()
        # endregion

        # region Button
        # -------<< Submit Button >> :
        buttonRegister = Button(costAmountFrame, text='Register Amount', width=14, height=1,
                                font=('Calibri', 10, 'bold'), bg='#FFFFFF', fg='#33691E', command=insertAmount)
        buttonRegister.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        costAmountForm.mainloop()