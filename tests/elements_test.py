import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage

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

class TestRadioButton:
    def test_radio_button(self,driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', 'radio button "yes" is not selected'
        assert output_impressive == 'Impressive', 'radio button "impressive" is not selected'
        assert output_no == 'No', 'radio button "no" is not selected'
