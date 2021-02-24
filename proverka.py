from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://sbermarket.ru")
button = find_element_by_css_selector("button.Button_1FB7o Button_2-2bD Button_1IGWb Button_11evH Button_2ZFqS cities_dPrOi")
button.click()