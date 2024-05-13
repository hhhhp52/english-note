# coding=utf-8
import tkinter as tk
import tkinter.constants as cs

from gui.base import BaseGUIFunc
from helpers import helpers


class TestingVocabularyGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.homepage_func_frame = None

    def testing_vocabulary_layout_init(self):
        testing_function_frame = tk.Frame(relief=cs.RIDGE, borderwidth=5, padx=3, pady=3, width=400, height=400)
        choose_question_button = tk.Button(testing_function_frame, text="選擇題", command=self.choose_question)
        choose_question_button.grid(row=0, column=0)
        fill_out_question_button = tk.Button(testing_function_frame, text="填空題", command=self.fill_out_question)
        fill_out_question_button.grid(row=0, column=1)
        testing_function_frame.pack(anchor=cs.CENTER, expand=True, fill=cs.BOTH)
        self.homepage_func_frame = testing_function_frame

    def choose_question(self):
        pass

    def fill_out_question(self):
        pass
