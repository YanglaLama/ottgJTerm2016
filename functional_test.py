from selenium import webdriver

#start Firefox
browser = webdriver.Firefox()
#got to this website via Firefox
browser.get('http://localhost:8000')

assert 'Django' in browser.title
