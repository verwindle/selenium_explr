link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    print(browser.find_element_by_xpath('//html').get_attribute('lang'))  # this is the lang
    