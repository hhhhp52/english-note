# coding=utf-8
import gui
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")
login_gui_func = gui.login.LoginGUIFunc()
create_vocabulary_func = gui.create_vocabulary.CreateVocabularyGUIFunc(current_date)
review_vocabulary_func = gui.review_vocabulary.ReviewVocabularyGUIFunc()
homepage_gui_func = gui.homepage.HomePageGUIFunc()


def init_homepage_layout(account):
    login_gui_func.destroy_login_layout()
    homepage_gui_func.account = account
    homepage_gui_func.homepage_layout_init()


def init_login_layout(first_init=False):
    if not first_init:
        homepage_gui_func.destroy_homepage_layout()
    login_gui_func.login_layout_init()


def init_create_vocabulary():
    if review_vocabulary_func.vocabulary_frame:
        review_vocabulary_func.vocabulary_frame.destroy()
    frame = create_vocabulary_func.create_vocabulary_layout_init()
    return frame


def init_review_vocabulary():
    if create_vocabulary_func.vocabulary_frame:
        create_vocabulary_func.vocabulary_frame.destroy()
    frame = review_vocabulary_func.review_vocabulary_layout_init()
    return frame
