from playwright.sync_api import Page
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open page')
    def open(self, url):
        """
        :param url: открываемая ссылка
        """
        self.page.goto(url)

    @allure.step('Find element by locator')
    def find(self, locator: str):
        """
        :param locator: локатор искаемого элемента. Тип str.
        """
        return self.page.locator(locator)
    
    @allure.step('Press key in element')
    def press_key(self, locator: str, key: str):
        """
        :param locator: локатор элемента, в котором нужно нажать клавишу
        :param key: клавиша, которую нужно нажать
        """
        self.find(locator).press(key)

    @allure.step('Return text from locator of element')
    def get_text_from_locator(self, locator : str) -> str:
        """
        :param locator: локатор, с элемента которого получаем текст
        :type locator: str
        """
        return self.find(locator).inner_text()