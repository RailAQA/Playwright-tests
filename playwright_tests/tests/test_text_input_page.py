import pytest
import allure
from pages.inputs_page.text_input_page import TextInputPage


@allure.epic('Тесты для страницы TextInputPage')
class TestInputsPage:
    
    @allure.suite('Смоук тесты для страницы TextInputPage')
    class TestSmokeTextInputPage:

        @allure.title('Проверка ввода любого валидного значнения в поле ввода')
        @allure.description('Введенное значение отображается в отдельном блоке.')
        def test_fill_input(self, page):
            inputs_page = TextInputPage(page)
            inputs_page.open('https://www.qa-practice.com/elements/input/simple')
            inputs_page.fill_input_field()
            inputs_page.press_enter_in_input_field()
            inputs_page.check_input_result()