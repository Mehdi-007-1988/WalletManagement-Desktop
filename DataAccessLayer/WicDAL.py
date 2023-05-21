from datetime import datetime
from Model.WicModel import WicModel
from DataAccessLayer.Connection import ConnectionString

class CrudWIC:
    def getAllSingleTypeItems(self, wicType):
        CS = ConnectionString().ConnStr()
        SelectWalletItemsQuery = "Select Name From WIC Where type = ?"
        SelectWalletItemsParameters = (wicType)
        Cursor = CS.cursor()
        Command = Cursor.execute(SelectWalletItemsQuery, SelectWalletItemsParameters)
        CS.commit()
        WalletCompleteItems = Command.fetchall()
        CS.close()
        Items = ['']
        for item in WalletCompleteItems:
            Items.append(item[0])
        return Items

    def InsertItem(self, wallet: WicModel, type):
        CS = ConnectionString().ConnStr()
        if wallet.parentId == '':
            ParentId = None
        else:
            SelectParentIdQuery = "Select Id From WIC Where Name = ? and Type = ?"
            SelectParentIdParameter = (wallet.parentId, wallet.type)
            CursorSelectParentId = CS.cursor()
            CommandSelectParentId = CursorSelectParentId.execute(SelectParentIdQuery, SelectParentIdParameter)
            CS.commit()
            a = CommandSelectParentId.fetchone()
            ParentId = a[0]

        InsertWalletItemQuery = "Insert into WIC (Name, ParentId, Type, UserId, CreatedAt, UpdatedAt)" \
                                "Values(?, ?, ?, ?, ?, ?)"
        InsertWalletItemParameter = (wallet.name, ParentId, wallet.type, wallet.userId, datetime.now(),
                                     datetime.now())
        CursorInsert = CS.cursor()
        Command = CursorInsert.execute(InsertWalletItemQuery, InsertWalletItemParameter)
        CS.commit()
        CS.close()