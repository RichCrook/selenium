import unittest
from random import randrange  # let's not import the entire module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
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

    def test_register_a_new_account_happy_path(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_011
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

    def test_register_a_new_account_invalid_year_of_birth(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_004
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys("BAD YEAR")
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#year + .reg_error")  # sibling combinator
        assert element.text == 'Please use YYYY format'


    def test_register_a_new_account_invalid_gender(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_003
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        # self.driver.find_element_by_id("gender_m").click() leave this unselected
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#gender_m ~ .reg_error")  # general sibling combinator
        assert element.text == 'Required'


    def test_register_a_new_account_invalid_zip(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_005
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys("BAD ZIP")
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#postal + .reg_error")
        assert element.text == 'Please enter a 5 digit zip code'


    def test_register_a_new_account_blank_email(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_006
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        # self.driver.find_element_by_id("email").send_keys(self.random_email_address()) leave this unentered
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#email + .reg_error")
        assert element.text == 'Required'


    def test_register_a_new_account_bad_email(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_007
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_bad_email_address())
        # self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password')) leave this unentered
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#password1 + .reg_error")
        assert element.text == 'Required'


    def test_register_a_new_account_blank_first_name(self):
        """
        Registration Tab In test_cases.ods - Test Case #1
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        # self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#first_name + .reg_error")
        assert element.text == 'Required'


    def test_register_a_new_account_blank_last_name(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_002
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        # self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#last_name + .reg_error")
        assert element.text == 'Required'


    def test_register_a_new_account_blank_email(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_008
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_email_address())
        # self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password')) leave this unentered
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#password1 + .reg_error")
        assert element.text == 'Required'


    def test_register_a_new_account_blank_second_password(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_009
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_bad_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'password'))
        # self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element = self.driver.find_element_by_css_selector("#password2 + .reg_error")
        assert element.text == 'Required'


    def test_register_a_new_account_invalid_first_password(self):
        """
        Registration Tab In test_cases.ods - Test Case #reg_010
        """
        self.driver.get(parser.get('SectionOne', 'url_in_test'))
        self.driver.find_element_by_id("first_name").send_keys(parser.get('SectionOne', 'first_name'))
        self.driver.find_element_by_id("last_name").send_keys(parser.get('SectionOne', 'last_name'))
        self.driver.find_element_by_id("gender_m").click()
        self.driver.find_element_by_id("year").send_keys(parser.get('SectionOne', 'year'))
        self.select_dropdown_option(self.driver, "country", parser.get('SectionOne', 'country'))
        self.driver.find_element_by_id("postal").send_keys(parser.get('SectionOne', 'zip'))
        self.driver.find_element_by_id("email").send_keys(self.random_bad_email_address())
        self.driver.find_element_by_id("password1").send_keys(parser.get('SectionOne', 'bad_password'))
        self.driver.find_element_by_id("password2").send_keys(parser.get('SectionOne', 'password'))
        self.driver.find_element_by_css_selector(".reg_right .btn2").click()
        element_one = self.driver.find_element_by_css_selector("#password1 + .reg_error")
        assert element_one.text == 'Password must be at least 8 characters'
        element_two = self.driver.find_element_by_css_selector("#password2 + .reg_error")
        assert element_two.text == 'Passwords must match'


    def tearDown(self):
        self.driver.close() #The quit will exit entire browser, where as close will close a tab, but if it is just one tab, by default most browser will exit entirely


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
        return "robbie" + str(randrange(100, 999)) + "@mailinator.com"


    def random_bad_email_address(self):
        """
        Returns a randomly generated bad email address.
        """
        return "robbie" + str(randrange(100, 999)) + "mailinator.com"


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


if __name__ == "__main__": #Final lines are some boiler plate code to run the test suite
    unittest.main() #http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # magic methods