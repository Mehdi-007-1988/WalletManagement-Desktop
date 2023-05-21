from tkinter import *
from Model.UserModel import UserModel
from DataAccessLayer.UserDAL import CrudUser

class RegisterFrom:
    def formLoad(self):
        # ---------<< Register Methode >>
        def registerUserUI():
            FirstName = txtFirstName.get()
            LastName = txtLastName.get()
            Gender = txtGender.get()
            BirthDate = txtBirthDate.get()
            Username = txtUserName.get()
            Password = txtPassword.get()
            x = UserModel(FirstName=FirstName, LastName=LastName, Gender=Gender, BirthDate=BirthDate,
                          Username=Username, Password=Password)
            regUser = CrudUser()
            regUser.insertUser(userRegister=x)

        # ---------<< Check BirthDate Validation >>
        def checkDate(*args):
            temp = txtBirthDate.get()

            if len(temp) <= 4 and not temp.isdigit():
                txtBirthDate.set(txtBirthDate.get()[:len(txtBirthDate.get()) - 1])

            if len(temp) == 5 and temp[4] != '/':
                txtBirthDate.set(txtBirthDate.get()[:len(txtBirthDate.get()) - 1])

            if len(temp) > 5 and not temp[5:6].isdigit():
                txtBirthDate.set(txtBirthDate.get()[:len(txtBirthDate.get()) - 1])

            if len(temp) == 8 and temp[7] != '/':
                txtBirthDate.set(txtBirthDate.get()[:len(txtBirthDate.get()) - 1])

            if len(temp) > 8 and not temp[8:9].isdigit():
                txtBirthDate.set(txtBirthDate.get()[:len(txtBirthDate.get()) - 1])

            if len(temp) >= 11:
                txtBirthDate.set(txtBirthDate.get()[:len(txtBirthDate.get()) - 1])

        # region RegisterForm
        RegisterForm = Tk()
        RegisterForm.title('Accounting Book - Register')
        # RegisterForm.geometry('325x310')
        RegisterForm.iconbitmap('Files/Images/wallet.ico')
        RegisterForm.configure(bg='#F3E5F5')
        # endregion

        # region InfoFrame
        # ---------<< Frame >>
        frameInfo = LabelFrame(RegisterForm, text='  Register : ',bg='#F3E5F5')
        frameInfo.grid(row=1, column=0, padx=20, pady=10)
        # endregion

        # region FirstName
        # ---------<< First Name Label >>
        labelFirstName = Label(frameInfo, text='First Name:', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        labelFirstName.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        # ---------<< First Name Entry >>
        txtFirstName = StringVar()
        entryFirstName = Entry(frameInfo, textvariable=txtFirstName, width=20, highlightthickness=1, font='tahoma 10')
        entryFirstName.grid(row=1, column=1, padx=10, pady=5)
        # endregion

        # region LastName
        # ---------<< Last Name Label >>
        labelLastName = Label(frameInfo, text='Last Name:', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        labelLastName.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        # ---------<< Last Name Entry >>
        txtLastName = StringVar()
        entryLastName = Entry(frameInfo, textvariable=txtLastName, width=20, highlightthickness=1, font='tahoma 10')
        entryLastName.grid(row=2, column=1, padx=10, pady=5)
        # endregion

        # region Gender
        # ---------<< Gender Label >>
        labelGender = Label(frameInfo, text='Gender:', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        labelGender.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        # ---------<< Gender Radio Button >>
        txtGender = StringVar()
        txtGender.set(value=None)
        radioMale = Radiobutton(frameInfo, text='Male', variable=txtGender, value='M', bg='#F3E5F5')
        radioMale.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        radioFemale = Radiobutton(frameInfo, text='Female', variable=txtGender, value='F', bg='#F3E5F5')
        radioFemale.grid(row=3, column=1, padx=5, pady=5, sticky='e')
        # endregion

        # region BirthDate
        # ---------<< Birth Date Label >>
        labelBirthDate = Label(frameInfo, text='Birth Date:', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        labelBirthDate.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        # ---------<< Birth Date Entry >>
        txtBirthDate = StringVar()
        txtBirthDate.trace('w', checkDate)
        entryBirthDate = Entry(frameInfo, textvariable=txtBirthDate, width=20, highlightthickness=1, font='tahoma 10')
        entryBirthDate.grid(row=4, column=1, padx=10, pady=5)
        # endregion

        # region Separator
        # ---------<< Separator >>
        separator1 = Label(frameInfo, text='.' * 85, bg='#F3E5F5', fg='light gray')
        separator1.grid(row=5, column=0, columnspan=2, padx=10, pady=0)
        # endregion

        # region Username
        # ---------<< Username Label >>
        labelUserName = Label(frameInfo, text='User Name:', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        labelUserName.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        # ---------<< Username Entry >>
        txtUserName = StringVar()
        entryUserName = Entry(frameInfo, textvariable=txtUserName, width=20, highlightthickness=1, font='tahoma 10')
        entryUserName.grid(row=6, column=1, padx=10, pady=5)
        # endregion

        # region Password
        # ---------<< Password Label >>
        labelPassword = Label(frameInfo, text='Password:', fg='Indigo', font=('Calibri', 10, 'bold'), bg='#F3E5F5')
        labelPassword.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        # ---------<< Password Entry >>
        txtPassword = StringVar()
        entryPassword = Entry(frameInfo, textvariable=txtPassword, width=20, highlightthickness=1, font='tahoma 10')
        entryPassword.grid(row=7, column=1, padx=10, pady=5)
        # endregion

        # region Buttons
        # ---------<< Register Button >>
        buttonRegister = Button(frameInfo, text='Register', width=10, height=1, font=('Calibri', 10, 'bold'), bg='#FFFFFF',
                                fg='#33691E', command=registerUserUI)
        buttonRegister.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
        # endregion

        RegisterForm.mainloop()