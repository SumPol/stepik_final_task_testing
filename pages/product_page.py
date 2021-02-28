from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    def should_add_to_basket(self):
        assert self.is_element_present(*ProductLocators.ADD_TO_BASKET), "There is no add to basket button"
        basket_button = self.browser.find_element(*ProductLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_message_about_add_to_basket(self):
        assert self.is_element_present(*ProductLocators.MESSAGE_ABOUT_ADD_TO_BASKET_PRODUCT), "There is no message about add to basket poduct"

    def should_be_right_message_about_add_to_basket(self):
     	assert self.browser.find_element(*ProductLocators.NAME_PRODUCT_IN_BASKET).text == self.browser.find_element(*ProductLocators.NAME_PRODUCT).text, "Name does not match"

    def should_be_message_about_price(self):
        assert self.is_element_present(*ProductLocators.MESSAGE_ABOUT_PRICE_ADDED_PRODUCT), "There is no message about price added to basket poduct"

    def should_be_right_message_about_price(self):
    	assert self.browser.find_element(*ProductLocators.PRICE_PRODUCT_IN_BASKET).text == self.browser.find_element(*ProductLocators.PRICE_PRODUCT).text, "Price does not match"