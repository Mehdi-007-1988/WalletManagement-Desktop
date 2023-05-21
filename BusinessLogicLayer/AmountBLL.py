from Model.AmountModel import AmountsModel
from DataAccessLayer.AmountDAL import CrudAmount
class AmountLogic:
    def validateForm(self, Amount: AmountsModel, Type):
        price = int(Amount.price)
        wicItem = Amount.wicId
        type = Type
        amount = Amount
        if price != '' and 0 < price < 999999999999 and wicItem != '':
            x = CrudAmount()
            x.insertAmount(Amount=amount, Type=type)
            message = "Insert Success"
        else:
            message = "failed"
        return message

    def vaidateReportForm(self, Type: list, Name, StartDate, EndDate, MinPrice, MaxPrice ):
        ObjCrudAmount = CrudAmount()
        typeList = []
        if Type[0] == 1:
            typeList.insert(0, 'W')
        else:
            typeList.insert(0, '')

        if Type[1] == 1:
            typeList.insert(1, 'I')
        else:
            typeList.insert(1, '')

        if Type[2] == 1:
            typeList.insert(2, 'C')
        else:
            typeList.insert(2, '')

        if StartDate == '':
            startDate = ObjCrudAmount.selectFirstDate()
        else:
            x = StartDate.split('/')
            m = int(x[0])
            if 0 < m < 10:
                M = '0' + str(m)
            else:
                M = str(m)
            d = int(x[1])
            if 0 < d < 10:
                D = '0' + str(d)
            else:
                D = str(d)
            y = '20' + x[2]
            date = y + '-' + M + '-' + D
            startDate = date + " 00:00:01.1"

        if EndDate == '':
            endDate = ObjCrudAmount.selectLastDate()
        else:
            x = EndDate.split('/')
            m = int(x[0])
            if 0 < m < 10:
                M = '0'+str(m)
            else:
                M = str(m)
            d = int(x[1])
            if 0 < d < 10:
                D = '0'+str(d)
            else:
                D = str(d)
            y = '20'+x[2]
            date = y+'-'+M+'-'+D
            endDate = date + " 23:59:59.9"

        if MinPrice == '':
            minPrice = ObjCrudAmount.selectMinPrice()
        else:
            minPrice = MinPrice

        if MaxPrice == '':
            maxPrice = ObjCrudAmount.selectMaxPrice()
        else:
            maxPrice = MaxPrice

        name = '%' + Name + '%'

        x = ObjCrudAmount.selectFilteredAmountItems(Type=typeList, StartDate=startDate, EndDate=endDate, Name=name,
                                                    PriceMin=minPrice, PriceMax=maxPrice)
        return x




