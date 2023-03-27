import sqlite3


try:
    # define connection and cursor
    connection = sqlite3.connect('database/user_account.db')
    cursor = connection.cursor()

    # create user account table
    table = """CREATE TABLE IF NOT EXISTS
    User_Acc(userID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)"""

    cursor.execute(table)
    connection.commit()

    print("Table Created")
    cursor.close

except sqlite3.Error as e:
    print("Connection Error")

finally:
    if(connection):
        connection.close()
        print("Connection Closed")
