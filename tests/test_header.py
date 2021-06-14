from pages.base_page import BasePage
from pages.auth_page import AuthPage
import config

import pytest


class TestHeader:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser, config.LINKS["main_page"])
        self.page.open_page()
        self.auth_page = AuthPage(browser, browser.current_url)
        self.auth_page.login(config.USERS["QA"]["login"], config.USERS["QA"]["password"])

    def test_open_profile(self):
        self.page.go_to_profile()
        self.page.check_url_correct("user-profile")
