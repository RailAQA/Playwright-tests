from generator.generator import generated_random_text
from locators.inputs_page import InputsPageLocators
from playwright.sync_api import expect
from pages.base_page import BasePage



class TextInputPage(BasePage):
        '''
        Класс на модуль TextInput
        '''

        def __init__(self, page):
             super().__init__(page)
             self.locator = InputsPageLocators()
             self.input_field = self.locator.INPUT_FIELD

        def fill_input_field(self, text: str = None):
            if text is None:
                self.random_text = generated_random_text()
                self.page.fill(self.input_field, self.random_text)
            else:
                self.page.fill(self.input_field, text)
            return self.random_text

        def press_enter_in_input_field(self):
            self.press_key(self.locator.INPUT_FIELD, 'Enter')
            expect(self.find(self.input_field)).to_be_visible()

        def check_input_result(self) -> bool:
            result_text = self.locator.RESULT_TEXT
            expect(self.find(result_text)).to_have_text(self.random_text)