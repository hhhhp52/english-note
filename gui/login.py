# coding=utf-8
import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox

import transfer
from gui.base import BaseGUIFunc


class LoginGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None
        self.env_variable = None

    def login_layout_init(self):
        env_variable = tk.StringVar()
        env_variable.set("env")
        login_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        # env_label = tk.Label(login_frame, text="Environment: ")
        # env_label.grid(row=0, column=0)
        # local_radio_button = tk.Radiobutton(
        #     login_frame, variable=env_variable, text="local", value="local"
        # )
        # local_radio_button.select()
        # local_radio_button.grid(row=0, column=1)
        # dev_radio_button = tk.Radiobutton(
        #     login_frame, variable=env_variable, text="development", value="dev"
        # )
        # dev_radio_button.grid(row=0, column=2)
        # staging_radio_button = tk.Radiobutton(
        #     login_frame, variable=env_variable, text="staging", value="staging"
        # )
        # staging_radio_button.grid(row=0, column=3)
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
        clear_button = tk.Button(login_frame, text="Clear", command=self.clear)
        clear_button.grid(row=3, column=2)
        login_frame.pack(anchor=cs.CENTER, expand=True)
        self.login_frame = login_frame
        self.account_entry = account_entry
        self.password_entry = password_entry
        self.env_variable = env_variable

    def clear(self):
        self.destroy_widgets(self.login_frame, self.account_entry, self.password_entry)
        self.login_layout_init()

    def login(self):
        try:
            account = self.account_entry.get()
            password = self.password_entry.get()
            host = True
            # host = get_host_by_env(env)

            if host and account and password:
                flag = True
                # flag = domain.login_flow(host, account, password)
                if flag:
                    messagebox.showinfo("Success", "Login Success")
                    transfer.init_homepage_layout(account)
                else:
                    messagebox.showerror("Failed", "Login Failed")
            else:
                messagebox.showerror("Failed", "Login Failed")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    @classmethod
    def guest_login(cls):
        messagebox.showinfo("Success", "Login Success")
        transfer.init_homepage_layout("Guest")

    def destroy_login_layout(self):
        self.login_frame.destroy()
        self.account_entry.destroy()
        self.password_entry.destroy()
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None
        self.env_variable = None
