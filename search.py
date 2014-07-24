import unittest
from selenium import webdriver
 # Tests with the page object pattern.
  class SearchTest(unittest.TestCase):
      def setUp(self):
          self.browser = webdriver.Firefox()
  
      def test_someone_can_search(self):
          homepage = Homepage(self.browser)
          homepage.navigate()
          search_form = homepage.getSearchForm()
          search_form.setName("Hercules")

          search_form.submit()
 
  
          #elem = self.browser.find_element_by_css_selector('#logged_in_header')
          #assert elem is not None
  
      def tearDown(self):
          self.browser.close()