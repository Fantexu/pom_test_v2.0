from selenium.webdriver.common.by import By
from element.element import HH_ELEMENT
from base.baseAction import Action
import time


class HhPage(Action):
    def select_1_gz(self):
        self.action_select_by_index(HH_ELEMENT['select_1'], 5)

    def select_2_(self):
        self.action_select_by_index(HH_ELEMENT['select_2'], 10)

    def button_3(self):
        self.action_click(HH_ELEMENT['option_3'])

    def button_4(self):
        self.action_click(HH_ELEMENT['option_4'])

    def button_5(self):
        self.action_click(HH_ELEMENT['option_5'])

    def button_6(self):
        self.action_click(HH_ELEMENT['option_6'])

    def button_7(self):
        self.action_click(HH_ELEMENT['option_7'])

    def input_8(self, text):
        self.action_send_keys(HH_ELEMENT['input_8'], text)

    def button_sumbit(self):
        self.action_click(HH_ELEMENT['submit'])

    def yw_1(self):
        self.select_1_gz()
        self.select_2_()
        self.button_3()
        self.button_4()
        self.button_5()
        self.button_6()
        self.button_7()
        self.input_8('万一真找不到工作呢')
        self.button_sumbit()


if __name__ == '__main__':
    from base.baseDriver import get_driver
    h = HhPage(get_driver())
    h.action_open_url('https://jinshuju.net/f/xVOHwW')
    h.button_3()
    time.sleep(3)
    h.action_quit()