from .base import FunctionalTest
from basic import processors
import time

# Create your tests here.


CONFIG_DATA = processors.main_config('/')['CONFIG_DATA']


class NewVisitorTest(FunctionalTest):

    def test_load_the_website(self):
        # Edith has heard about a cool new online soccer manager app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention the website name
        self.assertIn(CONFIG_DATA['WEB_NAME'], self.browser.title)
        #self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

    def test_failed_login(self):
        self.browser.get('http://localhost:8000')
        # She introduces her login credentials wrongly
        inputbox_username = self.browser.find_element_by_id('id_username')
        inputbox_password = self.browser.find_element_by_id('id_password')
        inputbox_username.send_keys("cosme")
        inputbox_password.send_keys("12345")
        inputbox_password.send_keys(self.keys.ENTER)
        time.sleep(2)
        self.assertIn("Please enter a correct", self.browser.page_source)

