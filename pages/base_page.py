from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def check_url_correct(self, url_part):
        WebDriverWait(self.browser, 10).until(ec.url_contains(url_part))

    def avatar_click(self):
        self.wait_until_clickable(BasePageLocators.AVATAR_BUTTON).click()

    def go_to_profile(self):
        self.avatar_click()
        self.wait_until_clickable(BasePageLocators.PROFILE_BUTTON).click()

    def check_user_authenticated(self):
        assert self.check_element_present(BasePageLocators.AVATAR_BUTTON), "Пользователь не авторизовался"

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable(locator))

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located(locator))

    def check_element_present(self, locator, timeout=10):
        try:
            return self.wait_until_visible(locator, timeout)
        except TimeoutException:
            return False
