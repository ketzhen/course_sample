import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    browser_location = request.config.option.browser_location

    if browser_location == "remote":
        capabilities = {
            "browserName": "chrome",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)
    else:
        browser = webdriver.Chrome()

    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--browser_location")
