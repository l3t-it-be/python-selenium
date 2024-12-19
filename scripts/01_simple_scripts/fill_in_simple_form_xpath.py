from selenium.webdriver.common.by import By

from scripts.setup import create_browser, create_random_generator, get_alert_text

browser = create_browser()
random = create_random_generator()

try:
    browser.get('https://suninjuly.github.io/find_xpath_form')

    first_name_input = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    first_name_input.send_keys(random.first_name())
    last_name_input = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    last_name_input.send_keys(random.last_name())
    city_input = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    city_input.send_keys(random.city())
    country_input = browser.find_element(By.XPATH, '//input[@id="country"]')
    country_input.send_keys(random.country())

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
    get_alert_text(browser)

finally:
    browser.quit()
