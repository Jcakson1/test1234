import pytest
from selenium import webdriver
from ddt import data, ddt, unpack, file_data
from page.login_page.test_login import LoginPath
from selenium.webdriver.common.by import By


@ddt
class TestLogin:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        url = 'http://192.168.98.163/webroot/decision/login'
        cls.driver.get(url)
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

    # @pytest.mark.skip(reason="跳过此测试方法")
    # # @pytest.mark.parametrize("account, password", read_data())
    # def test_001(self, account, password):
    #     S = LOG_PAGE(self.driver)
    #     S.login_succeeded(account, password)
    #     # 添加断言和其他测试逻辑
    @pytest.mark.skip(reason="跳过此测试方法")
    def test_002(self):
        S = LoginPath(self.driver)
        S.login()
