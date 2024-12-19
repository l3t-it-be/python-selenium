from selenium.webdriver.common.by import By

from scripts.setup import create_browser

browser = create_browser()

try:
    browser.get('https://suninjuly.github.io/wait1.html')
    browser.find_element(By.CSS_SELECTOR, '#verify').click()

    message = browser.find_element(By.CSS_SELECTOR, '#verify_message').text
    assert 'successful' in message

finally:
    browser.quit()
