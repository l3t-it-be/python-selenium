import math

from selenium.common import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_basket(self):
        from pages.basket_page import BasketPage

        basket_link = self.browser.find_element(*BasePageLocators.basket_link)
        basket_link.click()
        return BasketPage(self.browser)

    def go_to_login_page(self):
        from pages.login_page import LoginPage

        self.browser.find_element(*BasePageLocators.login_link).click()
        return LoginPage(self.browser)

    def is_disappeared(self, locator, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                ec.presence_of_element_located((locator, selector))
            )
        except TimeoutException:
            return False

        return True

    def is_element_present(self, locator, selector):
        try:
            self.browser.find_element(locator, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((locator, selector))
            )
        except TimeoutException:
            return True

        return False

    def open(self, url):
        self.browser.get(url)

    def should_be_authorized_user(self, email):
        self.browser.find_element(*BasePageLocators.user_icon).click()
        user_email = self.browser.find_element(*BasePageLocators.user_email)
        assert (
            user_email.text == email
        ), 'User email is not presented, probably unauthorised user'

    def should_have_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.login_link
        ), 'Login link is not presented'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')

    def url_should_contain_text(self, text: str):
        assert text in self.browser.current_url, f'URL should contain {text}'
