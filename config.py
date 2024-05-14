# coding=utf-8
from typing import List, Dict

from helpers import helpers


class Config:

    def __init__(self):
        self.account = None
        self.email = None
        self.exist_vocabulary_files = list()
        self.mapping_between_file_and_vocabulary_count = dict()
        self.account_vocabulary = list()

    def set_account(self, account: str):
        self.account = account

    def init_account_data(self):
        if self.account is not None:
            mapping_between_file_and_vocabulary_count = dict()
            exist_vocabulary_files = list()
            file_names = helpers.list_file_names(self.account)
            vocabulary = list()
            for file_name in file_names:
                file_data = helpers.read_file(self.account, file_name)
                if file_data:
                    exist_vocabulary_files.append(file_name)
                    mapping_between_file_and_vocabulary_count[file_name] = len(file_data)
                    for i, (word, _, _, _) in enumerate(file_data):
                        vocabulary.append(word)
                else:
                    mapping_between_file_and_vocabulary_count[file_name] = 0

            self._set_file_list(exist_vocabulary_files)
            self._set_mapping_between_file_and_vocabulary_count(mapping_between_file_and_vocabulary_count)
            self._set_account_vocabulary(vocabulary)

    def _set_file_list(self, exist_vocabulary_files: List):
        self.exist_vocabulary_files = exist_vocabulary_files

    def _set_mapping_between_file_and_vocabulary_count(self, mapping_between_file_and_vocabulary_count: Dict):
        self.mapping_between_file_and_vocabulary_count = mapping_between_file_and_vocabulary_count

    def _set_account_vocabulary(self, vocabulary):
        self.account_vocabularies = vocabulary

    def _check_different_between_account_file_and_guest_file(self):
        pass
