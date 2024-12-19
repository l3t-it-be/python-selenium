import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox',
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language: ",
        choices=(
            'ar',
            'ca',
            'cs',
            'da',
            'de',
            'en',
            'el',
            'es',
            'fi',
            'fr',
            'it',
            'ko',
            'nl',
            'pl',
            'pt',
            'pt-br',
            'ro',
            'ru',
            'sk',
            'uk',
            'zh-hans',
        ),
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        print('\nStart Chrome browser for test')
        service = Service(executable_path=ChromeDriverManager().install())
        browser_options = webdriver.ChromeOptions()
        browser_options.page_load_strategy = 'eager'
        browser_options.add_argument('--headless')
        browser_options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        browser = webdriver.Chrome(service=service, options=browser_options)

    elif browser_name == 'firefox':
        print('\nStart Firefox browser for test')
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        browser_options = webdriver.FirefoxOptions()
        browser_options.page_load_strategy = 'eager'
        browser_options.add_argument('--headless')
        browser_options.set_preference('intl.accept_languages', str(language))
        browser = webdriver.Firefox(service=service, options=browser_options)

    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser
    print('\nQuit browser after test')
    browser.quit()


@pytest.fixture()
def random():
    random = Faker()
    return random
