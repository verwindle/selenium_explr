from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin


def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    # find first submit btn - open new window
    subm = browser.find_element_by_xpath('//button[@type="submit"]')
    subm.click()
    # switch to window
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    # you are on the next tab
    # just captcha
    x = browser.find_element(By.ID, "input_value").text
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(calc(x))

    # submit btn
    subm = browser.find_element_by_xpath('//button[@type="submit"]')
    subm.click()
finally:
    time.sleep(10)
    browser.quit()
