from playwright.sync_api import Page, expect

class Driver:
    def __init__(self, page: Page) -> None:
        self.page = page
        
# Actions
    def navigate_to(self, pageUrl:str) -> None:
        self.page.goto(Config.get_app_url())

    def click_on(self, locator:str) -> None:
        self.page.locator(locator).click()
        
    def enter_text(self, locator: str, text: str) -> None:
        self.page.locator(locator),fill(text) 
        
# Verifications
    def verify_element_is_visible(self, locator:str) -> None:
        expect(self.page.locator(locator), "Element is not visible!").to_be_visible()