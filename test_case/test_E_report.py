import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from ddt import data, ddt, unpack, file_data
from test_case.test_login import TestLogin
from page.login_page.test_login import LoginPath
from page.Engineering_report.E_report import Eng_report
from page.Engineering_report.Engineering_inspection import EngReport as Report
from utils.assert_method import assert_method


@allure.parent_suite('我是parent_suite')
@allure.suite('我是suite')
@allure.sub_suite("我是sub_suite")
@allure.epic("我是epic 一级")
@allure.feature('我是feature二级')
@allure.story('我是story三级')
class Test_report:
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

    @allure.title('我是标题')
    @allure.id("12345")
    @allure.link("http://example.com/issue/123")
    @allure.label("custom-label", "my-label")
    @allure.issue("BUG-123")
    @allure.description("这是一个测试用例的描述")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("smoke", "regression")
    @allure.testcase("http://example.com/testcase/123")
    @allure.description_html("<h1>这是HTML描述</h1>")
    @pytest.mark.skip(reason="临时跳过，等待修复")
    def test_001(self):
        # 登录后的方法调用
        S = LoginPath(self.driver)
        S.login()
        S1 = Eng_report(self.driver)
        # S1.commendatory_letter_enter()
        S1.commendatory_letter_select_time()

        # S1.commendatory_letter_select_branch_office()
        # S1.commendatory_letter_select_Approval_Status()
        # S1.commendatory_letter_select_Commending_unit()
        # S1.commendatory_letter_select_entry_name()
        # S1.commendatory_letter_export()
        # S1.commendatory_adding_record()
    @allure.title('我是标题')
    @allure.id("12345")
    @allure.link("http://example.com/issue/123")
    @allure.label("custom-label", "my-label")
    @allure.issue("BUG-123")
    @allure.description("这是一个测试用例的描述")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("smoke", "regression")
    @allure.testcase("http://example.com/testcase/123")
    @allure.description_html("<h1>这是HTML描述</h1>")
    def test_002(self):
        pass
        S = LoginPath(self.driver)
        S.login()
        S2 = Report(self.driver)
        S2.Generic_methods()
        time.sleep(3)