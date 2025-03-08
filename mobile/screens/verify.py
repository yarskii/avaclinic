from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class VerifyInformationMobileApp:
    def should_any_department_button(self):
        browser.element((AppiumBy.ID, 'ru.avapeter.selfservice:id/chooseClinicsSelectedAnyButton')).should(
            be.visible).should(have.text('Любое отделение'))
