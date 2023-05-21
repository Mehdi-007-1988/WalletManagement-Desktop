from tkinter import *

class basicInfo:
    def formLoad(self):
        basicInfoForm = Tk()
        basicInfoForm.title('Accounting Book - Basic Info')
        basicInfoForm.geometry('350x180')
        basicInfoForm.iconbitmap('Files/Images/wallet.ico')
        basicInfoForm.configure(bg='#F3E5F5')

        MenuBar = Menu(basicInfoForm)
        basicInfoForm.config(menu=MenuBar)

        fileMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
        MenuBar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="About")
        fileMenu.add_command(label="Exit", command=lambda: basicInfoForm.destroy())

        dataMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
        MenuBar.add_cascade(label="Data", menu=dataMenu)
        dataMenu.add_command(label="Insert New Income")
        dataMenu.add_command(label="Insert New Cost")
        dataMenu.add_command(label="Income Report")
        dataMenu.add_command(label="Cost Report")
        dataMenu.add_command(label="Total Report")

        editMenu = Menu(MenuBar, tearoff=0, font=('Calibri', 10))
        MenuBar.add_cascade(label="Basic Info", menu=editMenu)
        editMenu.add_command(label="Income Items")
        editMenu.add_command(label="Cost Items")

        lblUserName = Label(basicInfoForm, text='Basic Info: ', fg='Indigo', font=('Calibri', 12, 'bold'), bg='#F3E5F5')
        lblUserName.grid(row=0, column=0)

        basicInfoForm.mainloop()


