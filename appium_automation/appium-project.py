# PYcharm interpreter has some bug running automation. Next line is a workaround.
# not important for Appium automation.
from __future__ import absolute_import

#for running automation
import unittest
from appium import webdriver

#  this section is for locating elements.
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class HotspotShield(unittest.TestCase):

    def setUp(self):
        "Setup for the test"
        # about desired capabilities: https://appium.io/slate/en/master/?ruby#appium-server-capabilities
        desired_caps = {}
        desired_caps['platformName'] = 'Android'

        # 'uiautomator2' automation name using for platform version 7.0,7.1.1
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = 'C:\\Python projects\\appium_automation\\Hotspot Shield Free VPN Proxy_v5.0.4_apkpure.com.apk'

        # noReset means that appium won't reinstall the application .apk file above every time you run it.
        desired_caps['noReset'] = 'true'

        # Start webdriver on the server that you launched.
        # Server should "listen" on the same location: "http://localhost:4723".
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_IP_change(self):
        "Test the Single Player mode launches correctly"
        # TODO Get public ip berfore starting Hotspot app.
        # TODO get public ip after starting hotspot app
        # TODO choose randomly the country from the list
        driver = self.driver

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'button_connect')))  

        button = driver.find_element(By.ID,'button_connect')
        button.click()

        # in case AD is displayed:
        try:
            print "looking for an AD. using Expected Conditions EC"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Interstitial close button')))
            driver.find_element_by_accessibility_id('Interstitial close button').click()
        except NoSuchElementException:
            print "Ad was not displayed at this time, continue"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((MobileBy.ID, 'select_location')))
        driver.find_element(MobileBy.ID, 'select_location').click()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HotspotShield)
    unittest.TextTestRunner(verbosity=2).run(suite)