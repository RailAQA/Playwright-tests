import pytest
from pages.inputs_page import InputsPage

def test_fill_input(InputsPage):
    inputs_page = InputsPage()
    inputs_page.op