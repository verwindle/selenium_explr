from .pages.promo_page import PromoPage
import pytest


PROMO_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
BUG_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
BUG_LINK_VARIANTS = 10
PROMO_LINK_LIST = [f'{BUG_LINK}?promo=offer{k}' for k in range(BUG_LINK_VARIANTS)]

# @pytest.mark.parametrize('link', PROMO_LINK_LIST)
# def test_guest_should_access_promo_page(browser, link):
#     page = PromoPage(browser, link)
#     page.open()

# @pytest.mark.parametrize('link', PROMO_LINK_LIST)
# def test_guest_can_see_product(browser, link):
#     page = PromoPage(browser, link)
#     page.open()
#     page.should_be_product()

@pytest.mark.parametrize('link', PROMO_LINK_LIST)
def test_guest_can_add_product_to_basket(browser, link):
    page = PromoPage(browser, link)
    print(link)
    page.open()
    promo_code = page.add_product_to_basket()
    print(f"Your code: {promo_code}")
