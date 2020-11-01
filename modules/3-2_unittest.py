from selenium import webdriver
import time
import unittest


def register_me(link):
    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name, last_name, email = 'Name', 'Surname', '@mail.com'
        _first_name, _last_name, _email = map(lambda el:\
                browser.find_element_by_css_selector(el), ('input[placeholder="Input your first name"]',\
                'input[placeholder="Input your last name"]',\
                'input[placeholder="Input your email"]'))
        _first_name.send_keys(first_name)
        _last_name.send_keys(last_name) 
        _email.send_keys(email)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

    return welcome_text


class TestAuth(unittest.TestCase):
    
    text = 'Congratulations! You have successfully registered!'

    def test_registration_one(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(self.text, register_me(link))

    def test_registration_two(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(self.text, register_me(link))


if __name__ == '__main__':
    unittest.main()
