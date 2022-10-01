
import allure_commons
import pytest
from selene.support.shared import browser
from selene import support
from appium import webdriver
import config


@pytest.fixture(scope='function', autouse=True)
def create_driver():
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    return browser
