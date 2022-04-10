import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import HTMLTestRunner
from common import login
from common import set_driver
from selenium.webdriver.support import expected_conditions as EC

current = os.path.dirname(__file__)
print(current)
chrome_driver_path = os.path.join(current, '../../Webdriver/chromedriver')
print(chrome_driver_path)


class ZentaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_loginSuccess01(self):
        '''测试test01账号登录'''
        login.login(self.driver, 'test01', 'newdream123')
        # self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        # self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        result_name = self.driver.find_element(By.XPATH, '//*[@id="userNav"]/li/a/span[1]').text
        self.assertEqual(result_name, 'test01', 'test_login01用例执行失败')

    def test_loginSuccess02(self):
        '''测试test02账号登录'''
        login.login(self.driver, 'test02', 'newdream123')
        # self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test02')
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        # self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        result_name = self.driver.find_element(By.XPATH, '//*[@id="userNav"]/li/a/span[1]').text
        self.assertEqual(result_name, 'test01', 'test_login02用例执行失败')
        # self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="userNav"]/li/a/span[1]'), 'test01'), 'test_login02用例执行失败')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite01 = unittest.TestSuite(unittest.makeSuite(ZentaoTest))
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = open('result{}.html'.format(now_time),'wb')
    html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='测试用例执行结果', description='标题党')
    html_runner.run(suite01)

