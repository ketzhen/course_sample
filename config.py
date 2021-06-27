from selenium import webdriver

USERS = {"QA": {"login": "QA_tester_1", "password": "Tester2019!"},
         "PM": {"login": "Project_1", "password": "Projectmanager1"}}
LINKS = {"main_page": "https://testit.geekbrains.ru/"}
BROWSER_REMOTE_CAPABILITIES = {
       "browserName": "chrome",
       "version": "90.0",
       "enableVNC": True,
   }
VALID_BROWSERS = {
    "local": webdriver.Chrome,
    "remote": webdriver.Remote}
