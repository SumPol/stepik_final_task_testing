from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-Child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	MESSAGE_ABOUT_ADD_TO_BASKET_PRODUCT = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
	MESSAGE_ABOUT_PRICE_ADDED_PRODUCT = (By.CSS_SELECTOR, ".alert-info")
	NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
	PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-info>.alertinner>p:nth-Child(1)>strong")
	NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main>.price_color")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")

class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")