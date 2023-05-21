from DataAccessLayer.UserDAL import *
from UserInterfaceLayer.Login import loginForm
from UserInterfaceLayer.Register import RegisterFrom

# -------<< Check Count of User. If Exist User Open Login Form, Else Open Register Form >> :
CheckUserObject = CrudUser()
if int(CheckUserObject.checkEmptyUser()) >= 0:
    LoginForm = loginForm().formLoad()
else:
    RegisterFrom = RegisterFrom().formLoad()
