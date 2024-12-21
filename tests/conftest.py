import pytest
from pages.notesPage import NotesPage
from playwright.sync_api import Page


@pytest.fixture
def notesPage(page: Page) -> NotesPage:
    return NotesPage(page)