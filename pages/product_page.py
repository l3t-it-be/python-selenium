from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def add_product_to_basket(self):
        self.url_should_contain_text(ProductPageLocators.text_in_url)
        self.click_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_have_success_message()
        self.product_name_should_match_the_one_added()
        self.product_price_should_match_original_product_price()

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.add_to_basket_button).click()

    def should_have_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.success_message
        ), 'Success message is not presented'

    def should_not_have_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.success_message
        ), 'Success message is presented, but should not be'

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.success_message
        ), 'Success message is presented, but should disappear'

    def product_name_should_match_the_one_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name).text
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.product_name_in_message
        ).text
        assert (
            product_name == product_name_in_message
        ), 'Product name does not match the one added to cart'

    def product_price_should_match_original_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.product_price
        ).text
        product_price_in_message = self.browser.find_element(
            *ProductPageLocators.product_price_in_message
        ).text
        assert (
            product_price == product_price_in_message
        ), 'Product price does not match original product price'
