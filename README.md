# sber_market
base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой страницы. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

Файл test_main_page.py - тут мы выполняем сами тесты. Тут вызванные функции будут запускаться.

conftest.py - тут мы храним фикстуры и декораторы
