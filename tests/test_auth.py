from pages.auth_page import AuthPage
from config import USERS, LINKS

import pytest


class TestAuth:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = AuthPage(browser, LINKS["main_page"])
        self.page.open_page()

    @pytest.mark.parametrize("login,password", [(USERS["PM"]["login"], USERS["PM"]["password"]),
                                                (USERS["QA"]["login"], USERS["QA"]["password"])])
    def test_login_success(self, login, password):
        self.page.login(login, password)
        self.page.check_user_authenticated()
