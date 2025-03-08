from selene import browser, by

from utils.config import logger


class Verify:
    def verify_information_on_page(self, title):
        logger.info(f'Проверяем, что страница содержит информацию "{title}"')
        browser.element(by.xpath(f"//div[@class='container']/*[starts-with(name(), 'h')]")).element(by.text(title))
