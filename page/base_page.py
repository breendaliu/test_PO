
# 存放公共服务
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver=None):
        if driver is None:
            # index页面会使用这个
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            # self.driver.get("https://work.weixin.qq.com/")
            # 改成_base_url是可以允许每个类定义自己的打开页面
            self._driver.get(self._base_url)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

    def close(self):
        sleep(5)
        self._driver.quit()