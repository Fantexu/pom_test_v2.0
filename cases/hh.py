import time

import pytest

from base.baseDriver import get_driver
from page.page import Page


class TestHH:
    def setup(self):
        self.hh = Page(get_driver(True)).HhPage
        self.hh.action_open_url('https://jinshuju.net/f/xVOHwW')

    def teardown(self):
        self.hh.action_quit()

    @pytest.mark.parametrize('a', [i for i in range(100)])
    def test_1(self, a):
        self.hh.yw_1()
        print(a)
        time.sleep(3)
