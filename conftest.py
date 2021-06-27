import pytest
import config


@pytest.fixture(scope="function")
def browser(request):
    launch = request.config.getoption("--launch")
    capabilities = config.BROWSER_REMOTE_CAPABILITIES if launch == "remote" else None
    browser = config.VALID_BROWSERS[launch](desired_capabilities=capabilities)
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--launch", default="local")
