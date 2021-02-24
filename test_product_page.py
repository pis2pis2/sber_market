import time
link = "https://sbermarket.ru"

def test_guest_should_see_all_cities(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = find_element_by_css_selector("button.Button_1FB7o")
    button.click()
