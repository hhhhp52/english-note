# coding=utf-8
import tkinter as tk
from datetime import datetime

import transfer
from helpers import helpers


def _create_tk():
    app = tk.Tk()
    app.title("Vocabulary App")
    app.geometry("1024x768")  # width, height
    app.resizable(False, False)
    return app


if __name__ == '__main__':
    app = _create_tk()
    transfer.init_login_layout(first_init=True)
    # Get the current date in the format YYYY-MM-DD
    current_date = datetime.now().strftime("%Y-%m-%d")
    helpers.check_and_create_file(current_date)
    app.mainloop()
