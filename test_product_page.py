from .pages.product_page import ProductPage
#import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_to_basket()
    page.should_be_right_message_about_add_to_basket()
    page.should_be_message_about_price()
    page.should_be_right_message_about_price()
    #time.sleep(60)
