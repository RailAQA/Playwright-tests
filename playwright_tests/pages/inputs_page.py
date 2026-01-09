from pages.base_page import BasePage
from locators.inputs_page import InputsPageLocators
from generator.generator import generated_random_text
from playwright.sync_api import expect

class InputsPage(BasePage):
    inputs_page_locators = InputsPageLocators()
    input_field = inputs_page_locators.INPUT_FIELD
    random_text = generated_random_text()

    def fill_input_field(self):
        self.page.fill(self.input_field, self.random_text)

    def press_enter_in_input_field(self):
        self.press_key(InputsPageLocators.INPUT_FIELD, 'Enter')
        expect(self.find(self.input_field)).to_be_visible()

    def check_input_result(self):
        result_text = self.inputs_page_locators.RESULT_TEXT
        expect(self.find(result_text)).to_have_text(self.random_text)



