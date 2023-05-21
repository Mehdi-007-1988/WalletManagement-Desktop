import sqlite3
from datetime import datetime
from Model.UserModel import UserModel
from DataAccessLayer.Connection import ConnectionString

class CrudUser:
    def checkEmptyUser(self):
        CS = ConnectionString().ConnStr()
        InsertOrderQuery = 'select count(id) from Users'
        Cursor = CS.cursor()
        Command = Cursor.execute(InsertOrderQuery)
        CS.commit()
        UserCount = Command.fetchone()[0]
        CS.close()
        return UserCount

    def insertUser(self, userRegister: UserModel):
        CS = ConnectionString().ConnStr()
        InsertUserQuery = 'insert into Users' \
                          '(ID, FirstName, LastName, UserName, Password, Gender, BirthDate, CreatedAt, UpdatedAt)' \
                          'Values (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        InsertUserParameters = (1, userRegister.firstName, userRegister.lastName, userRegister.username,
                                userRegister.password, userRegister.gender, userRegister.birthDate, datetime.now(),
                                datetime.now())
        Cursor = CS.cursor()
        Command = Cursor.execute(InsertUserQuery, InsertUserParameters)
        CS.commit()
        CS.close()

    def selectUserPass(self):
        CS = ConnectionString().ConnStr()
        SelectUserQuery = 'Select UserName, Password from Users where ID = ?'
        SelectUserParameters = ('1')
        Cursor = CS.cursor()
        Command = Cursor.execute(SelectUserQuery, SelectUserParameters)
        CS.commit()
        UserPass = Command.fetchone()
        CS.close()
        return UserPass