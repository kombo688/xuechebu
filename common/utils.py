"""
公共方法
"""
from appium import webdriver


def init_driver():
    capabilities = {
        "platformName": "Android",  # 模拟器名称
        "platformVersion": "5.1",  # 模拟器型号
        "deviceName": "Android 5",  # 模拟器平台
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测引用的包名
        "appActivity": ".MainActivity",  # 待测应用的启动名
        "resetKeyboard": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    driver.implicitly_wait(30)
    return driver
