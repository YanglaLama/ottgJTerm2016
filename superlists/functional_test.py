from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has a cool new online to-do app
        # She checks out the homepage
        # starts Firefox

        #got to this website via Firefox
        self.browser.get('http://localhost:8000')

        # She notices page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # same as line 8
        # if ! 'To-Dp in browser.title:
        #    throw new AssertionError

        # Edith really likes fly fishing
        # She is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # Sometimes she may forget and leave an empty

        # When she hits enter, the page updates and now the page lists
        # "1. Buy peacock feathers" as an item
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # She can still add more to do items
        # She writes "Use peacock feathers to make fly"
        # (Edith is very methodolical)

        # The homepage uodates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.
        # The site generates a unique URL for her- there is some explanation

        # She visits the URL- her to-do list is still there

        # She is done!
        self.fail('Finish the app!')

if __name__ == '__main__':
    unittest.main()
