# 这是注册页面
from selenium.webdriver.common.by import By

from test_PO.page.base_page import BasePage


class Register(BasePage):
    # def __init__(self, driver):
    #     self.driver=driver
    # 去掉driver初始化，引入base_page.py文件中的类 BasePage
    def register(self, corpname):
        # 注册页面，需要输入公司名等参数
        self._driver.find_element(By.ID, "corp_name").send_keys(corpname)
        # 公司名corpname，是从外面传参，所以send_keys中写参数名
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def get_error_message(self):
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg"):
            result.append(element.text)
        return result
