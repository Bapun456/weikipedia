from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.country=(By.ID,"searchInput")
        self.search_button=(By.CLASS_NAME,"pure-button.pure-button-primary-progressive")

    def log(self,country):
        wait=WebDriverWait(self.driver,20)
        wait.until(ec.visibility_of_element_located(self.country)).send_keys(country)
        wait.until(ec.element_to_be_clickable(self.search_button)).click()