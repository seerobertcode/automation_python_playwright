import allure

from pages.notesPage import NotesPage

@allure.testcase("Test Elements on Note App")
def test_verify_page_elements(notesPage: NotesPage):
    notesPage.open_notes_page()
    notesPage.verify_page_title()
    notesPage.click_on_edit_button()
    notesPage.verify_element(notesPage.__title_textbox)
    notesPage.verify_element(notesPage.__note_textbox)
    notesPage.verify_element(notesPage.__add_button)
    notesPage.add_text_to_title_textbox("First Note")
    notesPage.add_text_to_note_textbox("The Best Note Ever")