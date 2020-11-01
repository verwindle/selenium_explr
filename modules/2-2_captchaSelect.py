from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from math import log, sin
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # get x and y values
    x = browser.find_element(By.ID, 'num1')
    y = browser.find_element(By.ID, 'num2')
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(x.text) + int(y.text)))

    #submit btn
    subm = browser.find_element_by_xpath('//button[@type="submit"]')
    subm.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()