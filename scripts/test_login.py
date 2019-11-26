"""
执行测试用例
"""
import pytest

from common.utils import init_driver
from page.page import PageFactory
from tools.read_yaml import build_login_data


class TestLogin(object):
    def setup(self):
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,pwd',build_login_data())
    def test_login(self,name,pwd):
        self.page_factory.home_page.click_mine()
        self.page_factory.mine_page.click_home()
        self.page_factory.login_page.input_name(name)
        self.page_factory.login_page.input_pwd(pwd)
        self.page_factory.login_page.click_button()
        self.page_factory.login_page.click_sure()