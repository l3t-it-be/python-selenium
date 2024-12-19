import os

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sympy import sympify, symbols
from webdriver_manager.chrome import ChromeDriverManager


def create_browser():
    service = Service(executable_path=ChromeDriverManager().install())

    browser_options = webdriver.ChromeOptions()
    browser_options.page_load_strategy = 'eager'
    browser_options.add_argument('--headless')

    browser = webdriver.Chrome(service=service, options=browser_options)
    browser.implicitly_wait(5)
    return browser


def create_random_generator():
    random = Faker()
    return random


def get_alert_text(browser):
    alert_text = browser.switch_to.alert.text

    num_in_alert = ''.join(
        [symbol for symbol in alert_text if symbol.isdigit() or symbol == '.']
    )
    print(num_in_alert)
    browser.switch_to.alert.accept()


def calculation(formula_text, x_text):
    formula_start = formula_text.find('ln')
    formula_end = formula_text.find(',')
    formula_text = formula_text[formula_start:formula_end]
    formula = sympify(formula_text)

    x_int = int(x_text)
    x_symbol = symbols('x')

    return str(formula.subs(x_symbol, x_int).evalf())


def get_file_path(file_name):
    file_path = os.path.abspath(file_name)
    return file_path
