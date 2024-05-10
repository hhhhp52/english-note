import os
import csv
from datetime import datetime
from typing import List


def check_and_create_file(current_date: str):
    # Construct the file name using the current date
    file_name = f"{current_date}.csv"

    # Check if the file exists
    file_path = os.path.join("file", file_name)
    if os.path.exists(file_path):
        print(f"The file '{file_name}' already exists.")
    else:
        # Create the file if it doesn't exist
        os.makedirs("file", exist_ok=True)
        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write header if needed
            csv_writer.writerow(["Vocabulary", "Part of speech", "Explain", "Sentence"])
        print(f"The file '{file_name}' has been created.")


def open_and_write_file(current_date: str, vocabulary: str, part_of_speech: List, explain:str, sentence:str):
    check_and_create_file(current_date)

    # Construct the file name using the current date
    file_name = f"{current_date}.csv"

    # Check if the file exists
    file_path = os.path.join("file", file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                part_of_speech_str = ', '.join(part_of_speech)
                csv_writer.writerow([vocabulary, part_of_speech_str, explain, sentence])
        except Exception as e:
            print(e)
            return False
    return True


def list_file_names():
    file_names = os.listdir("file")
    return file_names


def read_file(file_name):
    file_path = os.path.join("file", file_name)
    data = list()
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            # Skip the header row
            next(csv_reader)
            for row in csv_reader:
                data.append(row)
    else:
        print(f"The file '{file_name}' does not exist.")
        return None
    return data
