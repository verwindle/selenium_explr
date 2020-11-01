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

    def solve_quiz_and_get_code(self):
        """Toy function for the task only
            New Year promo solver"""

        import math
        from selenium.common.exceptions import NoAlertPresentException

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            
            return alert_text
        except NoAlertPresentException:
            print("No second alert presented")