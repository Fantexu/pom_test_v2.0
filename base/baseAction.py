import os

import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.baseDriver import get_driver


SCREENSHOT = os.path.dirname(__file__)+'/../screenshot/'


class Action:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = get_driver()

    def action_open_url(self, url):
        self.driver.get(url)

    def action_quit(self):
        self.driver.quit()

    def action_find_element(self, loc, timeout=30, poll_frequency=0.1, is_screen=True):
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
        except:
            if is_screen:
                self.action_get_screen('元素查找失败')
            else:
                return False

    def action_get_screen(self, text):
        self.driver.save_screenshot(os.path.join(SCREENSHOT, '{}{}.png'.format(text, time.strftime('%Y_%m_%d-%H_%M_%S'))))

    def action_send_keys(self, loc, text, is_clear=True):
        ele = self.action_find_element(loc)
        if is_clear:
            ele.clear()
        ele.send_keys(text)

    def action_click(self, loc):
        self.action_find_element(loc).click()

    def action_select_by_index(self, loc, index):
        Select(self.action_find_element(loc)).select_by_index(index)

if __name__ == '__main__':
    demo = Action(get_driver())
    demo.action_open_url('http://localhost/index.php/Home/user/login.html')
    demo.action_send_keys((By.ID, 'username'), '12312412512')
    demo.action_click((By.XPATH, '//a[@name="sbtbutton"]'))
    time.sleep(5)
    demo.driver.quit()
