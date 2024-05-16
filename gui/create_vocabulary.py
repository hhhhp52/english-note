# coding=utf-8
import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox

from config import Config
from gui.base import BaseGUIFunc
from helpers import helpers


class CreateVocabularyGUIFunc(BaseGUIFunc):

    def __init__(self, config: Config(), current_date: str):
        self.homepage_func_frame = None
        self.word_entry = None
        self.translation_entry = None
        self.part_of_speech_listbox = None
        self.explain_entry = None
        self.sentence_entry = None
        self.current_date = current_date
        self.config = config

    def create_vocabulary_layout_init(self):
        vocabulary_frame = tk.Frame(relief=cs.RIDGE, borderwidth=5, padx=3, pady=3, width=400, height=400)
        vocabulary_title_label = tk.Label(vocabulary_frame, text="Vocabulary Entry Panel")
        vocabulary_title_label.grid(row=0, column=0)
        part_of_speech_list = ["Noun", "Verb", "Adjective", "Adverb", "Preposition"]
        word_label = tk.Label(vocabulary_frame, text="Word")
        word_label.grid(row=2, column=0)
        word_entry = tk.Entry(vocabulary_frame)
        word_entry.grid(row=2, column=1)
        translation_label = tk.Label(vocabulary_frame, text="Translation")
        translation_label.grid(row=3, column=0)
        translation_entry = tk.Entry(vocabulary_frame)
        translation_entry.grid(row=3, column=1)
        part_of_speech_label = tk.Label(vocabulary_frame, text="Part of speech")
        part_of_speech_label.grid(row=4, column=0)
        part_of_speech_listbox = tk.Listbox(vocabulary_frame, selectmode=tk.MULTIPLE)
        for pos in part_of_speech_list:
            part_of_speech_listbox.insert(tk.END, pos)
        part_of_speech_listbox.grid(row=4, column=1)
        explain_label = tk.Label(vocabulary_frame, text="Explain")
        explain_label.grid(row=5, column=0)
        explain_entry = tk.Entry(vocabulary_frame)
        explain_entry.grid(row=5, column=1)
        sentence_label = tk.Label(vocabulary_frame, text="Sentence")
        sentence_label.grid(row=6, column=0)
        sentence_entry = tk.Entry(vocabulary_frame)
        sentence_entry.grid(row=6, column=1)
        create_button = tk.Button(vocabulary_frame, text="Send", command=self.send)
        create_button.grid(row=7, column=0)
        clear_button = tk.Button(vocabulary_frame, text="Clear", command=self.clear)
        clear_button.grid(row=7, column=1)
        vocabulary_frame.pack(anchor=cs.CENTER, expand=True, fill=cs.BOTH)
        self.homepage_func_frame = vocabulary_frame
        self.word_entry = word_entry
        self.translation_entry = translation_entry
        self.part_of_speech_listbox = part_of_speech_listbox
        self.explain_entry = explain_entry
        self.sentence_entry = sentence_entry

    def clear(self, auto_clear=False):
        if not auto_clear:
            word_entry = self.word_entry.get()
            translation_entry = self.translation_entry.get()
            explain_entry = self.explain_entry.get()
            sentence_entry = self.sentence_entry.get()
            # Check if any data is empty
            if not word_entry or not translation_entry or not explain_entry or not sentence_entry:
                result = messagebox.askquestion("Clear Data", "Are you sure you want to clear all data?")
                if result == "yes":
                    self.destroy_widgets(self.homepage_func_frame)
                    self.create_vocabulary_layout_init()
        else:
            self.destroy_widgets(self.homepage_func_frame)
            self.create_vocabulary_layout_init()

    def send(self):
        vocabulary_entry = self.word_entry.get()
        translation_entry = self.translation_entry.get()
        part_of_speech_listbox = self.part_of_speech_listbox.curselection()
        explain_entry = self.explain_entry.get()
        sentence_entry = self.sentence_entry.get()

        # Check if any data is empty
        if not vocabulary_entry or not translation_entry or not part_of_speech_listbox or not explain_entry or not sentence_entry:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Get selected part of speech values
        selected_part_of_speech = [self.part_of_speech_listbox.get(index) for index in part_of_speech_listbox]

        if not helpers.open_and_write_file(
            self.config.account,
            self.current_date,
            vocabulary_entry,
            translation_entry,
            selected_part_of_speech,
            explain_entry,
            sentence_entry
        ):
            messagebox.showerror("Failed", "Create Failed")
        else:
            file_name = f"{self.current_date}.csv"
            if file_name not in self.config.exist_vocabulary_files:
                self.config.exist_vocabulary_files.append(file_name)
            if self.config.mapping_between_file_and_vocabulary_count.get(file_name):
                count = self.config.mapping_between_file_and_vocabulary_count.get(file_name) + 1
                self.config.mapping_between_file_and_vocabulary_count[file_name] = count
            self.config.account_vocabulary.append(dict(word=vocabulary_entry, translation=translation_entry))
            messagebox.showinfo("Success", "Create Success")
            self.clear(auto_clear=True)

