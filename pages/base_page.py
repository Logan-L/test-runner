from typing import Tuple, Union
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement

class BasePage():
    TIMEOUT = 60

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_visible(self, locator: Tuple[str, str]):
        return WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, webelement_or_locator: Union[WebElement, Tuple[str, str]]):
        return WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.element_to_be_clickable(webelement_or_locator))
    