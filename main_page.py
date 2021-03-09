from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re




class MainPage(BasePage):
    def show_all_cities(self):
        button_show_all_cities = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa=home_landing_show_button]"))
        )
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", button_show_all_cities)
        help_window_open = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "jvlabelWrap"))
        )
        help_window_open.click()
        button_show_all_cities.click()

        all_cities_1 = list(self.browser.find_element_by_css_selector("div.cities_2UD0M").text.split("\n"))
        all_cities_2 = list(self.browser.find_element_by_css_selector("div.cities_2UD0M:nth-child(4)").text.split("\n"))
        all_cities = all_cities_1 + all_cities_2

        numbers_cities = self.browser.find_element_by_css_selector("div.cities_12Awe>span").text
        new_numbers_cities = re.findall((r"\d+"), numbers_cities)
        assert len(all_cities) == int(
            new_numbers_cities[0]), "Кол-во городов отличается от указанного в шаге 2 кол-ва городов"
        assert len(all_cities) == len(set(all_cities)), "Названия городов повторяются"

    def select_any_city(self):
        button_select_any_city = self.browser.find_element_by_css_selector("a.cities_2OU_U:nth-child(1)")
        button_select_any_city.click()

    def select_any_store(self):
        button_select_any_store_1 = self.browser.find_element_by_css_selector("button.stores_12LB3:nth-child(1)")
        button_select_any_store_1.click()
        button_show_stores_by_locate = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa=address-modal-submit]"))
        )
        button_show_stores_by_locate.click()
        button_select_any_store_2 = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.stores_2Gvn5:nth-child(1)"))
        )
        get_name_store_by_click = self.browser.find_element_by_css_selector("div.stores_2Gvn5:nth-child(1) img.Image_1Sb56")
        get_name_store_by_click = get_name_store_by_click.get_attribute("alt")
        button_select_any_store_2.click()
        # button_fast_deliver_close = WebDriverWait(self.browser, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.Button_2mDPg"))
        # )
        # button_fast_deliver_close.click()
        #
        # button_feedback_close = WebDriverWait(self.browser, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div.Button_g0zP1>svg.Button_2mDPg"))
        # )
        # button_feedback_close.click()

        get_name_store_from_search = self.browser.find_element_by_css_selector("input.form_3jkWP")
        get_name_store_from_search = get_name_store_from_search.get_attribute("placeholder")
        get_name_store_from_search = get_name_store_from_search.replace("Найти в магазине ", "")
        assert get_name_store_by_click == get_name_store_from_search, "Название магазина в поисковой строке, отличается от названия магазина, выбранного на шаге 6"
