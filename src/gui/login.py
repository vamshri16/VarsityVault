# src/gui/login.py
import tkinter as tk
from tkinter import messagebox
from src.database import create_db_connection, check_login

def login_action(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    # Create a database connection
    connection = create_db_connection("141.209.241.81", "grp7th930", "passinit", "bis698_S24_th930")

    if connection is not None and connection.is_connected():
        user = check_login(connection, username, password)  # Updated to pass the connection
        if user:
            messagebox.showinfo("Login Success", "You are now logged in!")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")
        connection.close()
    else:
        messagebox.showerror("Database Error", "Failed to connect to the database.")

def create_login_form(root):
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    username_label = tk.Label(frame, text="Username:")
    username_label.grid(row=0, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=0, column=1)

    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=1, column=0)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(frame, text="Login", command=lambda: login_action(username_entry, password_entry))
    login_button.grid(row=2, column=0, columnspan=2, pady=5)
    
    return frame



