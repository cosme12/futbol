from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.keys = Keys
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()
