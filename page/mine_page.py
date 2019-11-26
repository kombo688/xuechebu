"""
"我的页面"
"""
from base.base_page import BasePage
import page


class MinePage(BasePage):
    login_btn = page.login_btn

    def click_home(self):
        """点击登录/注册"""
        self.click_func(self.login_btn)
