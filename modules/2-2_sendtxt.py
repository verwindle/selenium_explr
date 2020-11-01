from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # fill personal data
    first_name, last_name, email = 'Name', 'Surname', '@mail.com'
    _first_name, _last_name, _email = map(lambda el:\
            browser.find_element(By.NAME, el), ('firstname', 'lastname', 'email'))
    _first_name.send_keys(first_name)
    _last_name.send_keys(last_name) 
    _email.send_keys(email)

    # find and load txt
    txt_file = os.path.abspath(os.path.dirname(__file__))
    txt_file = os.path.join(txt_file, 'txt.txt')
    loader = browser.find_element(By.ID, 'file')
    loader.send_keys(txt_file)

    #submit btn
    subm = browser.find_element_by_xpath('//button[@type="submit"]')
    subm.click()
finally:
    time.sleep(10)
    browser.quit()
