from tkinter import *
from DataAccessLayer.AmountDAL import CrudAmount
from BusinessLogicLayer.MenuItemInfo import menuItems

class totalReport:
    def formLoad(self):
        totalReportAmountForm = Tk()
        totalReportAmountForm.title('Accounting Book - Report')
        positionRight = int(totalReportAmountForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(totalReportAmountForm.winfo_screenheight() / 2 - 300 / 2)
        totalReportAmountForm.geometry("+{}+{}".format(positionRight, positionDown))
        totalReportAmountForm.resizable(0, 0)
        # totalReportAmountForm.geometry('400x180')
        totalReportAmountForm.iconbitmap('Files/Images/wallet.ico')
        totalReportAmountForm.configure(bg='#F3E5F5')

        # region Menu :
        menu = menuItems()
        menu.displayMenu(pageForm=totalReportAmountForm)
        # endregion

        x = CrudAmount()

        totalReportFrame = LabelFrame(totalReportAmountForm, bg='#F3E5F5')
        totalReportFrame.grid(row=1, column=0, padx=20, pady=10)

        # -------<< Wallet Amount >> :
        totalWalletAmounts = x.selectSumOfAmounts(wicType='W')
        totalReportWalletLabel = Label(totalReportFrame, text=' Total Wallet Amount : ', fg='Indigo',
                            font=('Calibri', 12, 'bold'), bg='#F3E5F5')
        totalReportWalletLabel.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        totalReportWalletValue = Label(totalReportFrame,fg='Green', font=('Calibri', 10, 'bold'), bg='#F3E5F5',
                                       text=str('{:,}'.format(totalWalletAmounts)) + "  IRR",)
        totalReportWalletValue.grid(row=2, column=1, padx=10, pady=5, sticky='e')

        # -------<< Income Amount >> :
        totalIncomeAmounts = x.selectSumOfAmounts(wicType='I')
        totalReportIncomeLabel = Label(totalReportFrame, text=' Total Income Amount : ', fg='Indigo',
                                       font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        totalReportIncomeLabel.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        totalReportIncomeValue = Label(totalReportFrame,font=('Calibri', 10, 'bold'), bg='#F3E5F5', fg='Blue',
                                       text=str('{:,}'.format(totalIncomeAmounts)) + "  IRR")
        totalReportIncomeValue.grid(row=4, column=1, padx=10, pady=5, sticky='e')

        # -------<< Cost Amount >> :
        totalCostAmounts = x.selectSumOfAmounts(wicType='C')
        totalReportCostLabel = Label(totalReportFrame, text=' Total Cost Amount : ', fg='Indigo',
                                       font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        totalReportCostLabel.grid(row=6, column=0, padx=10, pady=5, sticky='w')

        totalReportCostValue = Label(totalReportFrame,font=('Calibri', 10, 'bold'), bg='#F3E5F5',
                                     text=str('{:,}'.format(totalCostAmounts)) + "  IRR", fg='Red')
        totalReportCostValue.grid(row=6, column=1, padx=10, pady=5, sticky='e')

        totalReportAmountForm.mainloop()