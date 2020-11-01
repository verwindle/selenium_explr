from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time


def calc(x):
  return str(log(abs(12*sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # get x value and input the chest
    chest = browser.find_element(By.CSS_SELECTOR, 'img[id="treasure"]')
    x = chest.get_attribute('valuex')
    # x = browser.find_element(By.ID, "input_value")
    ans = browser.find_element(By.ID, "answer")
    # x = x.text
    ans.send_keys(calc(x))

    # checkbox
    box = browser.find_element(By.ID, 'robotCheckbox')
    box.click()
    # radiobtn
    radbtn = browser.find_element(By.ID, 'robotsRule')
    radbtn.click()

    #submit btn
    subm = browser.find_element_by_xpath('//button[@type="submit"]')
    subm.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()