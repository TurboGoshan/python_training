import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: fr or es")
# 'pytest --language en test_items.py -s' - example of command in PyTest for select language

@pytest.fixture(scope="function")
def browser(request):
    print('\nstart testing...')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nfinish testing...')
    browser.quit()
