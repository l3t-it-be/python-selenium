import pytest
from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/'


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
class TestMainPage:

    @staticmethod
    def open_main_page(browser, language):
        browser.get(link + f'{language}')

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser, language):
        self.open_main_page(browser, language)
        login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
        assert login_link.is_enabled(), f'{login_link} should be enabled'

    @pytest.mark.skip
    @pytest.mark.regression
    def test_guest_should_see_basket_link(self, browser, language):
        self.open_main_page(browser, language)
        basket_link = browser.find_element(By.CSS_SELECTOR, '.basket-mini a.btn')
        assert basket_link.is_enabled(), f'{basket_link} should be enabled'

    @pytest.mark.xfail(reason='fixing this bug right now')
    def test_guest_should_see_search_button(self, browser, language):
        self.open_main_page(browser, language)
        search_button = browser.find_element(By.CSS_SELECTOR, 'input.btn')
        assert search_button.is_enabled(), f'{search_button} should be enabled'
