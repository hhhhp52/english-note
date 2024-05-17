# coding=utf-8
import random
import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox
from typing import List

from config import Config
from gui.base import BaseGUIFunc


class QuestionNode:
    def __init__(self, vocabulary_words: List, testing_way: str, testing_size: int):
        self.size = testing_size
        random.sample(
            vocabulary_words,
            testing_size if len(vocabulary_words) >= 5 else len(vocabulary_words)
        )
        self.size = testing_size if len(vocabulary_words) >= 5 else len(vocabulary_words)
        self.way = testing_way
        self.previous = 0
        self.next = 1

        if self.way == "fill_out":
            self.testing_vocabulary_words = self._set_fill_out_data(self.size, vocabulary_words)
        else:
            self.testing_vocabulary_words = self._set_choose_data(self.size, vocabulary_words)

    def _set_fill_out_data(self, testing_size, vocabulary_words):
        testing_data = list()
        testing_vocabulary_words = random.sample(
            vocabulary_words,
            testing_size if len(vocabulary_words) >= 5 else len(vocabulary_words)
        )
        for word in testing_vocabulary_words:
            data = dict(
                word=word.get("word"),
                translation=word.get("translation"),
                answer=None,
                correct=False
            )
            testing_data.append(data)
        return testing_data

    def _set_choose_data(self, testing_size, vocabulary_words):
        testing_data = list()
        return testing_data

    def move_to_previous(self):
        if self.previous > 0:
            self.previous -= 1
            self.next -= 1

    def save_answer(self, answer):
        self.testing_vocabulary_words[self.previous]["answer"] = answer
        if self.testing_vocabulary_words[self.previous]["word"] == answer:
            self.testing_vocabulary_words[self.previous]["correct"] = True

    def move_to_next(self):
        if self.next < self.size:
            self.previous += 1
            self.next += 1

    def get_data(self):
        return self.testing_vocabulary_words[self.previous]

    def get_result(self):
        correct_count = 0
        for data in self.testing_vocabulary_words:
            if data["correct"]:
                correct_count += 1

        result = dict(
            total=self.size,
            correct=correct_count
        )
        return result


class TestingVocabularyGUIFunc(BaseGUIFunc):

    def __init__(self, config: Config()):
        self.homepage_func_frame = None
        self.testing_frame = None
        self.config = config
        self.question = None
        self.testing_way = None

    def testing_vocabulary_layout_init(self):
        testing_function_frame = tk.Frame(relief=cs.RIDGE, borderwidth=5, padx=3, pady=3, width=400, height=400)
        # Create a frame for buttons at the top center
        button_frame = tk.Frame(testing_function_frame)
        button_frame.pack(pady=10, anchor=tk.N)
        choose_question_button = tk.Button(button_frame, text="選擇題", command=self.choose_question_init)
        choose_question_button.pack(side=cs.LEFT)
        fill_out_question_button = tk.Button(button_frame, text="填空題", command=self.fill_out_init)
        fill_out_question_button.pack(side=cs.LEFT)
        testing_function_frame.pack(expand=True, fill=cs.BOTH)
        self.homepage_func_frame = testing_function_frame

    def choose_question_init(self):
        if self.config.account_vocabulary:
            if self.testing_frame:
                self.destroy_widgets(self.testing_frame)
                self.testing_frame = None
            self.question = None
            self.testing_way = "choose"
            self.question = QuestionNode(
                vocabulary_words=self.config.account_vocabulary,
                testing_way=self.testing_way,
                testing_size=5
            )
            self.choose_question(self.question.get_data())
        else:
            messagebox.showinfo("Notice", "There isn't any vocabulary to test")

    def fill_out_init(self):
        if self.config.account_vocabulary:
            if self.testing_frame:
                self.destroy_widgets(self.testing_frame)
                self.testing_frame = None
            self.question = None
            self.testing_way = "fill_out"
            self.question = QuestionNode(
                vocabulary_words=self.config.account_vocabulary,
                testing_way=self.testing_way,
                testing_size=5
            )
            self.fill_out_question(self.question.get_data())
        else:
            messagebox.showinfo("Notice", "There isn't any vocabulary to test")

    def choose_question(self, data):
        data_frame = tk.Frame(self.homepage_func_frame, relief=cs.RIDGE, borderwidth=10, padx=5, pady=5)

    def fill_out_question(self, data):
        self.testing_frame = tk.Frame(self.homepage_func_frame, relief=cs.RIDGE, borderwidth=10, padx=5, pady=5)
        inner_frame = tk.Frame(self.testing_frame)
        inner_frame.pack(pady=10, anchor=tk.N)
        vocabulary_word_label = tk.Label(
            inner_frame,
            text="Question Word: {word}".format(
                word=(data.get("word").replace(
                    data.get("word")[1:-1], "_"))))
        vocabulary_word_label.grid(row=0, column=0)
        translation_label = tk.Label(
            inner_frame,
            text="Question Translation: {translation}".format(
                translation=(data.get("translation"))))
        translation_label.grid(row=1, column=0)
        if data.get("answer"):
            answer = tk.StringVar()
            answer.set(data.get("answer"))
            answer_entry = tk.Entry(
                inner_frame,
                textvariable=answer
            )
        else:
            answer_entry = tk.Entry(
                inner_frame
            )
        answer_entry.grid(row=2, column=0)
        func_button_frame = tk.Frame(self.testing_frame)
        func_button_frame.pack(pady=10, fill=cs.X, anchor=cs.S)
        if self.question.next < self.question.size:
            if self.question.previous != 0:
                previous_button = tk.Button(func_button_frame, text="previous", command=self._previous)
                previous_button.pack(side=cs.LEFT)
            next_button = tk.Button(func_button_frame, text="next", command=self._next)
            next_button.pack(side=cs.RIGHT)
        else:
            if self.question.size > 1:
                previous_button = tk.Button(func_button_frame, text="previous", command=self._previous)
                previous_button.pack(side=cs.LEFT)
            send_button = tk.Button(func_button_frame, text="send", command=self._send)
            send_button.pack(side=cs.RIGHT)

        self.testing_frame.pack()
        self.answer_entry = answer_entry

    def _previous(self):
        self.question.move_to_previous()
        self.destroy_widgets(self.testing_frame)
        self._reset_layout()

    def _next(self):
        self.question.save_answer(self.answer_entry.get())
        self.question.move_to_next()
        self.destroy_widgets(self.testing_frame)
        self._reset_layout()

    def _send(self):
        result = self.question.get_result()
        messagebox.showinfo("Result", "Correct Count: {correct}/{total}".format(
            correct=result["correct"], total=result["total"]
        ))
        self.destroy_widgets(self.homepage_func_frame)
        self.testing_vocabulary_layout_init()

    def _reset_layout(self):
        if self.testing_way == "fill_out":
            self.fill_out_question(self.question.get_data())
        else:
            self.choose_question(self.question.get_data())
