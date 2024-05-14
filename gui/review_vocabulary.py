# coding=utf-8
import tkinter as tk
import tkinter.constants as cs

from config import Config
from gui.base import BaseGUIFunc
from helpers import helpers


class ReviewVocabularyGUIFunc(BaseGUIFunc):

    def __init__(self, config: Config()):
        self.homepage_func_frame = None
        self.choose_review_date = None
        self.review_date = None
        self.config = config

    def review_vocabulary_layout_init(self):
        # Review Vocabulary Layout
        vocabulary_frame = tk.Frame(relief=cs.RIDGE, borderwidth=5, padx=3, pady=3, width=400, height=400)
        file_names = self.config.exist_vocabulary_files
        self.choose_review_date = tk.StringVar()
        if self.review_date is not None:
            self.choose_review_date.set(self.review_date)
        else:
            self.choose_review_date.set("請選擇")
        review_date_listbox = tk.OptionMenu(vocabulary_frame, self.choose_review_date, *file_names)  # 選單
        review_date_listbox.pack()
        vocabulary_frame.pack(anchor=cs.CENTER, expand=True, fill=cs.BOTH)
        self.choose_review_date.trace('w', self.show)
        self.homepage_func_frame = vocabulary_frame

    def show(self, *_):
        if self.choose_review_date.get() != "請選擇":
            self.review_date = self.choose_review_date.get()
            self.destroy_widgets(self.homepage_func_frame)
            self.review_vocabulary_layout_init()
            # Create a Canvas widget
            data_frame = tk.Frame(self.homepage_func_frame, relief=cs.RIDGE, borderwidth=10, padx=5, pady=5)
            canvas = tk.Canvas(data_frame)

            # Add a scrollbar to the Canvas
            scrollbar_y = tk.Scrollbar(data_frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

            # Link the scrollbar to the Canvas
            canvas.configure(yscrollcommand=scrollbar_y.set)

            # Create a Frame inside the Canvas
            inner_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=inner_frame, anchor=cs.NW)

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            # Bind the event to update the scroll region
            inner_frame.bind("<Configure>", on_configure)
            vocabulary_data = helpers.read_file(self.config.account, self.review_date)
            vocabulary_count = tk.Label(inner_frame, text="Total Vocabulary: {count}".format(count=len(vocabulary_data)))
            vocabulary_count.grid(row=0, column=0)
            count = 0
            row = 1
            for i, (word, pos, explain, sentence) in enumerate(vocabulary_data):
                group_frame = tk.LabelFrame(inner_frame, text=f"Vocabulary")
                group_frame.grid(row=row, column=count % 3, sticky="nsew", padx=5, pady=5)
                tk.Label(group_frame, text="Number: {number}".format(number=count + 1)).pack()
                tk.Label(group_frame, text=f"Vocabulary: {word}").pack()
                tk.Label(group_frame, text=f"Part of Speech: {pos}").pack()
                tk.Label(group_frame, text=f"Explain: {explain}").pack()
                tk.Label(group_frame, text=f"Sentence: {sentence}").pack()
                count += 1
                if count > 2 and count % 3 == 0:  # Start a new row every 3rd group frame=
                    row += 1

            inner_frame.update_idletasks()  # Update inner_frame size
            canvas.config(scrollregion=canvas.bbox("all"))
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            data_frame.pack(fill=tk.BOTH, expand=True)
