from selenium.webdriver.common.by import By

class MainPageLocators():


    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():


    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	MESSAGE_ABOUT_ADD_TO_BASKET_PRODUCT = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
	MESSAGE_ABOUT_PRICE_ADDED_PRODUCT = (By.CSS_SELECTOR, ".alert-info")
	NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
	PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-info>.alertinner>p:nth-Child(1)>strong")
	NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main>.price_color")