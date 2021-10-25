import pytest
from selenium import webdriver
import time
def pytest_addoption(parser):

    parser.addoption("--language", action='store', default=None,            help="Choose browser: chrome or firefox!!!!!!!!!")


@pytest.fixture(autouse=True)
def browser(request):
    browser =request.config.getoption("--language")
    print('@@@',browser,'!!#####!!')
    return browser
