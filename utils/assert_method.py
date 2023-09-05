import allure
import pytest

class assert_method():

    def assert_equal(self,actual, expected, message=None):
        """
        断言实际值与预期值相等
        :param actual: 实际值
        :param expected: 预期值
        :param message: 断言失败时的自定义消息
        """
        assert actual == expected, message or f"预期值为 {expected}，实际值为 {actual}"

    def assert_true(self,condition, message=None):
        """
        断言条件为真
        :param condition: 要断言的条件
        :param message: 断言失败时的自定义消息
        """
        assert condition, message or "条件不为真"

    def assert_false(self,condition, message=None):
        """
        断言条件为假
        :param condition: 要断言的条件
        :param message: 断言失败时的自定义消息
        """
        assert not condition, message or "条件不为假"

    # 将自定义的断言函数注册为 pytest 的自定义断言
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self,item, call):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == "call" and rep.failed:
            mode = "a" if hasattr(item, "_allure_attach") else "w"
            with allure.step("添加断言截图"):
                allure.attach(item._testcase, "失败截图", allure.attachment_type.PNG)
#
# if __name__ == '__main__':
#     Y = 1
#     X = 1
#     assert_method().assert_equal(X,Y,'相等')


