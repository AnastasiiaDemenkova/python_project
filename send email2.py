import unittest

import time
from selenium import webdriver


class My_send_email(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        url = 'https://www.google.com/gmail/about/'
        driver.get(url)
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def Test_itself(self):
        driver = self.driver
        sign_in_xpath = '//a[@data-g-label="Sign in"]'
        email_in_xpath = '//input[@id="Email"]'
        next_in_xpath = "//input[@id='next']"
        password_in_xpath = "//input[@id='Passwd']"
        sign_in_button = "//input[@id='signIn']"
        compose_button = '//div[text()="COMPOSE"]'
        recipient_field = "//*[text()='Recipients']"
        to_field = "//textarea[@name='to']"
        subject_field = "//input[@name='subjectbox']"
        my_message = "//div[@aria-label='Message Body']"
        my_subject = 'My best code %s' % time.ctime()
        send_button = "//*[text()='Send']"
        inbox_button = "//a[contains(text(),'Inbox')]"
        check_subject = "//span/*[text()='%s']" % my_subject
        driver.find_element_by_xpath(sign_in_xpath).click()
        my_login = 'anastasiia.demenkova@gmail.com'
        driver.find_element_by_xpath(email_in_xpath).send_keys(my_login)
        driver.find_element_by_xpath(next_in_xpath).click()
        my_password = 'miupiu26122014'
        driver.find_element_by_xpath(password_in_xpath).send_keys(my_password)
        driver.find_element_by_xpath(sign_in_button).click()
        driver.find_element_by_xpath(compose_button).click()
        if not driver.find_element_by_xpath(to_field).is_displayed():
            driver.find_element_by_xpath(recipient_field).click()
        driver.find_element_by_xpath(to_field).send_keys(my_login)
        driver.find_element_by_xpath(subject_field).send_keys(my_subject)
        my_text = "Ho ho ho ha ha ha"
        driver.find_element_by_xpath(my_message).send_keys(my_text)
        driver.find_element_by_xpath(send_button).click()
        for item in range(1, 61):
            print "Looking for element. Attempt number: %s" % item
            driver.find_element_by_xpath(inbox_button).click()
            try:
                assert driver.find_element_by_xpath(check_subject).is_displayed()
                break
            except:
                if item == 60:
                    assert False, "Failing the test.No email"
                print "No email. Sleeping 2 sec"
                time.sleep(2)
        print 'Done'
