import pytest
from selenium.webdriver.common.by import By

url1 = 'https://suninjuly.github.io/registration1.html'
url2 = 'https://suninjuly.github.io/registration2.html'
welcome_text_expected = 'Congratulations! You have successfully registered!'


class TestRegistration:
    @staticmethod
    def fill_registration_form(browser, url, random):
        browser.get(url)

        first_name_input = browser.find_element(
            By.CSS_SELECTOR, '.first_block input.first'
        )
        first_name_input.send_keys(random.first_name())
        last_name_input = browser.find_element(
            By.CSS_SELECTOR, '.first_block input.second'
        )
        last_name_input.send_keys(random.last_name())
        email_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        email_input.send_keys(random.email())
        browser.find_element(By.CSS_SELECTOR, 'button').click()

        welcome_text_actual = browser.find_element(By.TAG_NAME, 'h1').text
        assert (
            welcome_text_actual == welcome_text_expected
        ), f'If registration is successful, there should be a welcome text {welcome_text_expected}'

    @pytest.mark.smoke
    def test_registration(self, browser, random):
        self.fill_registration_form(browser, url1, random)

    @pytest.mark.xfail
    @pytest.mark.regression
    def test_registration_failed(self, browser, random):
        self.fill_registration_form(browser, url2, random)
