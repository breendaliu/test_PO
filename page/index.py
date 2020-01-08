
# 这是首页,有立即注册、企业登录功能
from selenium.webdriver.common.by import By
from test_PO.page.register import Register


class Index:

    def __init__(self, driver):
        self.driver = driver
        # 进行初始化，传入一个driver

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 点击立即注册，进入注册页面
        return Register(self.driver)
        # 返回Register页面

