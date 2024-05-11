# coding=utf-8
import tkinter as tk
import tkinter.constants as cs
from gui.base import BaseGUIFunc


class SettingGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.homepage_func_frame = None
        self.email_entry = None

    def setting_layout_init(self, config):
        setting_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2)
        data_frame = tk.Frame(setting_frame, relief=cs.RIDGE, borderwidth=1)
        setting_title_label = tk.Label(data_frame, anchor=cs.CENTER, text="Setting")
        setting_title_label.grid()
        email_label = tk.Label(data_frame, anchor=cs.CENTER, text="Email")
        email_label.grid(row=1, column=0)
        email = tk.StringVar()
        email.set(config.email)
        email_entry = tk.Entry(data_frame, textvariable=email)
        email_entry.grid(row=1, column=1)
        create_button = tk.Button(data_frame, anchor=cs.CENTER, text="Send", command=self.send)
        create_button.grid(row=2, column=0)
        clear_button = tk.Button(data_frame, anchor=cs.CENTER, text="Clear", command=self.clear)
        clear_button.grid(row=2, column=1)
        data_frame.pack(anchor=cs.CENTER, expand=True)
        setting_frame.pack(anchor=cs.CENTER, expand=True, fill=cs.BOTH)
        self.homepage_func_frame = setting_frame
        self.email_entry = email_entry

    def send(self):
        pass

    def clear(self):
        pass
