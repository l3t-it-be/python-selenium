from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from scripts.setup import create_browser, get_alert_text

browser = create_browser()

try:
    browser.get('https://suninjuly.github.io/selects1.html')

    num1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    result = num1 + num2

    select = Select(browser.find_element(By.CSS_SELECTOR, 'select'))
    select.select_by_visible_text(str(result))

    browser.find_element(By.CSS_SELECTOR, 'button').click()
    get_alert_text(browser)

finally:
    browser.quit()
