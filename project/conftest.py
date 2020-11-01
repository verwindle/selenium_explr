import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                    help="Choose browser: chrome or firefox")
    parser.addoption('--lang', action='store', default='en-gb',
                    help="Choose webpage language, default english <en-gb>")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    page_language = request.config.getoption("lang")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs',
                    {'intl.accept_languages': page_language})
        print('chosen webpage language:', page_language)
        browser = webdriver.Chrome(options=options)
        print('actual language of the page:', browser.execute_script(\
                    "return window.navigator.language"))  # doesn't make sense, why?
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", page_language)
        print('chosen webpage language:', page_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print('actual language of the page:', browser.execute_script(\
                    "return window.navigator.language"))  # doesn't make sense, why?
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

