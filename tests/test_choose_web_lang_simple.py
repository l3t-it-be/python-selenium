import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_displayed(browser):
    browser.get(
        'https://selenium1py.pythonanywhere.com/catalogue/the-art-of-the-start_169/'
    )
    add_to_basket_button = browser.find_element(
        By.CSS_SELECTOR, 'button.btn-add-to-basket'
    )
    assert (
        add_to_basket_button.is_displayed()
    ), f'Page should have {add_to_basket_button}'

    time.sleep(2)

    print(
        '\nFor running in console: ',
        'pytest --language=en .\\tests\\test_choose_web_lang_simple.py',
        'or pytest --language=ru .\\tests\\test_choose_web_lang_simple.py',
        'or pytest --language=uk .\\tests\\test_choose_web_lang_simple.py',
        'or pytest --language=pt-br .\\tests\\test_choose_web_lang_simple.py',
        sep='\n',
    )
