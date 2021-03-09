import pytest
from selenium import webdriver
import logging
from functools import wraps

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def method_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        return func(*args, **kwargs)
    return wrapper
