# coding=utf-8
import os
import yaml
from typing import List, Dict

from helpers import helpers


class Config:

    def __init__(self):
        self.account = None
        self.name = None
        self.email = None
        self.exist_vocabulary_files = list()
        self.mapping_between_file_and_vocabulary_count = dict()
        self.account_vocabulary = list()

    def init_account_data(self, account: dict, current_date: str):
        self.account = account["account"]
        self.name = account["name"]
        self.email = account["email"]
        helpers.check_and_create_file(self.account, current_date)
        mapping_between_file_and_vocabulary_count = dict()
        exist_vocabulary_files = list()
        file_names = helpers.list_file_names(self.account)
        vocabulary = list()
        for file_name in file_names:
            file_data = helpers.read_file(self.account, file_name)
            if file_data:
                exist_vocabulary_files.append(file_name)
                mapping_between_file_and_vocabulary_count[file_name] = len(file_data)
                for i, (word, translation, _, _, _) in enumerate(file_data):
                    vocabulary.append(dict(
                        word=word,
                        translation=translation
                    ))
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
        self.account_vocabulary = vocabulary

    def _check_different_between_account_file_and_guest_file(self):
        pass


def init_system_dir():
    os.makedirs(".env", exist_ok=True)
    os.makedirs("file", exist_ok=True)
    # Path to the YAML file
    file_name = 'system.yaml'
    data = {
        'version': '0.0.1',
        'last_login': ''
    }
    # Write data to the YAML file
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            yaml.dump(data, file)
    # Assuming you have a YAML file named 'data.yaml'
    with open(file_name, 'r') as file:
        yaml_data = yaml.safe_load(file)
        print(yaml_data)

