from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    
class PromoPageLocators():
    PRODUCT_AREA = (By.CLASS_NAME, 'product_main')
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.product_main [type=submit]')