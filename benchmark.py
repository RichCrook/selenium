import unittest
from selenium import webdriver
import time
from random import randrange  # let's not import the entire module
from selenium.webdriver.common.keys import Keys
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('inputs.ini')

class Benchmark(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def test_url_fire(self):
        time.sleep(2)
        self.driver = webdriver.Firefox()
        """
        Registration Tab In test_cases.ods - Test Case #11
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#main h1")
        username_in_test = parser.get('SectionOne', 'first_name') + ' ' + parser.get('SectionOne', 'last_name')
        assert element.text == username_in_test + ', welcome to your new IMDb account!'

    def test_url_phantom(self):
        time.sleep(1)
        self.driver = webdriver.PhantomJS()
        """
        Registration Tab In test_cases.ods - Test Case #11
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#main h1")
        username_in_test = parser.get('SectionOne', 'first_name') + ' ' + parser.get('SectionOne', 'last_name')
        assert element.text == username_in_test + ', welcome to your new IMDb account!'

    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
        self.driver.close()

    def random_email_address(self):
        """
        Returns a randomly generated email address.
        """
        return "robbie" + str(randrange(100, 999)) + "@mailinator.com"

    def select_dropdown_option(self, driver, select_locator, option_text):
        """
        A helper to select an item from a dropdown
        """
        dropdown = self.driver.find_element_by_id(select_locator)
        for option in dropdown.find_elements_by_tag_name("option"):
            if option.text == "United States":
                option.click()
                break

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Benchmark)
    unittest.TextTestRunner(verbosity=0).run(suite)