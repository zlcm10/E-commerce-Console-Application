import bcrypt
import sqlite3
import sys

try:
    # Connect to database
    connection = sqlite3.connect('database/user_account.db')
    cursor = connection.cursor()

    # Input username
    input_username = input("Username: ")

    cursor.execute("SELECT username FROM User_Acc where username = ?", (
        input_username,))

    # Check if username exists in database, if yes, system close
    for x in cursor.fetchall():
        if input_username in x:
            print('Username already exists')
        sys.exit()

    # Input password and confirm password
    input_password = input("Password: ")
    input_conpassword = input("Confirm Password: ")

    # Check if password do not match with confirm password
    if input_password != input_conpassword:
        print("Confirm Password do not match with the password !")

    # Check if password match with confirm password, then create a new account
    if input_password == input_conpassword:
        password = input_password.encode("utf-8")
        salt = b"$2b$12$4hKzd0gZOFPWE5G1uOSw8e"
        hashed = bcrypt.hashpw(password, salt)

        user_data = """INSERT INTO User_Acc (username, password) VALUES ('{}', '{}');""".format(
            input_username, hashed.decode())

        cursor.execute(user_data)
        connection.commit()

        print("Successful Register !")
    cursor.close()

except sqlite3.Error as e:
    print("Error while Inserting data", e)

finally:
    if(connection):
        connection.close()
