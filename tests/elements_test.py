import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from pages.elements_page import TextBoxPage, CheckBoxPage

class TestElements:
    class TestTextBox:
        def test_text_box(self,driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'the full name is not the matched'
            assert email == output_email, "the email is not the matched"
            assert current_address == output_current_address, "the current address is not the matched"
            assert permanent_address == output_permanent_address, "the permanent address is not the matched"

class TestCheсkBox:
    def test_check_box(self,driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_check_box =check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_check_box == output_result, 'checkboxes have not been checked'
