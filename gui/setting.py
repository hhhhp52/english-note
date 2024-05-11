# coding=utf-8
import tkinter as tk
import tkinter.constants as cs
import transfer
from gui.base import BaseGUIFunc


class SettingGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.homepage_func_frame = None
        self.email_entry = None

    def setting_layout_init(self, config):
        setting_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        setting_title_label = tk.Label(setting_frame, text="Setting")
        setting_title_label.grid(row=0, column=0)
        email_label = tk.Label(setting_frame, text="Email")
        email_label.grid(row=2, column=0)
        email_entry = tk.Entry(setting_frame, textvariable=config.account)
        email_entry.grid(row=2, column=1)
        create_button = tk.Button(setting_frame, text="Send", command=self.send)
        create_button.grid(row=3, column=0)
        clear_button = tk.Button(setting_frame, text="Clear", command=self.clear)
        clear_button.grid(row=3, column=1)
        setting_frame.pack(anchor=cs.CENTER, expand=True)
        self.homepage_func_frame = setting_frame
        self.email_entry = email_entry

    def send(self):
        pass

    def clear(self):
        pass
