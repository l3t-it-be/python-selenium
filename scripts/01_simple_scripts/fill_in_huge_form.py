from selenium.webdriver.common.by import By

from scripts.setup import create_browser, get_alert_text

browser = create_browser()

try:

    browser.get('https://suninjuly.github.io/huge_form.html')

    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys('Hello, World!')

    browser.find_element(By.CSS_SELECTOR, 'button').click()
    get_alert_text(browser)

finally:
    browser.quit()
