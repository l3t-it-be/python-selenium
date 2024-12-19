import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestVerification:
    @pytest.mark.smoke
    def test_successful_verification(self, browser):
        browser.get('https://suninjuly.github.io/wait2.html')

        verify_button = browser.find_element(By.CSS_SELECTOR, '#verify')
        WebDriverWait(browser, 5).until(
            ec.element_to_be_clickable(verify_button)
        ).click()

        message = browser.find_element(By.CSS_SELECTOR, '#verify_message').text
        word = 'successful'
        assert word in message, f'Should be {word} in {message}'
