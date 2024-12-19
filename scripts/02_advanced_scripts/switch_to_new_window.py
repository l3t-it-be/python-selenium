from selenium.webdriver.common.by import By

from scripts.setup import create_browser, calculation, get_alert_text

browser = create_browser()

try:
    browser.get('https://suninjuly.github.io/redirect_accept.html')

    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    formula_text = browser.find_element(By.CSS_SELECTOR, 'label .nowrap').text.strip()
    x_text = browser.find_element(By.CSS_SELECTOR, '#input_value').text.strip()
    result = calculation(formula_text, x_text)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    get_alert_text(browser)

finally:
    browser.quit()
