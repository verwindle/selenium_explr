from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, By_selector, elem):
        try:
            self.browser.find_element(By_selector, elem)
        except NoSuchElementException:
            return False
        return True