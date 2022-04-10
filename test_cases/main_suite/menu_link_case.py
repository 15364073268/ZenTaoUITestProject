import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as EC

current = os.path.dirname(__file__)
print(current)
chrome_driver_path = os.path.join(current, '../../Webdriver/chromedriver')
print(chrome_driver_path)


class ZentaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        '''验证我的地盘菜单'''
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[1]/a/span').click()
        time.sleep(2)
        self.assertTrue(EC.title_is('我的地盘-禅道'))

    def test_product_link(self):
        '''验证产品菜单'''
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[2]/a').click()
        time.sleep(2)
        self.assertTrue(EC.title_is('产品主页-禅道'))




if __name__ == '__main__':
    unittest.main(verbosity=2)
    # suite01 = unittest.TestSuite(unittest.makeSuite(ZentaoTest))
    # now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    # file = open('result{}.html'.format(now_time),'wb')
    # html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='测试用例执行结果', description='标题党')
    # html_runner.run(suite01)
