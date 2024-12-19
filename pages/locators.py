from selenium.webdriver.common.by import By


class BasePageLocators:
    login_link = (By.CSS_SELECTOR, '#login_link')
    basket_link = (By.CSS_SELECTOR, '.btn-group a')
    user_icon = (By.CSS_SELECTOR, '.icon-user')
    user_email = (By.XPATH, '//th[.="Email address"]/following-sibling::td')


class LoginPageLocators:
    text_in_url = 'login'
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')
    email_field = (By.CSS_SELECTOR, '#id_registration-email')
    password_field = (By.CSS_SELECTOR, '#id_registration-password1')
    confirm_password_field = (By.CSS_SELECTOR, '#id_registration-password2')
    submit_registration_button = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    text_in_url = '?promo='
    add_to_basket_button = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    success_message = (By.CSS_SELECTOR, '.alertinner')
    product_name = (By.CSS_SELECTOR, 'h1')
    product_name_in_message = (By.CSS_SELECTOR, '.alertinner strong')
    product_price = (By.CSS_SELECTOR, 'p.price_color')
    product_price_in_message = (By.CSS_SELECTOR, '.alertinner p strong')


class BasketPageLocators:
    basket_items = (By.CSS_SELECTOR, '.basket-items')
    empty_basket_message = (By.CSS_SELECTOR, '#content_inner p')
