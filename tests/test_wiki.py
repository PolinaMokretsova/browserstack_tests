import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser


@allure.tag('Appium Pixel 4 API 30')
@allure.title('Search on Wikipedia')
def test_wikipedia_search():

    with step('First page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text("The Free Encyclopedia"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step('Second page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text("New ways to explore"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step('Third page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.exact_text("Reading lists with sync"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

    with step('Fourth page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")) \
            .should(have.text("Send anonymous data"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")) \
            .should(be.visible)
