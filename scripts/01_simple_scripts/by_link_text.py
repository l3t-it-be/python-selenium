import math

from selenium.webdriver.common.by import By

from scripts.setup import create_browser, create_random_generator, get_alert_text

browser = create_browser()
random = create_random_generator()

try:
    browser.get('https://suninjuly.github.io/find_link_text')

    text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    browser.find_element(By.LINK_TEXT, text).click()

    first_name_input = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    first_name_input.send_keys(random.first_name())
    last_name_input = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    last_name_input.send_keys(random.last_name())
    city_input = browser.find_element(By.CSS_SELECTOR, 'input.city')
    city_input.send_keys(random.city())
    country_input = browser.find_element(By.CSS_SELECTOR, '#country')
    country_input.send_keys(random.country())

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    get_alert_text(browser)

finally:
    browser.quit()
