# src/gui/register.py
import tkinter as tk
from tkinter import messagebox
from src.database import create_db_connection, check_login, add_user


def register_action(fullname_entry, username_entry, password_entry):
    # Retrieve the entered information
    fullname = fullname_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    # Create a database connection
    connection = create_db_connection("141.209.241.81", "grp7th930", "passinit", "bis698_S24_th930")
    
    # Check if the connection was successful
    if connection is not None and connection.is_connected():
        # Hash the password here before sending it to the database
        # hashed_password = hash_password(password)  # Implement this function
        
        # Add the new user to the database
        add_user(connection, username, password)  # Pass the hashed password instead of plain text
        messagebox.showinfo("Success", "Registration successful!")
        
        # Close the connection
        connection.close()
    else:
        messagebox.showerror("Error", "Failed to connect to the database.")

def create_register_form(root):
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    fullname_label = tk.Label(frame, text="Full Name:")
    fullname_label.grid(row=0, column=0)
    fullname_entry = tk.Entry(frame)
    fullname_entry.grid(row=0, column=1)

    username_label = tk.Label(frame, text="Username:")
    username_label.grid(row=1, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1)

    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=2, column=0)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=2, column=1)

    register_button = tk.Button(frame, text="Register", command=lambda: register_action(fullname_entry, username_entry, password_entry))
    register_button.grid(row=3, column=0, columnspan=2, pady=5)
    
    return frame



