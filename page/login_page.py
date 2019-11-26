"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    user_name = page.user_name
    pwd = page.pwd
    login_bu = page.login_bu
    com_btn = page.com_btn

    def input_name(self, text):
        """输入用户名"""
        self.input_func(self.user_name, text)

    def input_pwd(self, text):
        """输入密码"""
        self.input_func(self.pwd, text)

    def click_button(self):
        """点击登录"""
        self.click_func(self.login_bu)

    def click_sure(self):
        """点击弹窗确定"""
        self.click_func(self.com_btn)
