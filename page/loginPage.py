from base.baseAction import Action
from element.element import LOGIN_ELEMENT


class LoginPage(Action):

    def input_username(self, username):
        self.action_send_keys(LOGIN_ELEMENT['username_input'], username)

    def input_password(self, pwd):
        self.action_send_keys(LOGIN_ELEMENT['password_input'], pwd)

    def input_code(self, code):
        self.action_send_keys(LOGIN_ELEMENT['code_input'], code)

    def click_login(self):
        self.action_click(LOGIN_ELEMENT['login_button'])

    def yw_login(self, username, password, code):
        self.input_username(username)
        self.input_password(password)
        self.input_code(code)
        self.click_login()
