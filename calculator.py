import unittest

import time
from selenium import webdriver

class My_calculator(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        url = 'http://www.calculator.pro/'
        driver.get(url)
        self.driver = driver
    def tearDown(self):
        self.driver.quit()

    def test_itself(self):
        driver = self.driver
        expected_result = 10
        four_button_xpath = '//button[text()="4"]'
        six_button_xpath = '//button[text()="6"]'
        plus_button_xpath = "//*[@id='plus']"
        equal_button_xpath = "//*[@id='result']"
        actual_line = "//input[@name='expression']"
        driver.find_element_by_xpath(four_button_xpath).click()
        driver.find_element_by_xpath(plus_button_xpath).click()
        driver.find_element_by_xpath(six_button_xpath).click()
        driver.find_element_by_xpath(equal_button_xpath).click()
        time.sleep(10)
        actual_result = driver.find_element_by_xpath(actual_line).text
        print actual_result, type(actual_result)




