from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Product in basket is presented, but should not be"

    def guest_can_see_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "There is no message about empty basket"