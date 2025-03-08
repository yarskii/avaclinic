from selene import browser, be, by

from tests.conftest import base_url
from utils.config import logger


class Navigation:
    @staticmethod
    def open_home_page():
        logger.info(f'Открываем {base_url}')
        browser.open('/')

    def select_header_section(self, section):
        logger.info(f'Переходим в "{section}"')
        browser.element('.headerMenuRow_menu').should(be.visible).element(by.text(section)).click()

    def select_footer_section(self, section):
        logger.info(f'Переходим в "{section}"')
        browser.element('.footerMenu').should(be.visible).element(by.text(section)).click()
