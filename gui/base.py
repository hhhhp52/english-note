# coding=utf-8
class BaseGUIFunc:
    @staticmethod
    def destroy_widgets(*widgets):
        for widget in widgets:
            if widget is not None:
                widget.destroy()
