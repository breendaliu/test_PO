# 这是注册页面
from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver):
        self.driver=driver
    def register(self, corpname):
        # 注册页面，需要输入公司名等参数
        self.driver.find_element(By.ID, "corp_name").send_keys(corpname)
        # 公司名corpname，是从外面传参，所以send_keys中写参数名
        self.driver.find_element(By.ID, "submit_btn").click()