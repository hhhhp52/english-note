# coding=utf-8
import tkinter as tk

import config
import transfer


def _create_tk():
    app = tk.Tk()
    app.title("Vocabulary App")
    app.geometry("1024x768")  # width, height
    app.resizable(False, False)
    return app


if __name__ == '__main__':
    app = _create_tk()
    config.init_system_dir()
    transfer.init_login_layout(first_init=True)
    app.mainloop()
