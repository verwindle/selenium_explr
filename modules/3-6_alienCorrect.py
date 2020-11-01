import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log
from time import time


links = '''
    https://stepik.org/lesson/236895/step/1
    https://stepik.org/lesson/236896/step/1
    https://stepik.org/lesson/236897/step/1
    https://stepik.org/lesson/236898/step/1
    https://stepik.org/lesson/236899/step/1
    https://stepik.org/lesson/236903/step/1
    https://stepik.org/lesson/236904/step/1
    https://stepik.org/lesson/236905/step/1
    '''

labels = [f'step {n}' for n in range(len(links.split('\n')))]

@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links.split('\n'), ids=labels)
def test_correct_feedback(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
    # get stepik input window
    input = browser.find_element(By.CLASS_NAME, 'textarea')
    input.send_keys(str(log(int(time()))))
    # click submit
    btn = browser.find_element(By.CLASS_NAME, 'submit-submission')
    btn.click()
    # check hint on success submition
    # WebDriverWait(browser, 10).until(\
        # EC.element_located_to_be_selected(By.CLASS_NAME, 'attempt-message_correct'))
    hint = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    assert hint.text == 'Correct!', f'Hint text is "{hint.text}", not "Correct!"'