from __future__ import absolute_import
import unittest
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
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = 'C:\\Python projects\\appium_automation\\Hotspot Shield Free VPN Proxy_v5.0.4_apkpure.com.apk'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_ip_change(self):
        driver = self.driver
        WebDriverWait(driver, 10). until(ES.presence_of_element_located((By.ID, 'button_connect')))
        button = driver.find_element(By.ID,'button_connect')
        button.click()
