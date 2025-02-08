from pages.base_page import BasePage

class TestPage(BasePage):
    PAGE_TITLE = "Test Page"

    def __init__(self, driver):
        self.driver = driver

    def test_page_specific_function(self):
        pass
