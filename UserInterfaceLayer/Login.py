from tkinter import *
from UserInterfaceLayer.Home import homeForm
from DataAccessLayer.UserDAL import CrudUser

class loginForm:
    def formLoad(self):
        # -------<< Check Login Method >> :
        def checkLogin():
            UserName = username.get()
            Password = password.get()

            userpass = CrudUser()
            fetchUser = userpass.selectUserPass()

            # print(userpass.selectUserPass()[0][1])
            if fetchUser[0] == UserName and fetchUser[0] == Password:
                loginForm.destroy()
                h = homeForm().formLoad()
            else:
                lblfailedLogin = Label(loginForm, text='Username or Password is Incorrect! ', fg='#FF0000',
                                       font=('Calibri', 10, 'bold'), bg='#F3E5F5')
                lblfailedLogin.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

        # region Form
        loginForm = Tk()
        loginForm.title('Accounting Book - Login')
        # loginForm.geometry('350x150')
        loginForm.iconbitmap('Files/Images/wallet.ico')
        loginForm.configure(bg='#F3E5F5')
        # endregion

        # region LoginFrame
        loginFrame = LabelFrame(loginForm, text='  Login : ',bg='#F3E5F5')
        loginFrame.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region Username
        # -------<< Username Label >> :
        lblUserName = Label(loginFrame, text='Username: ', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        lblUserName.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        # -------<< Username Entry >> :
        username = StringVar()
        entUserName = Entry(loginFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo',
                            textvariable=username)
        entUserName.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        # endregion

        # region Password
        # -------<< Password Label >> :
        lblPassword = Label(loginFrame, text='Password: ', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        lblPassword.grid(row=1, column=0, padx=10, pady=0, sticky='nw')
        # -------<< Password Entry >> :
        password = StringVar()
        entPassword = Entry(loginFrame, width=20, highlightthickness=1, font=('Calibri', 10), fg='Indigo', show='*',
                            textvariable=password)
        entPassword.grid(row=1, column=1, padx=10, pady=0, columnspan=2)
        # endregion

        # region Buttons
        # -------<< Login Button >> :
        btnLogin = Button(loginFrame, text='Login', width=10, height=1, font=('Calibri', 10, 'bold'), bg='#FFFFFF',
                          fg='#33691E', command=checkLogin)
        btnLogin.grid(row=2, column=1, padx=10, pady=10, sticky='nw')
        # endregion
        loginForm.mainloop()

