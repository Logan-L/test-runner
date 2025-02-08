from pages.base_page import BasePage

class HomePage(BasePage):
    PAGE_TITLE = "Home Page"

    def __init__(self, driver):
        self.driver = driver

    def home_page_specific_function(self):
        pass
