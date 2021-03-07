from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "There is no add to basket button"
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_message_about_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET_PRODUCT), "There is no message about add to basket poduct"

    def should_be_right_message_about_add_to_basket(self):
     	assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text == self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text, "Product name does not match"

    def should_be_message_about_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_PRICE_ADDED_PRODUCT), "There is no message about price added to basket poduct"

    def should_be_right_message_about_price(self):
    	assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text == self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text, "Product price does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is not disappeared" 