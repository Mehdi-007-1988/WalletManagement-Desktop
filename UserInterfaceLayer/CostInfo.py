from tkinter import *
from tkinter.ttk import Combobox
from DataAccessLayer.WicDAL import CrudWIC
from Model.WicModel import WicModel
from BusinessLogicLayer.WicBLL import checkFormEntry
from BusinessLogicLayer.MenuItemInfo import menuItems

class costItems:
    def formLoad(self):
        # -------<< Insert Cost Items Method >> :
        def insertCostItem():
            Name = CostItemValue.get()
            Parent = ParentItemName.get()
            Type = 'C'
            x = WicModel(Name=Name, ParentId=Parent, Type=Type, UserId=1)
            items = checkFormEntry()
            message = items.CheckUniqueName(wic=x, wicType=x.type)
            fillComboBox()
            labelMessage = Label(costItemFrame, text=message, fg='black', font=('Calibri', 10, 'bold'),
                                 bg='#F3E5F5')
            labelMessage.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
            labelMessage.after(1500, lambda: labelMessage.destroy())

        # -------<< Empty Entries Method >> :
        def fillComboBox():
            entCostItem.delete(0, END)
            entParentItem.delete(0, END)
            a = CrudWIC()
            ParentList = a.getAllSingleTypeItems(wicType='C')
            entParentItem['values'] = ParentList

        # region Form
        costForm = Tk()
        costForm.title('Accounting Book - Cost Items')
        positionRight = int(costForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(costForm.winfo_screenheight() / 2 - 300 / 2)
        costForm.geometry("+{}+{}".format(positionRight, positionDown))
        costForm.resizable(0, 0)
        # costForm.geometry('400x180')
        costForm.iconbitmap('Files/Images/wallet.ico')
        costForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=costForm)
        # endregion

        # region CostItemFrame
        # -------<< Coste Item Frame >> :
        costItemFrame = LabelFrame(costForm, text=' Cost Items : ', bg='#F3E5F5')
        costItemFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region CostItem
        # -------<< Cost Item Label >> :
        lblCostItem = Label(costItemFrame, text='Item Name: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblCostItem.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        # -------<< Cost Item Entry >> :
        CostItemValue = StringVar()
        entCostItem = Entry(costItemFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                            textvariable=CostItemValue)
        entCostItem.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky='w')
        # endregion

        # region CostParentItem
        # -------<< Cost Parent Item Label >> :
        lblParentItem = Label(costItemFrame, text='Parent: ', fg='Indigo', font=('Calibri', 12, 'bold'),
                              bg='#F3E5F5')
        lblParentItem.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        # -------<< Cost Parent Item Entry >> :
        ParentItemValue = StringVar()
        entParentItem = Combobox(costItemFrame, width=20, font=('Calibri', 10), textvariable=ParentItemValue,
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
        buttonRegister = Button(costItemFrame, text='Register Item', width=14, height=1, font=('Calibri', 10, 'bold'),
                                bg='#FFFFFF', fg='#33691E', command=insertCostItem)
        buttonRegister.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        costForm.mainloop()