from selenium import webdriver

# Edith has a cool new online to-do app
# She checks out the homepage
# starts Firefox
browser = webdriver.Firefox()
#got to this website via Firefox
browser.get('http://localhost:8000')

# She notices page title and header mention to-do lists
assert 'To-Do' in browser.title

# same as line 8
# if ! 'To-Dp in browser.title:
#    throw new AssertionError

# Edith really likes fly fishing
# She is invited to enter a to-do item

# She types "Buy peacock feathers" into a text box

# When she hits enter, the page updates and now the page lists
# "1. Buy peacock feathers" as an item

# She can still add more to do items
# She writes "Use peacock feathers to make fly"
# (Edith is very methodolical)

# The homepage uodates again, and now shows both items on her list

# Edith wonders whether the site will remember her list.
# The site generates a unique URL for her- there is some explanation

# She visits the URL- her to-do list is still there

# She is done!

browser.quit()
