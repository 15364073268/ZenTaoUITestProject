import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import HTMLTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login


class ZentaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_loginFail01(self):
        '''测试test01账号登录失败'''
        login.login(self.driver,'test0000','newdream123')
        # self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test0000')
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        # self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        # result_name = self.driver.find_element(By.XPATH, '//*[@id="userNav"]/li/a/span[1]').text
        # self.assertEqual(result_name, 'test01', 'test_login01用例执行失败')
        self.assertTrue(WebDriverWait(self.driver, 2).until(EC.alert_is_present()),'执行失败')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # suite01 = unittest.TestSuite(unittest.makeSuite(ZentaoTest))
    # now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # file = open('result{}.html'.format(now_time),'wb')
    # html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='测试用例执行结果', description='标题党')
    # html_runner.run(suite01)

