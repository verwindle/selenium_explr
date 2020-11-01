from .base_page import BasePage
from .locators import PromoPageLocators
from selenium.webdriver.common.by import By


class PromoPage(BasePage):

    def should_be_product(self):
        assert self.is_element_present(*PromoPageLocators.PRODUCT_AREA),\
                "Product is not presented"

    def add_product_to_basket(self):
        assert self.is_element_present(*PromoPageLocators.ADD_TO_BASKET_BTN),\
                "Have not found button to add to basket"
        basket_btn = self.browser.find_element(*PromoPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()
        promo_code = self.solve_quiz_and_get_code()
        assert len(promo_code), 'Have not got valid promo code'

        return promo_code        
        

    
