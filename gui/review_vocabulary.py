# coding=utf-8
import tkinter as tk
import tkinter.constants as cs

from gui.base import BaseGUIFunc
from helpers import helpers


class ReviewVocabularyGUIFunc(BaseGUIFunc):

    def __init__(self):
        self.vocabulary_frame = None
        self.choose_review_date = None
        self.review_date = None

    def review_vocabulary_layout_init(self):
        # Review Vocabulary Layout
        vocabulary_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        file_names = helpers.list_file_names()
        self.choose_review_date = tk.StringVar()
        if self.review_date is not None:
            self.choose_review_date.set(self.review_date)
        else:
            self.choose_review_date.set("請選擇")
        review_date_listbox = tk.OptionMenu(vocabulary_frame, self.choose_review_date, *file_names)  # 選單
        review_date_listbox.grid(row=0, column=0)
        vocabulary_frame.pack(side=cs.TOP)
        self.choose_review_date.trace('w', self.show)
        self.vocabulary_frame = vocabulary_frame

    def show(self, *_):
        if self.choose_review_date.get() != "請選擇":
            self.review_date = self.choose_review_date.get()
            self.destroy_widgets(self.vocabulary_frame)
            self.review_vocabulary_layout_init()
            tk.Label(self.vocabulary_frame, text="Vocabulary:").grid(row=1, column=0)
            tk.Label(self.vocabulary_frame, text="Part of Speech:").grid(row=1, column=1)
            tk.Label(self.vocabulary_frame, text="Explain:").grid(row=1, column=2)
            tk.Label(self.vocabulary_frame, text="Sentence:").grid(row=1, column=3)

            vocabulary_data = helpers.read_file(self.review_date)

            for i, (word, pos, explain, sentence) in enumerate(vocabulary_data, start=2):
                tk.Label(self.vocabulary_frame, text=word).grid(row=i, column=0)
                tk.Label(self.vocabulary_frame, text=pos).grid(row=i, column=1)
                tk.Label(self.vocabulary_frame, text=explain).grid(row=i, column=2)
                tk.Label(self.vocabulary_frame, text=sentence).grid(row=i, column=3)