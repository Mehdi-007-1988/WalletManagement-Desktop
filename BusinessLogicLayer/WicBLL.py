from Model.WicModel import WicModel
from DataAccessLayer.WicDAL import CrudWIC

class checkFormEntry:
    def CheckUniqueName(self, wic: WicModel, wicType):
        x = CrudWIC()
        wicName = x.getAllSingleTypeItems(wicType)
        a = False
        for item in wicName:
            if wic.name == item:
                a = True

        if a == False:
            x.InsertItem(wallet=wic, type=wic.type)
            message = 'The Name Insert Successful'
        else:
            message = 'Already Exist!'

        return message