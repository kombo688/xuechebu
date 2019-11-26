"""
工厂方法类
"""
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def mine_page(self):
        return MinePage(self.driver)

    @property
    def home_page(self):
        return HomePage(self.driver)

    @property
    def login_page(self):
        return LoginPage(self.driver)
