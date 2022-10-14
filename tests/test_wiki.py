import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from util.attachment import add_video


@allure.tag('mobile')
@allure.title('Test search browserstack')
def test_wiki_search(app_android):
    with step('Type search browserstack'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('BrowserStack')
    with step('Verify content found'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')) \
            .should(have.size_greater_than(0))
    add_video(browser)


@allure.tag('mobile')
@allure.title('Test search qa')
def test_wiki_sqa(app_android):
    with step('Type search qa'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Software quality assurance")
    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))
    add_video(browser)


@allure.tag('mobile')
@allure.title('Test search browserstack')
def test_wiki_appium(app_android):
    with step('Type search appium'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")
    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))
    add_video(browser)


@allure.tag('mobile')
@allure.title('Test search browserstack')
def test_wiki_api_search(app_android):
    with step('Type search api'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Api")
    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))
    add_video(browser)


@allure.tag('mobile')
@allure.title('Test search browserstack')
def test_wiki_selenium_search(app_android):
    with step('Type search android'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Selenium")
    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))
    add_video(browser)
