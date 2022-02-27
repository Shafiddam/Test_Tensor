import time

from .pages.base_page import BasePage
import pytest


def test_yandex_search_tensor(browser):
    """
    Поиск в яндексе
    1)	Зайти на yandex.ru
    2)	Проверить наличия поля поиска
    3)	Ввести в поиск Тензор
    4)	Проверить, что появилась таблица с подсказками (suggest)
    5)	При нажатии Enter появляется таблица результатов поиска
    6)	 В первых 5 результатах есть ссылка на tensor.ru
    """
    link = 'http://yandex.ru'
    page = BasePage(browser, link)
    page.open()
    page.should_be_search_field()
    page.enter_word_tensor()
    time.sleep(3)
    # page.should_be_link_tensor()

