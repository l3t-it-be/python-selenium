import pytest

from pages.main_page import MainPage

link = 'https://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser)
        main_page.open(link)
        main_page.should_have_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser)
        main_page.open(link)
        login_page = main_page.go_to_login_page()
        login_page.should_be_on_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser)
    main_page.open(link)
    basket_page = main_page.go_to_basket()
    basket_page.basket_should_be_empty()
    basket_page.empty_basket_should_have_message_about_it()
