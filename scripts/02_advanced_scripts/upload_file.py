from selenium.webdriver.common.by import By

from scripts.setup import (
    create_browser,
    create_random_generator,
    get_alert_text,
    get_file_path,
)

browser = create_browser()
random = create_random_generator()

try:
    browser.get('https://suninjuly.github.io/file_input.html')

    first_name_input = browser.find_element(
        By.CSS_SELECTOR, '[name="firstname"]'
    )
    first_name_input.send_keys(random.first_name())
    last_name_input = browser.find_element(
        By.CSS_SELECTOR, '[name="lastname"]'
    )
    last_name_input.send_keys(random.last_name())
    email_input = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email_input.send_keys(random.email())

    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(
        get_file_path('../../best_stepik_courses.txt')
    )
    browser.find_element(By.CSS_SELECTOR, 'button').click()

    get_alert_text(browser)

finally:
    browser.quit()
