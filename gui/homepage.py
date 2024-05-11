# coding=utf-8
import tkinter as tk
import tkinter.constants as cs

import transfer
from gui.base import BaseGUIFunc


class HomePageGUIFunc(BaseGUIFunc):

    def __init__(self, account=None):
        self.homepage_frame = None
        self.function_frame = None
        self.account = account

    def homepage_layout_init(self):
        homepage_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=1024, height=400)
        account_label = tk.Label(homepage_frame, text="Account: {account}".format(account=self.account))
        account_label.grid(row=0, column=0)
        clear_button = tk.Button(homepage_frame, text="Clear", command=self.clear)
        clear_button.grid(row=0, column=1)
        logout_button = tk.Button(homepage_frame, text="Logout", command=self.logout)
        logout_button.grid(row=0, column=2)
        content_label = tk.Label(
            homepage_frame,
            text="Hi, {name}, Welcome to english note".format(
                name=self.account
            )
        )
        content_label.grid(row=1, column=0)
        create_vocabulary_button = tk.Button(
            homepage_frame,
            text="Create Vocabulary",
            command=self.create_vocabulary
        )
        create_vocabulary_button.grid(row=2, column=0)
        review_vocabulary_button = tk.Button(
            homepage_frame,
            text="Review Vocabulary",
            command=self.review_vocabulary,
        )
        review_vocabulary_button.grid(row=2, column=1)
        homepage_frame.pack(anchor=cs.CENTER, fill=cs.X)
        self.homepage_frame = homepage_frame

    def logout(self):
        self.clear()
        transfer.init_login_layout()

    def clear(self):
        # Clear previous content if any
        if self.function_frame is not None:
            self.destroy_widgets(self.function_frame)
            self.function_frame = None

    def destroy_homepage_layout(self):
        self.homepage_frame.destroy()
        self.homepage_frame = None
        self.account = None

    def create_vocabulary(self):
        self.clear()
        self.function_frame = transfer.init_create_vocabulary()

    def review_vocabulary(self):
        self.clear()
        self.function_frame = transfer.init_review_vocabulary()
