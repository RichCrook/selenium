import unittest
from random import randrange # let's not import the entire module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('inputs.ini')

class Registration(unittest.TestCase):
    """
    This module registers a new account on the IMDB website.  
    To generate HTML documentation for this module issue the
    command and regenerate this document:

        pydoc -w registration

    """
    def setUp(self):
        """
        Attempts to register a new account.
        """
        self.driver = webdriver.Firefox()

    def test_register_a_new_account(self):
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
        self.driver.close()

    def select_dropdown_option(self, driver, select_locator, option_text):
        """
        A helper to select an item from a dropdown
        """
        dropdown = self.driver.find_element_by_id(select_locator)
        for option in dropdown.find_elements_by_tag_name("option"):
            if option.text == "United States":
                option.click()
                break

    def random_email_address(self):
        """
        Returns a randomly generated email address.
        """
        return "robbie" + str(randrange(100,999)) + "@mailinator.com"

    def ConfigSectionMap(section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

if __name__ == "__main__":
    unittest.main()