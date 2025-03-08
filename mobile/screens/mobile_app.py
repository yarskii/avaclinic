from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class AvaPetekApp:
    RECORD_TAB = (AppiumBy.ACCESSIBILITY_ID, 'Запись')
    CONFIRM_BUTTON = (AppiumBy.ID, 'ru.avapeter.selfservice:id/confirmButton')
    ADULT_PATIENT = (AppiumBy.ACCESSIBILITY_ID, 'Взрослый')
    TYPE = (AppiumBy.ACCESSIBILITY_ID, 'Диагностика')
    SEARCH_FIELD = (AppiumBy.ID, 'ru.avapeter.selfservice:id/searchEditText')
    SEARCH_BUTTON = (AppiumBy.ID, 'ru.avapeter.selfservice:id/searchInputFindButton')
    FIRST_RESULT = (
        AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="ru.avapeter.selfservice:id/searchResultsRecyclerView"]/android.view.ViewGroup[1]'
    )
    SERVICE = (AppiumBy.ACCESSIBILITY_ID, 'УЗИ мочевого пузыря с определением остаточной мочи')

    def select_main_tab(self):
        browser.element(self.RECORD_TAB).should(be.visible).click()

    def skip_screen(self):
        browser.element(self.CONFIRM_BUTTON).should(be.visible).click()

    def select_adult(self):
        browser.element(self.ADULT_PATIENT).should(be.visible).click()

    def select_diagnostic(self):
        browser.element(self.TYPE).should(be.visible).click()

    def search_direction(self, direction):
        browser.element(self.SEARCH_FIELD).should(be.visible).type(direction)
        browser.element(self.SEARCH_BUTTON).should(be.visible).click()

    def select_first_variant(self):
        first_article = browser.element(self.FIRST_RESULT)
        first_article.click()

    def select_service(self):
        browser.element(self.SERVICE).should(be.visible).click()


mobile = AvaPetekApp()
