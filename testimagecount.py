import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 


class TestImageCount(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Firefox()

    def test_search(self):

        self.driver.get('http://www.imdb.com/title/tt1430612')
        image_count = self.driver.find_elements_by_xpath("//img")
        print len(image_count)

    def tearDown(self):
        self.driver.close() 

if __name__ == "__main__":  # Final lines are some boiler plate code to run the test suite
    unittest.main()  # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    # magic methods