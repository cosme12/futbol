from .base import FunctionalTest
from basic import processors

# Create your tests here.


CONFIG_DATA = processors.main_config('/')['CONFIG_DATA']


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        self.assertIn(CONFIG_DATA['WEB_NAME'], self.browser.title)
        self.fail('Finish the test!')
        # She is invited to enter a to-do item straight away
