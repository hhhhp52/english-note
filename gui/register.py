# coding=utf-8
import os
import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox

import yaml

import transfer
from gui.base import BaseGUIFunc
from helpers import helpers


class RegisterGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.register_frame = None
        self.account_entry = None
        self.password_entry = None
        self.check_password_entry = None
        self.name_entry = None
        self.email_entry = None

    def register_layout_init(self):
        register_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        account_label = tk.Label(register_frame, text="Account: ")
        account_label.grid(row=1, column=0)
        account_entry = tk.Entry(register_frame)
        account_entry.grid(row=1, column=1)
        password_label = tk.Label(register_frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = tk.Entry(register_frame, show="*")
        password_entry.grid(row=2, column=1)
        check_password_label = tk.Label(register_frame, text="Check Password: ")
        check_password_label.grid(row=3, column=0)
        check_password_entry = tk.Entry(register_frame, show="*")
        check_password_entry.grid(row=3, column=1)
        name_label = tk.Label(register_frame, text="Name: ")
        name_label.grid(row=4, column=0)
        name_entry = tk.Entry(register_frame)
        name_entry.grid(row=4, column=1)
        email_label = tk.Label(register_frame, text="Email: ")
        email_label.grid(row=5, column=0)
        email_entry = tk.Entry(register_frame)
        email_entry.grid(row=5, column=1)
        login_button = tk.Button(register_frame, text="Send", command=self.register)
        login_button.grid(row=6, column=0)
        clear_button = tk.Button(register_frame, text="Clear", command=self.clear)
        clear_button.grid(row=6, column=1)
        register_frame.pack(anchor=cs.CENTER, expand=True)
        self.register_frame = register_frame
        self.account_entry = account_entry
        self.password_entry = password_entry
        self.check_password_entry = check_password_entry
        self.name_entry = name_entry
        self.email_entry = email_entry

    def clear(self):
        self.destroy_widgets(self.register_frame)
        self.account_entry = None
        self.password_entry = None
        self.check_password_entry = None
        self.name_entry = None
        self.email_entry = None
        self.register_layout_init()

    def register(self):
        try:
            account = self.account_entry.get()
            password = self.password_entry.get()
            check_password = self.check_password_entry.get()

            if account and password and (password == check_password):
                flag = self._check_account_file_exist_or_not(account=account)
                if flag:
                    messagebox.showerror("Failed", "Register Failed")
                else:
                    messagebox.showinfo("Success", "Register Success\nRedirect to homepage")
                    self._generate_account_file()
                    self.destroy_register_layout()
                    transfer.init_login_layout(first_init=True)
            else:
                messagebox.showerror("Failed", "Register Failed")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def destroy_register_layout(self):
        self.register_frame.destroy()

    @classmethod
    def _check_account_file_exist_or_not(cls, account):
        file_name = f"{account}.yaml"
        file_dir = os.path.join(".env", account)

        # Check if the file exists
        file_path = os.path.join(file_dir, file_name)
        if os.path.exists(file_path):
            return True
        return False

    def _generate_account_file(self):
        account = self.account_entry.get()
        password = self.password_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        data = {
            'account': account,
            'password': password,
            'name': name,
            'email': email
        }

        file_name = f"{account}.yaml"
        file_dir = os.path.join(".env", account)

        # Check if the file exists
        file_path = os.path.join(file_dir, file_name)

        # Create the file if it doesn't exist
        os.makedirs(file_dir, exist_ok=True)
        # Write data to the YAML file
        with open(file_path, 'w') as file:
            yaml.dump(data, file)

        print(f"The file '{file_name}' has been created.")
