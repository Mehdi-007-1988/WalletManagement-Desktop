from tkinter import *
from DataAccessLayer.AmountDAL import CrudAmount
from BusinessLogicLayer.MenuItemInfo import menuItems
from BusinessLogicLayer.AmountBLL import AmountLogic
from tkcalendar import DateEntry

class filteredReport:
    def formLoad(self):
        lst = []
        # -------<< Search Method >> :
        def searchByFilter():
            StartDate = startDate.get()
            EndDate = endDate.get()
            W = TypeW.get()
            I = TypeI.get()
            C = TypeC.get()
            Type = [W, I, C]
            MinPrice = minPrice.get()
            MaxPrice = maxPrice.get()
            Name = name.get()
            x = AmountLogic()
            result = x.vaidateReportForm(Type=Type, Name=Name, StartDate=StartDate, EndDate=EndDate,
                                         MinPrice=MinPrice, MaxPrice=MaxPrice)

            resetGrid()
            counter = 1
            for i in range(len(result)):
                Price = result[i][1]
                Name = result[i][8]
                wic = result[i][10]
                if wic == 'C':
                    Type = 'Cost'
                elif wic == 'I':
                    Type = 'Income'
                elif wic == 'W':
                    Type = 'Wallet'
                date1 = result[i][4]
                date2 = date1.split(' ')
                Date = date2[0].replace('-', '/')

                Row = i+7
                a1 = Label(filteredReportFrame, text=counter, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10))
                a1.grid(row=Row, column=0, padx=2, pady=5, sticky='w')

                a2 = Label(filteredReportFrame, text=Name, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10))
                a2.grid(row=Row, column=1, padx=2, pady=5, sticky='w')

                a3 = Label(filteredReportFrame, text=Type, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10))
                a3.grid(row=Row, column=2, padx=2, pady=5, sticky='w')

                a4 = Label(filteredReportFrame, text=Price, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10))
                a4.grid(row=Row, column=3, padx=2, pady=5, sticky='w')

                a5 = Label(filteredReportFrame, text=Date, fg='Indigo', bg='#F3E5F5', font=('Calibri', 10))
                a5.grid(row=Row, column=4, padx=2, pady=5, sticky='w')
                lst.extend([a1, a2, a3, a4, a5])
                counter += 1

        # -------<< Remove Previous Grids Method >> :
        def resetGrid():
            for i in range(len(lst)):
                lst[i].destroy()

        # region Form
        filteredReportAmountForm = Tk()
        filteredReportAmountForm.title('Accounting Book - Report')
        positionRight = int(filteredReportAmountForm.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(filteredReportAmountForm.winfo_screenheight() / 2 - 300 / 2)
        filteredReportAmountForm.geometry("+{}+{}".format(positionRight, positionDown))
        filteredReportAmountForm.resizable(0, 0)
        # filteredReportAmountForm.geometry('400x180')
        filteredReportAmountForm.iconbitmap('Files/Images/wallet.ico')
        filteredReportAmountForm.configure(bg='#F3E5F5')
        # endregion

        # region Menu
        menu = menuItems()
        menu.displayMenu(pageForm=filteredReportAmountForm)
        # endregion

        # -------<< Create Crud Object Label >> :
        x = CrudAmount()

        # region ReportFrame
        filteredReportFrame = LabelFrame(filteredReportAmountForm, bg='#F3E5F5')
        filteredReportFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region StartDate
        # -------<< Start Date Label >> :
        filterStartDateLabel = Label(filteredReportFrame, text='Start Date:', fg='Indigo', bg='#F3E5F5',
                                     font=('Calibri', 10, 'bold'))
        filterStartDateLabel.grid(row=2, column=0, padx=2, pady=5, sticky='w')
        # -------<< Start Date Entry >> :
        startDate = StringVar()
        filterStartDateEntry = DateEntry(filteredReportFrame, width=10, highlightthickness=1, font=('Calibri', 10),
                                         fg='Indigo', textvariable=startDate)
        filterStartDateEntry.grid(row=2, column=1, padx=2, pady=5, sticky='w')
        # endregion

        # region EndDate
        # -------<< End Date Label >> :
        filterEndDateLabel = Label(filteredReportFrame, text='End Date:', fg='Indigo', bg='#F3E5F5',
                                   font=('Calibri', 10, 'bold'))
        filterEndDateLabel.grid(row=2, column=2, padx=2, pady=5, sticky='w')
        # -------<< End Date Entry >> :
        endDate = StringVar()
        filterEndDateEntry = DateEntry(filteredReportFrame, width=10, highlightthickness=1, font=('Calibri', 10),
                                       fg='Indigo', textvariable=endDate, date_patternstr='y-mm-dd')
        filterEndDateEntry.grid(row=2, column=3, padx=2, pady=5, sticky='w')
        # endregion

        # region Type
        # -------<< Type Label >> :
        filterTypeLabel = Label(filteredReportFrame, text='Type:', fg='Indigo', bg='#F3E5F5',
                                     font=('Calibri', 10, 'bold'))
        filterTypeLabel.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        # -------<< Type Wallet CheckBox >> :
        TypeW = IntVar(value=1)
        filterTypeWCheckbox = Checkbutton(filteredReportFrame, text='Wallet',variable=TypeW, onvalue=1, offvalue=0,
                                          bg='#F3E5F5')
        filterTypeWCheckbox.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        # -------<< Type Income CheckBox >> :
        TypeI = IntVar(value=1)
        filterTypeICheckbox = Checkbutton(filteredReportFrame, text='Income',variable=TypeI, onvalue=1, offvalue=0,
                                          bg='#F3E5F5')
        filterTypeICheckbox.grid(row=3, column=2, padx=10, pady=5, sticky='w')
        # -------<< Type Cost CheckBox >> :
        TypeC = IntVar(value=1)
        filterTypeCCheckbox = Checkbutton(filteredReportFrame, text='Cost',variable=TypeC, onvalue=1, offvalue=0,
                                          bg='#F3E5F5')
        filterTypeCCheckbox.grid(row=3, column=3, padx=10, pady=5, sticky='w')
        # endregion

        # region MinPrice
        # -------<< Min Price Label >> :
        filterMinPriceLabel = Label(filteredReportFrame, text='Min Price:', fg='Indigo', bg='#F3E5F5',
                                    font=('Calibri', 10, 'bold'))
        filterMinPriceLabel.grid(row=4, column=0, padx=2, pady=5, sticky='w')
        # -------<< Min Price Entry >> :
        minPrice = StringVar()
        filterMinPriceEntry = Entry(filteredReportFrame, width=10, highlightthickness=1, font=('Calibri', 10),
                                    fg='Indigo', textvariable=minPrice)
        filterMinPriceEntry.grid(row=4, column=1, padx=2, pady=5, sticky='w')
        # endregion

        # region MaxPrice
        # -------<< Max Price Label >> :
        filterMaxPriceLabel = Label(filteredReportFrame, text='Max Price:', fg='Indigo', bg='#F3E5F5',
                                    font=('Calibri', 10, 'bold'))
        filterMaxPriceLabel.grid(row=4, column=2, padx=2, pady=5, sticky='w')
        # -------<< Max Price Entry >> :
        maxPrice = StringVar()
        filterMaxPriceEntry = Entry(filteredReportFrame, width=10, highlightthickness=1, font=('Calibri', 10),
                                    fg='Indigo', textvariable=maxPrice)
        filterMaxPriceEntry.grid(row=4, column=3, padx=2, pady=5, sticky='w')
        # endregion

        # region Name
        # -------<< Name Label >> :
        filterNameLabel = Label(filteredReportFrame, text='Name:', fg='Indigo', bg='#F3E5F5',
                                font=('Calibri', 10, 'bold'))
        filterNameLabel.grid(row=5, column=0, padx=2, pady=5, sticky='w')
        # -------<< Name Entry >> :
        name = StringVar()
        filterNameEntry = Entry(filteredReportFrame, width=10, highlightthickness=1, font=('Calibri', 10),
                                fg='Indigo', textvariable=name)
        filterNameEntry.grid(row=5, column=1, padx=2, pady=5, sticky='w')
        # endregion

        # region Button
        # -------<< Search Button >> :
        buttonRegister = Button(filteredReportFrame, text='Search', width=14, height=1, font=('Calibri', 10, 'bold'),
                                bg='#FFFFFF', fg='#33691E', command=searchByFilter)
        buttonRegister.grid(row=5, column=3, columnspan=2, padx=10, pady=5)
        # endregion

        # region Result
        # -------<< Result Grid >> :
        Label(filteredReportFrame, text='#', fg='black', bg='#F3E5F5', font=('Calibri', 10, 'bold')) \
            .grid(row=6, column=0, padx=2, pady=5, sticky='w')
        Label(filteredReportFrame, text='Title', fg='black', bg='#F3E5F5', font=('Calibri', 10, 'bold')) \
            .grid(row=6, column=1, padx=2, pady=5, sticky='w')
        Label(filteredReportFrame, text='Type', fg='black', bg='#F3E5F5', font=('Calibri', 10, 'bold')) \
            .grid(row=6, column=2, padx=2, pady=5, sticky='w')
        Label(filteredReportFrame, text='Price', fg='black', bg='#F3E5F5', font=('Calibri', 10, 'bold')) \
            .grid(row=6, column=3, padx=2, pady=5, sticky='w')
        Label(filteredReportFrame, text='Date', fg='black', bg='#F3E5F5', font=('Calibri', 10, 'bold')) \
            .grid(row=6, column=4, padx=2, pady=5, sticky='w')
        # endregion

        filteredReportAmountForm.mainloop()