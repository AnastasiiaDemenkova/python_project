import unittest

import time
from selenium import webdriver

class My_test_calculator(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        url = 'http://calculator-1.com/'
        driver.get(url)
        self.driver = driver
    def tearDown(self):
        self.driver.quit()

    def Test_itself(self):
        driver = self.driver
        expected_result = "10"
        number_seven_xpath = '//td[text()="7"]'
        button_plus_xpath = "//td[text() = '+']"
        number_three_xpath = "//td[text()='3']"
        button_equal_xpath = "//td[text()='=']"
        actual_line = "//*[@id='display']"
        driver.find_element_by_xpath(number_seven_xpath).click()
        driver.find_element_by_xpath(button_plus_xpath).click()
        driver.find_element_by_xpath(number_three_xpath).click()
        driver.find_element_by_xpath(button_equal_xpath).click()
        time.sleep(10)
        actual_result = driver.find_element_by_xpath(actual_line).text
        assert expected_result == actual_result, "wrong number"
        print actual_result, type(actual_result)

