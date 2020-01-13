
# 这是首页,有立即注册、企业登录功能
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_PO.page.base_page import BasePage
from test_PO.page.login import Login
from test_PO.page.register import Register

class Index(BasePage):
    # 优化3. 把__init__用例放到base_page.py文件中,此处引入base_page.py文件中的类 BasePage

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(3)
    #     self.driver.get("https://work.weixin.qq.com/")
    # def __init__(self, driver):
    #     self.driver = driver
    # 优化1.进行初始化，传入一个driver

    # def __init__(self, driver=None):
    #     if driver==None:
    #         self.driver = webdriver.Chrome()
    #         self.driver.implicitly_wait(3)
    #         self.driver.get("https://work.weixin.qq.com/")
    #     else:
    #         self.driver = driver
    # 优化2.if条件是为了引入外部drivre时，不影响使用
    _base_url = "https://work.weixin.qq.com/"
    # 加base前加_为了隐藏

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 点击立即注册，进入注册页面
        return Register(self._driver)
        # 返回Register页面

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业登录").click()
        return Login(self._driver)

