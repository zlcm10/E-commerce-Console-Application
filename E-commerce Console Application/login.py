import bcrypt
import sqlite3
import pyotp

try:
    input_username = input("Username: ")
    input_password = input("Password: ")

    # Hash the user password to compare the hashed password in database
    password = input_password.encode("utf-8")
    salt = b"$2b$12$4hKzd0gZOFPWE5G1uOSw8e"
    hashed = bcrypt.hashpw(password, salt)

    connection = sqlite3.connect('database/user_account.db')
    cursor = connection.cursor()

    cursor.execute("SELECT username, password FROM User_Acc where username = ? AND password = ?", (
        input_username, hashed.decode()))

    rows = cursor.fetchall()

    # If username and password correct with row, show TOTP
    if rows:
        totp = pyotp.TOTP("PIPWY5DOEHK3PXP")
        auth = input("Code: ")

        # If user input code are match with the correct TOTP, successful login
        if auth == totp.now():
            print("Successful Login !")

        else:
            print("Invalid Code !")

    else:
        print("Username or Password Invalid !")

    cursor.close()

except sqlite3.Error as e:
    print("Error while Inserting data", e)

finally:
    if(connection):
        connection.close()
