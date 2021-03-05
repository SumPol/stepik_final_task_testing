from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no 'login' in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form is not presented"

    def register_new_user(self, email, password, browser):
        email_value = browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_value.send_keys(email)
        password_value = browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_value.send_keys(password)
        confirm_password_value = browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_value.send_keys(password)
        button_register = browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_register.click()