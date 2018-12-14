import allure
import pytest
from base.baseDriver import get_driver
from data.data import *
from page.page import Page


class TestLogin:

    def setup(self):
        self.page = Page(get_driver(is_headless=True))
        self.login_page = self.page.LoginPage
        self.login_page.action_open_url(LOGIN_URL)

    def teardown(self):
        self.login_page.action_quit()

    
    @pytest.mark.parametrize('username, password, code', LOGIN_DATA)
    def test_1(self, username, password, code):
        self.login_page.yw_login(username, password, code)
        assert self.page.HomePage.get_login_status()
