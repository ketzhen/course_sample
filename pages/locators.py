from selenium.webdriver.common.by import By


class BasePageLocators:
    AVATAR_BUTTON = (By.CLASS_NAME, 'text-avatar')
    PROFILE_BUTTON = (By.NAME, 'person')


class AuthPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '[placeholder="Username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[placeholder="Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')