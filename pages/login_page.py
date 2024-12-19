from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def should_be_on_login_page(self):
        self.url_should_contain_text(LoginPageLocators.text_in_url)
        self.should_have_login_form()
        self.should_have_register_form()

    def should_have_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.login_form
        ), 'Login form is not presented'

    def should_have_register_form(self):
        self.is_element_present(
            *LoginPageLocators.register_form
        ), 'Register form is not presented'

    def register_new_user(self, email, password):
        self.browser.execute_script('window.scrollBy(0, 100);')

        email_field = self.browser.find_element(*LoginPageLocators.email_field)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.password_field)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(
            *LoginPageLocators.confirm_password_field
        )
        confirm_password_field.send_keys(password)
        submit_registration_button = self.browser.find_element(
            *LoginPageLocators.submit_registration_button
        )
        submit_registration_button.click()

        return BasePage(self.browser)
