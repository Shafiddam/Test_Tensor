from .pages.base_page import BasePage
import pytest


def test_yandex_pictures(browser):
    """
    Картинки на яндексе.
    1)	Зайти на yandex.ru
    2)	Ссылка «Картинки» присутствует на странице
    3)	Кликаем на ссылку
    4)	Проверить, что перешли на url https://yandex.ru/images/
    5)	Открыть 1 категорию, проверить что открылась, в поиске верный текст
    6) Открыть 1 картинку , проверить что открылась
    7) При нажатии кнопки вперед  картинка изменяется
    8) При нажатии кнопки назад картинка изменяется на изображение из шага 6.
    Необходимо проверить, что это то же изображение.
    """
    link = 'http://yandex.ru'
    page = BasePage(browser, link)
    page.open()
    # page.go_to_login_mail_page()
    # page.find_count_mail_and_write_mail()
