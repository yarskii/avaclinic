import os

import allure
from appium import webdriver as appium
import pytest
from selene import browser
from selenium import webdriver
from utils import config_mobile
from utils.config import base_url
from common import attach
from selenium.webdriver.chrome.options import Options

DEFAULT_BROWSER_VERSION = '126.0'
DEFAULT_WEB_ENVIRONMENT = 'local'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION
    )
    parser.addoption(
        '--web_env',
        default=DEFAULT_WEB_ENVIRONMENT
    )


@pytest.fixture(scope='function')
def browser_management(request):
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
    web_env = request.config.getoption('web_env') or DEFAULT_WEB_ENVIRONMENT
    driver_options = webdriver.ChromeOptions()

    if web_env == 'local':

        driver_options.page_load_strategy = 'eager'
        driver_options.add_argument('--headless=new')
        driver_options.add_argument('--no-sandbox')

        # Раскомментируйте, если требуется запуск в полноэкранном режиме.
        # driver_options.add_argument('--window-size=1920,1024')

    else:
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")

        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options,
            keep_alive=True
        )

        browser.config.driver = driver

        driver_options.page_load_strategy = 'eager'
        driver_options.add_argument('--window-size=1920,1024')

    browser.config.driver_options = driver_options
    browser.config.base_url = base_url

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def mobile_management():
    with allure.step('Инициализация сессии приложения'):
        browser.config.driver = appium.Remote(
            config_mobile.remote_url,
            options=config_mobile.to_driver_options_local()
        )

    browser.config.timeout = float(os.getenv('timeout', '30.0'))

    yield

    with allure.step('Закрытие мобильной сессии'):
        browser.quit()
