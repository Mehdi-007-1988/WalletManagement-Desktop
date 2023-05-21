from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.WicDAL import CrudWIC
from Model.WicModel import WicModel
from BusinessLogicLayer.WicBLL import checkFormEntry
from BusinessLogicLayer.MenuItemInfo import menuItems

class incomeItems:
    def formLoad(self):
        # -------<< Insert Income Item Method >> :
        def insertIncomeItem():
            Name = IncomeItemValue.get()
            Parent = ParentItemName.get()
            Type = 'I'
            x = WicModel(Name=Name, ParentId=Parent, Type=Type, UserId=1)
            items = checkFormEntry()
            message = items.CheckUniqueName(wic=x, wicType=x.type)
            fillComboBox()
            labelMessage = Label(incomeItemFrame, text=message, fg='black', font=('Calibri', 10, 'bold'),
                                 bg='#F3E5F5')
            labelMessage.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
            labelMessage.after(1500, lambda: labelMessage.destroy())

        # -------<< Empty Entries Method >> :
        def fillComboBox():
            entIncomeItem.delete(0, END)
            entParentItem.delete(0, END)
            a = CrudWIC()
            ParentList = a.getAllSingleTypeItems(wicType='I')
            entParentItem['values'] = ParentList

        # region Form
        incomeForm = Tk()
        incomeForm.title('Accounting Book - Income Items')
        positionRight = int(incomeForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(incomeForm.winfo_screenheight() / 2 - 300 / 2)
        incomeForm.geometry("+{}+{}".format(positionRight, positionDown))
        incomeForm.resizable(0, 0)
        # incomeForm.geometry('400x180')
        incomeForm.iconbitmap('Files/Images/wallet.ico')
        incomeForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=incomeForm)
        #endregion

        # region IncomeItemFrame
        # -------<< Income Item Frame >> :
        incomeItemFrame = LabelFrame(incomeForm, text=' Income Items : ', bg='#F3E5F5')
        incomeItemFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region IncomeItem
        # -------<< Income Item Label >> :
        lblIncomeItem = Label(incomeItemFrame, text='Item Name: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblIncomeItem.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        # -------<< Income Item Entry >> :
        IncomeItemValue = StringVar()
        entIncomeItem = Entry(incomeItemFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                            textvariable=IncomeItemValue)
        entIncomeItem.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        # endregion

        # region IncomeParentItem
        # -------<< Income Parent Item Label >> :
        lblParentItem = Label(incomeItemFrame, text='Parent: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblParentItem.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        # -------<< Income Parent Item Entry >> :
        ParentItemValue = StringVar()
        entParentItem = Combobox(incomeItemFrame, width=20, font=('Calibri', 10), textvariable=ParentItemValue,
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
        buttonRegister = Button(incomeItemFrame, text='Register Item', width=14, height=1, font=('Calibri', 10, 'bold'),
                                bg='#FFFFFF', fg='#33691E', command=insertIncomeItem)
        buttonRegister.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        incomeForm.mainloop()