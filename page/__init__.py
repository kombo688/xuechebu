from selenium.webdriver.common.by import By

# 主页面
mine = By.XPATH, '//*[contains(@text,"我的")]'
# 我的页面
login_btn = By.XPATH, '//*[contains(@text,"登录")]'
# 账号
user_name = By.XPATH,'//*[contains(@text,"账号")]'
# 密码
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'
# 登录按钮
login_bu = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'
# 确定
com_btn = By.XPATH,'//*[contains(@text,"确定")]'