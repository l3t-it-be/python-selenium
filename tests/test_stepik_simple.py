import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.stepik
class TestStepik:
    @pytest.mark.smoke
    def test_successful_login(self, browser):
        browser.get('https://stepik.org/')

        login_button = browser.find_element(
            By.CSS_SELECTOR, 'a[href="/catalog?auth=login"]'
        )
        login_button.click()

        login_input = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
        login_input.send_keys('stepikstudent@yandex.ru')
        password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys('stepikpassword')
        submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        time.sleep(2)

        profile_menu = browser.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Profile"]'
        )
        profile_menu.click()
        time.sleep(2)

        profile_button = browser.find_element(
            By.CSS_SELECTOR, '[data-qa="menu-item-profile"]'
        )
        profile_button.click()
        time.sleep(2)

        expected_name = 'Stepik Student'
        actual_name = browser.find_element(By.CSS_SELECTOR, 'h1').text
        assert actual_name == expected_name, f'Student name should be {expected_name}'

    @pytest.mark.stepik
    @pytest.mark.parametrize(
        'num',
        [
            '236895',
            '236896',
            '236897',
            '236898',
            '236899',
            '236903',
            '236904',
            '236905',
        ],
    )
    def test_stepik_puzzle(self, browser, num):
        link = f'https://stepik.org/lesson/{num}/step/1'
        browser.get(link)
        time.sleep(2)

        login_button = browser.find_element(
            By.CSS_SELECTOR, f'a[href="/lesson/{num}/step/1?auth=login"]'
        )
        login_button.click()
        time.sleep(2)

        input_name = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
        input_name.send_keys('stepikstudent@yandex.ru')
        input_password = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        input_password.send_keys('stepikpassword')
        submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        time.sleep(2)

        answer = math.log(int(time.time()))

        input_field = browser.find_element(By.CSS_SELECTOR, 'textarea')

        if not input_field.is_enabled():
            try_again_button = browser.find_element(By.CSS_SELECTOR, 'button.again-btn')
            WebDriverWait(browser, 10).until(
                ec.element_to_be_clickable(try_again_button)
            )
            try_again_button.click()
            time.sleep(2)

        input_field = browser.find_element(By.CSS_SELECTOR, 'textarea')
        input_field.clear()
        input_field.send_keys(answer)

        send_button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable(send_button))
        send_button.click()
        time.sleep(2)

        feedback = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
        if feedback != 'Correct!':
            print('', feedback, sep='\n')
