import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="141.209.241.81",  # Host should be a string
            user="grp7th930",       # User should be a string
            passwd="passinit",      # Password should be a string
            database="bis698_S24_th930"  # Database name should be a string
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def add_user(connection, username, password):
    cursor = None
    try:
        cursor = connection.cursor()
        query = "INSERT INTO User (Username, Password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        print("User added successfully")
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        if cursor is not None:
            cursor.close()

def check_login(connection, username, password):
    cursor = None
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM User WHERE Username = %s AND Password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result
    except Error as e:
        print(f"Error: '{e}'")
        return None
    finally:
        if cursor is not None:
            cursor.close()
