from unittest import skip
from .base import ToDoFunctionalTest

class ItemValidationTest(ToDoFunctionalTest):
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the homepage and accidently tries to submit
        # an empty list uitem
        # She hits "Enter" on the empty input box
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('')

        # The home page refreshes, and there is an error message
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item
        # which now works
        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('1. Buy milk')

        # Edith perversely tries to enter a second blank items
        self.enter_a_new_item('')

        # She recieves a similar warning on the list page
        self.check_for_row_in_list_table('1. Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.enter_a_new_item('Make tea')
        self.check_for_row_in_list_table('1. Buy milk')
        self.check_for_row_in_list_table('2. Make tea')
