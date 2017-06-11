import unittest
import time
from selenium import webdriver
# from selenium import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class My_login_togmail(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Firefox()
        url = 'https://www.google.com/gmail/about/'
        driver.get(url)
        driver.implicitly_wait(20)
        self.driver = driver




    def tearDown(self):
        self.driver.quit()

    def test_itself(self):
        delay = 20
        # pass
        driver = self.driver
        sign_in_element = driver.find_element_by_xpath('//a[@class="gmail-nav__nav-link gmail-nav__nav-link__sign-in"]')
        sign_in_element.click()
        time.sleep(3)
        # WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_element_by_id('Email')))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Email")))
        login = 'anastasiia.demenkova@gmail.com'
        password = 'miupiu26122014'
        driver.find_element_by_id('Email').send_keys(login)
        time.sleep(3)
        driver.find_element_by_id('next').click()
        time.sleep(3)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Passwd")))
        driver.find_element_by_id('Passwd').send_keys(password)
        time.sleep(3)
        driver.find_element_by_id('signIn').click()
        time.sleep(3)
