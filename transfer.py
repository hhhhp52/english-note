# coding=utf-8
import gui

from config import Config
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")
config = Config()


class FuncNodeAdapter:
    def __init__(self):
        self.login_gui_func = gui.login.LoginGUIFunc()
        self.create_vocabulary_func = gui.create_vocabulary.CreateVocabularyGUIFunc(current_date)
        self.review_vocabulary_func = gui.review_vocabulary.ReviewVocabularyGUIFunc()
        self.homepage_gui_func = gui.homepage.HomePageGUIFunc()
        self.setting_gui_func = gui.setting.SettingGUIFunc()
        self.testing_gui_func = gui.testing_vocabulary.TestingVocabularyGUIFunc()
        self.latest_func = None


func_node = FuncNodeAdapter()


def init_homepage_layout(account):
    func_node.login_gui_func.destroy_login_layout()
    func_node.homepage_gui_func.account = account
    config.account = account
    func_node.homepage_gui_func.homepage_layout_init()


def init_login_layout(first_init=False):
    if not first_init:
        func_node.homepage_gui_func.destroy_homepage_layout()
    homepage_func_frame_destroy()
    func_node.latest_func = None
    func_node.login_gui_func.login_layout_init()


def homepage_func_frame_destroy():
    if func_node.latest_func is not None:
        if func_node.latest_func.homepage_func_frame:
            func_node.latest_func.homepage_func_frame.destroy()


def init_create_vocabulary():
    homepage_func_frame_destroy()
    func_node.latest_func = func_node.create_vocabulary_func
    frame = func_node.create_vocabulary_func.create_vocabulary_layout_init()
    return frame


def init_review_vocabulary():
    homepage_func_frame_destroy()
    func_node.latest_func = func_node.review_vocabulary_func
    frame = func_node.review_vocabulary_func.review_vocabulary_layout_init()
    return frame


def init_setting():
    homepage_func_frame_destroy()
    func_node.latest_func = func_node.setting_gui_func
    frame = func_node.setting_gui_func.setting_layout_init(config)
    return frame


def init_testing_vocabulary():
    homepage_func_frame_destroy()
    func_node.latest_func = func_node.testing_gui_func
    frame = func_node.testing_gui_func.testing_vocabulary_layout_init()
    return frame

