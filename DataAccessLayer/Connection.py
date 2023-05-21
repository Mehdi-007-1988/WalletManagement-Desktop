import sqlite3

class ConnectionString:
    def ConnStr(self):
        ConnectionString = "D:/Data Science/52-Project/Accounting Book/AccountingBooks/acc.db"
        connection = sqlite3.connect(ConnectionString, timeout=10)
        return connection

