from __future__ import absolute_import
import unittest
import time
from appium import webdriver

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.common.exceptions import NoSuchElementException

class HotspotShield(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = 'C:\\Python projects\\Apps Mobile\\Coach_memory.apk'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_ip_change(self):
        driver = self.driver
        print "searching for button"
        WebDriverWait(driver, 10). until(ES.presence_of_element_located((By.ID, 'mmStartViewStartPlayPort')))
        button = driver.find_element(By.ID,'mmStartViewStartPlayPort')
        print "found button"
        button.click()
        print "clicked button"
        time.sleep(10)
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Problem solving']")))
        problem_button = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Problem solving']")
        problem_button.click()
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Simple Math']")))
        math_button = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Simple Math']")
        math_button.click()
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.ID, 'spYesNoMatchStartButton')))
        play_button = driver.find_element(By.ID, 'spYesNoMatchStartButton')
        play_button.click()
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.ID, 'btSolvingMoreLessLeftExpressionButton')))
        left_element = driver.find_element(By.ID,'btSolvingMoreLessLeftExpressionButton')
        left_element_text = left_element.text
        print left_element
        print left_element_text
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.ID, 'btSolvingMoreLessOperationExpressionButton')))
        operation_element = driver.find_element(By.ID, 'btSolvingMoreLessOperationExpressionButton')
        operation_element_text = operation_element.text
        print operation_element
        print operation_element_text
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.ID, 'btSolvingMoreLessRightExpressionButton')))
        right_element = driver.find_element(By.ID, 'btSolvingMoreLessRightExpressionButton')
        right_element_text = right_element.text
        print right_element
        print right_element_text
        statement = eval("{} {} {}".format(left_element_text, operation_element_text, right_element_text))
        # print "{} {} {}".format(left_element_text, operation_element_text, right_element_text)
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.ID, 'spYesNoNotMatchButton')))
        no_element = driver.find_element(By.ID, 'spYesNoNotMatchButton')
        WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.ID, 'spYesNoMatchButton')))
        yes_element = driver.find_element(By.ID, 'spYesNoMatchButton')
        if statement == True:
            yes_element.click()
        else:
            no_element.click()

