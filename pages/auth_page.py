from pages.base_page import BasePage
from pages.locators import AuthPageLocators


class AuthPage(BasePage):
    def input_login(self, login):
        self.wait_until_clickable(AuthPageLocators.EMAIL_FIELD).send_keys(login)

    def input_password(self, password):
        self.wait_until_clickable(AuthPageLocators.PASSWORD_FIELD)\
            .send_keys(password)

    def login_button_click(self):
        self.wait_until_clickable(AuthPageLocators.LOGIN_BUTTON).click()

    def login(self, login, password):
        self.input_login(login)
        self.input_password(password)
        self.login_button_click()
