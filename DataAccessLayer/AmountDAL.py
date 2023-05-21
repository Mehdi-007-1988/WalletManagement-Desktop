from datetime import datetime
from Model.AmountModel import AmountsModel
from DataAccessLayer.Connection import ConnectionString

class CrudAmount:
    def insertAmount(self, Amount: AmountsModel, Type):
        CS = ConnectionString().ConnStr()
        SelectWicIdQuery = "Select Id from WIC Where Name = ? And Type = ?"
        SelectWicIdParameter = (Amount.wicId, Type)
        SelectWicIdCursor = CS.cursor()
        SelectWicIdCommand = SelectWicIdCursor.execute(SelectWicIdQuery, SelectWicIdParameter)
        CS.commit()
        a = SelectWicIdCommand.fetchone()
        WicId = a[0]

        InsertAmountQuery = "Insert into Amounts (Price, WICId, UserId, CreatedAt, UpdatedAt) Values(?, ?, ?, ?, ?)"
        InsertAmountParameter = (Amount.price, WicId, Amount.userId, datetime.now(), datetime.now())
        CursorInsert = CS.cursor()
        Command = CursorInsert.execute(InsertAmountQuery, InsertAmountParameter)
        CS.commit()
        CS.close()
        return Command

    def selectSumOfAmounts(self, wicType):
        CS = ConnectionString().ConnStr()
        SelectAmountsPriceQuery = 'SELECT SUM(Price) FROM Amounts INNER JOIN WIC ON WIC.Id = Amounts.WICId WHERE WIC.Type = ? AND Amounts.DeletedAt IS NULL'
        SelectAmountsPriceParameter = (wicType)
        SelectAmountsPriceCursor = CS.cursor()
        SelectAmountsPriceCommand = SelectAmountsPriceCursor.execute(SelectAmountsPriceQuery,
                                                                     SelectAmountsPriceParameter)
        CS.commit()
        a = SelectAmountsPriceCommand.fetchone()
        SumOfPrice = a[0]
        CS.close()
        return SumOfPrice

    def selectFilteredAmountItems(self, Type: list, StartDate, EndDate, Name, PriceMin, PriceMax):
        CS = ConnectionString().ConnStr()
        SelectFilteredAmountItemsQuery = "SELECT * FROM Amounts INNER JOIN WIC ON WIC.Id = Amounts.WICId WHERE WIC.Type IN (?, ?, ?) AND Amounts.DeletedAt IS NULL AND Amounts.CreatedAt BETWEEN ? AND ? AND Amounts.Price BETWEEN ? AND ? AND WIC.Name like ?"
        SelectFilteredAmountItemsParameter = (Type[0], Type[1], Type[2], StartDate, EndDate, PriceMin, PriceMax, Name)
        SelectFilteredAmountItemsCursor = CS.cursor()
        SelectFilteredAmountItemsCommand = SelectFilteredAmountItemsCursor.execute(SelectFilteredAmountItemsQuery,
                                                                                   SelectFilteredAmountItemsParameter)
        CS.commit()
        AmountList = SelectFilteredAmountItemsCommand.fetchall()
        CS.close()
        # print(f"W: {Type[0]} - {type(Type[0])}\nI: {Type[1]} - {type(Type[1])}\nC: {Type[2]} - {type(Type[2])}\n"
        #       f"Start Date: {StartDate} - {type(StartDate)}\nEndDate: {EndDate} - {type(EndDate)}\n"
        #       f"MinPrice: {PriceMin} - {type(PriceMin)}\nMax Price: {PriceMax} - {type(PriceMax)}\n"
        #       f"Name: {Name} - {type(Name)}\n\n")
        Items = []
        for item in AmountList:
            Items.append(item)
        return Items

    def selectFirstDate(self):
        CS = ConnectionString().ConnStr()
        SelectFirstDateQuery = "SELECT CreatedAt FROM Amounts WHERE DeletedAt IS NULL ORDER BY CreatedAt ASC LIMIT 1"
        SelectFirstDateCursor = CS.cursor()
        SelectStartDateCommand = SelectFirstDateCursor.execute(SelectFirstDateQuery)
        CS.commit()
        a = SelectStartDateCommand.fetchone()
        FirstDate = a[0]
        CS.close()
        return FirstDate

    def selectLastDate(self):
        CS = ConnectionString().ConnStr()
        SelectLastDateQuery = "SELECT CreatedAt FROM Amounts WHERE DeletedAt IS NULL ORDER BY CreatedAt DESC LIMIT 1"
        SelectLastDateCursor = CS.cursor()
        SelectStartDateCommand = SelectLastDateCursor.execute(SelectLastDateQuery)
        CS.commit()
        a = SelectStartDateCommand.fetchone()
        LastDate = a[0]
        CS.close()
        return LastDate

    def selectMinPrice(self):
        CS = ConnectionString().ConnStr()
        selectMinPriceQuery = "SELECT Price FROM Amounts WHERE DeletedAt IS NULL ORDER BY Price ASC LIMIT 1"
        selectMinPriceCursor = CS.cursor()
        SelectMinPriceCommand = selectMinPriceCursor.execute(selectMinPriceQuery)
        CS.commit()
        a = SelectMinPriceCommand.fetchone()
        MinPrice = a[0]
        CS.close()
        return MinPrice

    def selectMaxPrice(self):
        CS = ConnectionString().ConnStr()
        selectMaxPriceQuery = "SELECT Price FROM Amounts WHERE DeletedAt IS NULL ORDER BY Price DESC LIMIT 1"
        selectMaxPriceCursor = CS.cursor()
        SelectMaxPriceCommand = selectMaxPriceCursor.execute(selectMaxPriceQuery)
        CS.commit()
        a = SelectMaxPriceCommand.fetchone()
        MaxPrice = a[0]
        CS.close()
        return MaxPrice