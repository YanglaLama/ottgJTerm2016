from .base import ToDoFunctionalTest
from selenium import webdriver

class NewVisitorTest(ToDoFunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get(self.live_server_url)

        # She notices page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Edith really likes fly fishing
        # She is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        self.enter_a_new_item('Buy peacock feathers')

        # Sometimes she may forget and leave the text box empty!

        # When she hits enter, she is taken to a new URL,
        # and now the page lists "1. Buy peacock feathers" as
        # a to-do list table
        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('Buy peacock feathers')

        # She can still add more to do items
        # She writes "Use peacock feathers to make fly"
        # (Edith is very methodolical)
        self.enter_a_new_item('Use peacock feathers to make a fly')

        # The homepage uodates again, and now shows both items on her list
        self.check_for_row_in_list_table('Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make a fly')

        # Now a new user, Pala, comes along to the site

        # We use a new browser session to make sure that no information
        # of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Pala vists the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Pala starts a new list by entering a new item.
        # He is less interesting that Eidth
        self.enter_a_new_item('Buy milk')

        # Pala gets his own unique URL
        pala_list_url = self.browser.current_url
        self.assertRegexpMatches(pala_list_url, '/lists/.+')
        self.assertNotEqual(pala_list_url, edith_list_url)

        # Again there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # She visits the URL- her to-do list is still there


        # She is done!
