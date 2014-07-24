import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('inputs.ini')


class Search(unittest.TestCase):
    """
     This module search the IMDB website.  
     To generate HTML documentation for this module issue the
     command and regenerate this document:
 
         pydoc -w registration
 
     """

    def setUp(self):
        """
        Search for a movie.
        """
        self.driver = webdriver.Firefox()


    def test_search(self):
        """
        Search Tab In test_cases.ods - Test Case #search_001
        """
        self.driver.get(parser.get('SectionTwo', 'url_in_test'))
        search_box = self.driver.find_element_by_id("navbar-query").send_keys('Hercules')
        self.driver.find_element_by_id("navbar-query").send_keys(Keys.RETURN);
        title_result = self.driver.find_element_by_xpath(".//*[@id='main']/div/div[2]/table/tbody/tr[1]/td[2]")
        assert title_result.text == 'Hercules (2014)'

    def tearDown(self):
        self.driver.close()  # The quit will exit entire browser, where as close will close a tab, but if it is just one tab, by default most browser will exit entirely

if __name__ == "__main__":  # Final lines are some boiler plate code to run the test suite
    unittest.main()  # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # magic methods