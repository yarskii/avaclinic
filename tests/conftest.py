import os

import allure
from appium import webdriver as appium
import pytest
from selene import browser
from selenium import webdriver
from utils import config_mobile
from utils.config import base_url


@pytest.fixture(scope='session')
def browser_management():
    driver_options = webdriver.ChromeOptions()

    driver_options.add_argument('--headless=new')
    driver_options.add_argument('--no-sandbox')

    # Раскомментируйте, если требуется запуск в полноэкранном режиме.
    # driver_options.add_argument('--window-size=1920,1024')

    browser.config.driver_options = driver_options
    browser.config.base_url = base_url


@pytest.fixture(scope='session')
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
