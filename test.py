# coding=utf-8
import os
import unittest,  time
from HTMLTestRunner import HTMLTestRunner
from appium import webdriver


path = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Login(unittest.TestCase):

    def setUp(self):
        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['platformVersion'] = '5.1'
        desired_cap['deviceName'] = '192.168.12.101:5555'
        desired_cap['appPackage'] = 'honc.td'
        desired_cap['appActivity'] = 'honc.td.feature.main.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_id("honc.td:id/tabAccount").click() #点击我的
        self.driver.find_element_by_id("honc.td:id/tv_user_name").click()  # 点击登录/注册
        time.sleep(1)
        self.driver.find_element_by_id('honc.td:id/loginNormal').click()  #点击账号密码登录
        time.sleep(1)
        self.driver.find_element_by_id("honc.td:id/accountEtPassword").send_keys("797979")
        time.sleep(1)
        self.driver.find_element_by_id("honc.td:id/buttonNormalLogin").click()  # 点击登陆
        time.sleep(5)
        self.driver.find_element_by_id("honc.td:id/iv_user_head").click()  # 进入个人中心
        time.sleep(1)
        self.driver.find_element_by_id("honc.td:id/button_login").click()  # 退出登录
        time.sleep(1)
        self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestSuite
    suite.addTest(Login("test_login"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "D:\\test\\report_" + now + ".html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="登录测试",
                            description="用例情况：")
    runner.run(suite)
    fp.close()