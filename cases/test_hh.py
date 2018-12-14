import allure
import pytest


class TestHh:
    def setup(self):
        pass

    def teardown(self):
        pass

    # @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    # @allure.step(title='测试用例hh')
    # def test_hh(self):
    #     allure.attach('步骤描述', '打印什么什么')
    #     print('adsad')
    #     # allure.attach('步骤描述', '断言结果', '试验')
    #     # assert True

    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # @allure.step(title='测试用例22')
    # def test_22(self):
    #     allure.attach('步骤描述', '随便啦')
    #     print('随便啦')

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title='测试用例22')
    def test_22(self):
        print('随便啦')
        