import allure
from core.config import Config
from playwright.sync_api import Page

class NotesPage:
    def __init__(self, page: Page) -> None:
        self.__page =   page
        self.__add_button = page.locator('//input[@type="add"]')
        
    @allure.step("Go to Notes Page")
    def open_notes_page(self) -> None:
        self.__page.goto(Config.get_app_url())
        
    @allure.step("Click on the Add Button")
    def click_on_add_button(self) -> None:
        self.__add_button.click