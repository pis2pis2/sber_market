from conftest import method_decorator
from main_page import MainPage
import allure
from allure_commons.types import AttachmentType

link = "https://sbermarket.ru"


@method_decorator
@allure.feature("show_all_cities")
@allure.story("Пользователь может видеть все города, при нажатии на кнопку 'Показать все'")
@allure.severity("critical")
def test_guest_can_see_all_cities(browser):
    page = MainPage(browser, link)
    page.open()
    page.show_all_cities()


@allure.feature('select_any_store')
@allure.story("Пользователь может видеть выбранный магазин в поисковой строке'")
@allure.severity("critical")
def test_guest_can_see_selected_store_in_search(browser):
    page = MainPage(browser, link)
    page.open()
    page.select_any_city()
    page.select_any_store()

# pytest --alluredir results
# allure serve results
