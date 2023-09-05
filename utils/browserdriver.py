import sys
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class ElementLocators:

    def __init__(self, driver,timeout=10):

        self.driver = driver
        self.timeout = timeout

    # def find_element(self,by,value):
    #     self.driver.find_element(by,value)

    # 显示等待定位元素方法，如果定位失败，自动重新连接
    def wait_for_element_visible(self, by, value, max_attempts=3, retry_interval=1):
        """
        等待元素可见并进行重复定位的方法
        :param by: 定位方法，如 'xpath', 'css_selector', 'id' 等
        :param value: 定位元素的值
        :param max_attempts: 最大重试次数，默认为 3
        :param retry_interval: 重试间隔时间（秒），默认为 1 秒
        :return: 定位成功则返回定位的元素对象，否则抛出 TimeoutException 异常
        """
        attempts = 0
        while attempts < max_attempts:
            try:
                wait = WebDriverWait(self.driver, self.timeout)
                element = wait.until(EC.visibility_of_element_located((eval(by), value)))
                return element

            except NoSuchElementException as e:
                print(f"Failed to locate element on attempt {attempts + 1}: {e}")
                attempts += 1
                time.sleep(retry_interval)

        # 如果重试次数耗尽仍未找到元素，则抛出 TimeoutException 异常
        raise TimeoutException(f"Element not visible after {max_attempts} attempts: {by}={value}")

    def click_element(self, by, value):
        element = self.wait_for_element_visible(by, value)
        element.click()

    def input_text(self, by, value, text):
        element = self.wait_for_element_visible(by, value)
        # 清空输入框，重置输入参数
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, value):
        element = self.wait_for_element_visible(by, value)
        return element.text

    # 定位元素的方法
    def find_element_out(self, locators, element_name):
        locator = locators.get(element_name)
        if locator:
            locator_type, locator_value = locator.split(",", 1)
            # 根据 locator_type 和 locator_value 定位元素，并返回元素对象
            element = self.wait_for_element_visible(locator_type, locator_value)
            return element
        else:
            raise ValueError(f"Element '{element_name}' not found in locators")
    # 元素是否可见
    def is_element_visible(self,by, value):
        try:
            element = self.wait_for_element_visible(by, value)
            return element.is_displayed()
        except:
            return False

    # 元素是否可点击
    def is_element_enabled(self, by, value):
        try:
            element = self.wait_for_element_visible(by, value)
            return element.is_enabled()
        except:
            return False

    # 鼠标移动到该元素
    def move_to_element(self, by, value):

        element = self.wait_for_element_visible(by, value)
        if element.is_displayed():
            element.click()
        else:
            ActionChains(self.driver).move_to_element(element).click().perform()

    # 等待元素不可见

    def invisibility_of_element_located(self, by, value, timeout=10):
        """
        使用 ExpectedConditions 中的 invisibility_of_element_located 方法等待元素不可见
        :param by: 定位方式，例如 By.ID、By.XPATH 等
        :param value: 定位表达式
        :param timeout: 最大等待时间，默认为 10 秒
        :return: None
        """
        try:
            wait = self.wait_for_element_visible(by,value)
        except Exception as e:
            # 记录错误信息或打印错误日志
            self.logger.error(f"等待元素不可见时发生错误：{e}")

    # 切换窗口
    def keep_only_tab_A(self,by,value):
        current_window_handle = self.driver.current_window_handle  # 获取当前窗口句柄

        # 保存所有窗口句柄
        all_window_handles = self.driver.window_handles

        # 切换到 A 标签页
        for window_handle in all_window_handles:
            self.driver.switch_to.window(window_handle)

            # 尝试定位 A 元素
            elements_A = self.wait_for_element_visible(by,value)

            if len(elements_A) > 0:
                # 如果定位到 A 元素，继续其他操作，这里仅演示点击 A 元素
                elements_A[0].click()  # 假设执行了某些操作
            else:
                # 关闭除 A 标签页以外的其他标签页
                if window_handle != current_window_handle:
                    self.driver.close()

        # 切换回 A 标签页
        self.driver.switch_to.window(current_window_handle)

            # 切换回原来的标签页
            # self.driver.switch_to.window(current_window_handle)

    # 执行双击操作
    def double_click(self, by, value, interval=0.2):
        """
        模拟双击鼠标操作
        参数:
        by: 元素定位的方式，如 'id', 'name', 'xpath' 等
        value: 元素定位的值
        interval (float): 两次点击之间的时间间隔
        返回:
        成功双击返回 True，未找到元素返回 False
        """
        try:
            element = self.wait_for_element_visible(by, value)

            # 创建 ActionChains 对象，执行双击操作
            action_chains = ActionChains(self.driver)
            action_chains.double_click(element).pause(interval).perform()
            return True
        except NoSuchElementException as e:
            print(f"Exception message: {e}")
            return False

    # 执行enter操作
    def press_enter_key(self, element):
        """
        模拟按下 Enter 键操作
        参数:
        element: 要在其上执行 Enter 按键操作的元素
        返回:
        None
        """
        element.send_keys(Keys.ENTER)

    # select 下拉框选择第一个
    def select_first_option(self, element):

        select = Select(element)
        select.select_by_index(0)
    #
    def select_from_dropdown_by_text(self, by, value, option_text):
        select_element = self.wait_for_element_visible(by,value)
        dropdown = Select(select_element)
        dropdown.select_by_visible_text(option_text)
    # 通过上传附件方法
    def click_upload_button(self, by,value,file_path):
        # 假设点击上传按钮后会弹出文件选择对话框
        upload_button = self.wait_for_element_visible( by, value)
        upload_button.click()
        # 等待对话框打开（根据需要调整等待时间）
        time.sleep(2)
        # 模拟键盘输入文件路径（根据实际情况修改文件路径）
        pyautogui.write(file_path)
        # 按下 Enter 键确认文件选择
        pyautogui.press('enter')
    # 上传文件方法
    def upload(self, by,value,filenamePath):
        """
        input标签才能这样：send_keys上传文件
        :return:
        """
        upload = self.wait_for_element_visible(by,value)
        time.sleep(3)
        upload.send_keys(filenamePath)
        upload_button = self.driver.find_element_by_id('onBtn')
        upload_button.click()