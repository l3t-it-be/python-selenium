import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.add_product_to_basket()


@pytest.mark.parametrize(
    'offer_number',
    [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        pytest.param('7', marks=pytest.mark.xfail),
        '8',
        '9',
    ],
)
def test_guest_can_add_product_to_basket_parametrized(browser, offer_number):
    link = f'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.add_product_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-with-the-dragon-tattoo_194/'
    product_page = ProductPage(browser)
    product_page.open(link)
    basket_page = product_page.go_to_basket()
    basket_page.basket_should_be_empty()
    basket_page.empty_basket_should_have_message_about_it()


def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.should_not_have_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-kicked-the-hornets-nest_199/'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.should_have_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/learning-python_121/'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.should_have_login_link()
    login_page = product_page.go_to_login_page()
    login_page.should_have_login_link()
    login_page.should_be_on_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, random):
        link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser)
        login_page.open(link)
        email = random.email()
        password = random.password()
        base_page = login_page.register_new_user(email, password)
        base_page.should_be_authorized_user(email)

    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/the-clean-coder_150/'
        product_page = ProductPage(browser)
        product_page.open(link)
        product_page.should_not_have_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        product_page = ProductPage(browser)
        product_page.open(link)
        product_page.add_product_to_basket()


@pytest.mark.xfail(reason='negative test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/97-things-every-programmer-should-know_173/'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.click_add_to_basket_button()
    product_page.should_not_have_success_message()


@pytest.mark.xfail(reason='negative test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/host_68/'
    product_page = ProductPage(browser)
    product_page.open(link)
    product_page.click_add_to_basket_button()
    product_page.success_message_should_disappear()
