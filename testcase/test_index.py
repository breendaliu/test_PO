# 这是一个操作过程
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_PO.page.index import Index
from test_PO.page.login import Login


class TestIndex:
    def setup(self):
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        # self.driver.get("https://work.weixin.qq.com/")
        # 公共服务代码复制到index.py中，使用index引入,test_register中的index=Index()可省略
        self.index = Index()

    def test_register(self):
        # self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 立即注册步骤放到index.py文件下
        # index = Index(self.driver)
        # self.driver传递过来
        self.index.goto_register().register("测试用")
        # Index是一个PO方法，引入进来；模拟的是上方进入首页，立即注册步骤

        # self.driver.find_element(By.ID, "corp_name").send_keys("测试用")
        # self.driver.find_element(By.ID, "submit_btn").click()
        # 注册页面编辑信息放到register.py下

    def test_login(self):
        register_page = self.index.goto_login().goto_registry().register("测试再次使用")
        print(register_page.get_error_message())
        print("|".join(register_page.get_error_message()))
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
    # 引入index.py中的close,关闭页面
