from tkinter import *

class menuItems:
    def displayMenu(self, pageForm: Tk):
        menuBar = Menu(pageForm)
        pageForm.config(menu=menuBar, bg='#F3E5F5')

        fileMenu = Menu(menuBar, tearoff=0, font=('Calibri', 10))
        menuBar.add_cascade(label="File", menu=fileMenu)
        # fileMenu.add_command(label="Profile")
        fileMenu.add_command(label="About", command=lambda: self.aboutMenu(CloseForm=pageForm))
        fileMenu.add_command(label="Exit", command=lambda: self.exitMenu(CloseForm=pageForm))

        dataMenu = Menu(menuBar, tearoff=0, font=('Calibri', 10))
        menuBar.add_cascade(label="Data", menu=dataMenu)
        dataMenu.add_command(label="Insert Wallet Data",
                             command=lambda: self.insertWalletAmountMenu(CloseForm=pageForm))
        dataMenu.add_command(label="Insert Income Data",
                             command=lambda: self.insertIncomeAmountMenu(CloseForm=pageForm))
        dataMenu.add_command(label="Insert Cost Data",
                             command=lambda: self.insertCostAmountMenu(CloseForm=pageForm))

        reportMenu = Menu(menuBar, tearoff=0, font=('Calibri', 10))
        menuBar.add_cascade(label="Reports", menu=reportMenu)
        # reportMenu.add_command(label="Wallet Report")
        # reportMenu.add_command(label="Income Report")
        # reportMenu.add_command(label="Cost Report")
        reportMenu.add_command(label="Total Report", command=lambda: self.totalReportMenu(CloseForm=pageForm))
        reportMenu.add_command(label="Details Report", command=lambda: self.detailsReportMenu(CloseForm=pageForm))

        editMenu = Menu(menuBar, tearoff=0, font=('Calibri', 10))
        menuBar.add_cascade(label="Basic Info", menu=editMenu)
        editMenu.add_command(label="Wallet Items", command=lambda: self.walletItemMenu(CloseForm=pageForm))
        editMenu.add_command(label="Income Items", command=lambda: self.incomeItemMenu(CloseForm=pageForm))
        editMenu.add_command(label="Cost Items", command=lambda: self.costItemMenu(CloseForm=pageForm))

    def aboutMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.About import about
        CloseForm.destroy()
        About = about()
        About.formLoad()

    def basicInfoMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.BasicInfo import basicInfo
        CloseForm.destroy()
        BasicInfo = basicInfo()
        BasicInfo.formLoad()

    def totalReportMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.TotalReport import totalReport
        CloseForm.destroy()
        TotalReport = totalReport()
        TotalReport.formLoad()

    def detailsReportMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.DetailsReports import filteredReport
        CloseForm.destroy()
        TotalReport = filteredReport()
        TotalReport.formLoad()

    def profileMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.Profile import profile
        CloseForm.destroy()
        Profile = profile()
        Profile.formLoad()

    def walletItemMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.WalletInfo import walletItems
        CloseForm.destroy()
        WalletItem = walletItems()
        WalletItem.formLoad()

    def incomeItemMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.IncomeInfo import incomeItems
        CloseForm.destroy()
        IncomeItem = incomeItems()
        IncomeItem.formLoad()

    def costItemMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.CostInfo import costItems
        CloseForm.destroy()
        CostItem = costItems()
        CostItem.formLoad()

    def insertWalletAmountMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.InsertWalletAmount import walletAmount
        CloseForm.destroy()
        CostItem = walletAmount()
        CostItem.formLoad()

    def insertIncomeAmountMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.InsertIncomeAmount import incomeAmount
        CloseForm.destroy()
        CostItem = incomeAmount()
        CostItem.formLoad()

    def insertCostAmountMenu(self, CloseForm: Tk):
        from UserInterfaceLayer.InsertCostAmount import costAmount
        CloseForm.destroy()
        CostItem = costAmount()
        CostItem.formLoad()

    def exitMenu(self, CloseForm: Tk):
        CloseForm.destroy()



