from base.baseAction import Action
from element.element import *


class HomePage(Action):

    def login_click(self):
        self.action_click(HOME_ELEMENT['login_button'])

    def logout_click(self):
        self.action_click(HOME_ELEMENT['logout_button'])

    def get_login_status(self):
        ele = self.action_find_element(HOME_ELEMENT['logout_button'], is_screen=False)
        if not ele:
            return False
        else:
            return True
