from base.baseDriver import get_driver
from page.hhpage import HhPage
from page.homePage import HomePage
from page.loginPage import LoginPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def LoginPage(self):
        return LoginPage(self.driver)

    @property
    def HomePage(self):
        return HomePage(self.driver)

    @property
    def HhPage(self):
        return HhPage(self.driver)