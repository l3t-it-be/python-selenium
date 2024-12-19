from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from scripts.setup import create_browser, calculation, get_alert_text

browser = create_browser()

try:
    browser.get('https://suninjuly.github.io/explicit_wait2.html')

    expected_price = '100'
    WebDriverWait(browser, 10).until(
        ec.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#price'), expected_price
        )
    )
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true)', input_field
    )

    formula_text = browser.find_element(
        By.CSS_SELECTOR, 'label .nowrap'
    ).text.strip()
    x_text = browser.find_element(By.CSS_SELECTOR, '#input_value').text.strip()
    result = calculation(formula_text, x_text)

    input_field.send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

    get_alert_text(browser)

finally:
    browser.quit()
