
class Utilities:
    def checkDate(self, InputDate):
        temp = InputDate.get()

        if len(temp) <= 4 and not temp.isdigit():
            InputDate.set(InputDate.get()[:len(InputDate.get()) - 1])

        if len(temp) == 5 and temp[4] != '/':
            InputDate.set(InputDate.get()[:len(InputDate.get()) - 1])

        if len(temp) > 5 and not temp[5:6].isdigit():
            InputDate.set(InputDate.get()[:len(InputDate.get()) - 1])

        if len(temp) == 8 and temp[7] != '/':
            InputDate.set(InputDate.get()[:len(InputDate.get()) - 1])

        if len(temp) > 8 and not temp[8:9].isdigit():
            InputDate.set(InputDate.get()[:len(InputDate.get()) - 1])

        if len(temp) >= 11:
            InputDate.set(InputDate.get()[:len(InputDate.get()) - 1])