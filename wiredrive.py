import unittest
import time
from selenium import webdriver


class Wiredrive(unittest.TestCase):


    def setUp(self):
        """
        Search for a movie.
        """
        fp = webdriver.FirefoxProfile()

        fp.add_extension(extension='firebug-2.0.xpi')
        fp.set_preference("extensions.firebug.currentVersion", "2.0") #Avoid startup screen
        fp.set_preference("extensions.firebug.console.enableSites", "true")
        fp.set_preference("extensions.firebug.net.enableSites", "true")
        fp.set_preference("extensions.firebug.script.enableSites", "true")
        fp.set_preference("extensions.firebug.allPagesActivation", "on")
        self.driver = webdriver.Firefox(firefox_profile=fp)


    def test_folder(self):
        self.driver.get('https://candidates.wiredrive.com/accounts/login')
        self.driver.find_element_by_id("id_username").send_keys('richard')
        self.driver.find_element_by_id("id_password").send_keys('gQNRKGyptC')
        
        self.driver.find_element_by_id("submit-id-login").click()

        self.driver.get('https://candidates.wiredrive.com/projects/project/3788737')
        #self.driver.find_element_by_xpath(".//*[@id='ygtvt4']").click()

    def tearDown(self):
        #self.driver.close()  # The quit will exit entire browser, where as close will close a tab, but if it is just one tab, by default most browser will exit entirely
        return "foo"

if __name__ == "__main__":  # Final lines are some boiler plate code to run the test suite
    unittest.main()  # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # magic methods