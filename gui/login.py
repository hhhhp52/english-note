# coding=utf-8
import os
import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox

import yaml

import transfer
from gui.base import BaseGUIFunc


class LoginGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None

    def login_layout_init(self):
        login_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        account_label = tk.Label(login_frame, text="Account: ")
        account_label.grid(row=1, column=0)
        account_entry = tk.Entry(login_frame)
        account_entry.grid(row=1, column=1)
        password_label = tk.Label(login_frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.grid(row=2, column=1)
        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=0)
        guest_login_button = tk.Button(login_frame, text="Guest Login", command=self.guest_login)
        guest_login_button.grid(row=3, column=1)
        register_button = tk.Button(login_frame, text="Register", command=self.register)
        register_button.grid(row=3, column=2)
        clear_button = tk.Button(login_frame, text="Clear", command=self.clear)
        clear_button.grid(row=3, column=3)
        login_frame.pack(anchor=cs.CENTER, expand=True)
        self.login_frame = login_frame
        self.account_entry = account_entry
        self.password_entry = password_entry

    def clear(self):
        self.destroy_widgets(self.login_frame, self.account_entry, self.password_entry)
        self.login_layout_init()

    def login(self):
        try:
            account = self.account_entry.get()
            password = self.password_entry.get()

            if account and password:
                flag, account_data = self._check_login(account=account, password=password)
                if flag:
                    messagebox.showinfo("Success", "Login Success")
                    transfer.init_homepage_layout(account_data)
                else:
                    messagebox.showerror("Failed", "Login Failed")
            else:
                messagebox.showerror("Failed", "Login Failed")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    @classmethod
    def guest_login(cls):
        account_data = dict(
            account="guest",
            name="Guest",
            email=None
        )
        messagebox.showinfo("Success", "Login Success")
        transfer.init_homepage_layout(account_data)

    @classmethod
    def register(cls):
        transfer.init_register_layout()

    def destroy_login_layout(self):
        self.login_frame.destroy()
        self.account_entry.destroy()
        self.password_entry.destroy()
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None

    @classmethod
    def _check_login(cls, account, password):
        file_name = f"{account}.yaml"
        file_dir = os.path.join(".env", account)

        # Check if the file exists
        file_path = os.path.join(file_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)

            if data["password"] == password:
                return True, dict(account=account, name=data["name"], email=data["email"])
        return False, None
