from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time


def calc(x):
  return str(log(abs(12*sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    ans = browser.find_element(By.ID, "answer")
    
    # scroll page down
    browser.execute_script('window.scrollBy(0, window.innerHeight / 4);')

    # input
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