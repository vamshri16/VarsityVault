import tkinter as tk
from tkinter import ttk
# Adjust the import paths based on your project structure
from gui.login import create_login_form
from gui.register import create_register_form
from src.database import create_db_connection, check_login


def show_login_form():
    # Clear the current frame content
    for widget in main_frame.winfo_children():
        widget.destroy()

    login_form = create_login_form(main_frame)
    login_form.pack()

    switch_to_register.pack(side=tk.BOTTOM, pady=10)

def show_register_form():
    # Clear the current frame content
    for widget in main_frame.winfo_children():
        widget.destroy()

    register_form = create_register_form(main_frame)
    register_form.pack()

    switch_to_login.pack(side=tk.BOTTOM, pady=10)

def main():
    global main_frame, switch_to_login, switch_to_register

    root = tk.Tk()
    root.title("Varsity Vault")
    root.geometry("400x300")

    # Main frame to contain different forms
    main_frame = ttk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Buttons to switch between forms
    switch_to_login = ttk.Button(root, text="Login", command=show_login_form)
    switch_to_register = ttk.Button(root, text="Register", command=show_register_form)

    # Initially show the login form
    show_login_form()

    root.mainloop()

if __name__ == "__main__":
    main()
