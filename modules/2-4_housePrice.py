from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time


def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # get current price on condition
    price = browser.find_element(By.ID, 'price')
    WebDriverWait(browser, 12).until(\
        EC.visibility_of(price)\
        and\
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    
    # on expectation is True
    book_btn = browser.find_element(By.ID, 'book')
    book_btn.click()
    
    # calc again
    x = browser.find_element(By.ID, "input_value").text
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(calc(x))
    
    # submit btn
    subm = browser.find_element_by_xpath('//button[@type="submit"]')
    subm.click()
    
finally:
    time.sleep(10)
    browser.quit()
