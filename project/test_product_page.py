from .pages.promo_page import PromoPage


PROMO_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
# BUG_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# BUG_LINK_VARIANTS = 10
# PROMO_LINK_LIST = [f'{BUG_LINK}?promo=offer{k}' for k in range(BUG_LINK_VARIANTS)]

def test_guest_should_access_promo_page(browser):
    page = PromoPage(browser, PROMO_LINK)
    page.open()

def test_guest_can_see_product(browser):
    page = PromoPage(browser, PROMO_LINK)
    page.open()
    page.should_be_product()

def test_guest_can_add_product_to_basket(browser):
    page = PromoPage(browser, PROMO_LINK)
    page.open()
    promo_code = page.add_product_to_basket()
    print(f"Your code: {promo_code}")

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PromoPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PromoPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
