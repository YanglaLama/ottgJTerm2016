from unittest import skip
from .base import ToDoFunctionalTest

class ItemValidationTest(ToDoFunctionalTest):
    @skip ("Haven't implemented this!")
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the homepage and accidently tries to submit
        # an empty list uitem
        # She hits "Enter" on the empty input box

        # The home page refreshes, and there is an error message

        # She tries again with some text for the item
        # which now works

        # Edith perversely tries to enter a second blank items

        # She recieves a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail("Finish the test!")
