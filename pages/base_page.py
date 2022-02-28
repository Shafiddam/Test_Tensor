import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def should_be_search_field(self):
        """ Проверка, что есть поле поиска. """
        assert self.is_element_present(*BasePageLocators.INPUT_BOX), "INPUT BOX IS NOT PRESENTED..."

    def enter_word_tensor(self):
        # вводим в поле поиска слово "Тензор":
        word = "Тензор"
        btn = self.browser.find_element(*BasePageLocators.INPUT_BOX)
        btn.send_keys(word)
        # Проверка, что есть таблица с подсказками (suggest):
        # assert self.is_element_present(
        #     *BasePageLocators.INPUT_BOX_SUGGEST_LIST), "INPUT BOX SUGGEST LIST IS NOT PRESENTED..."
        time.sleep(2)
        btn.send_keys(Keys.ENTER)  # нажимаем клавишу Enter

    def should_be_link_tensor(self):
        # проверяем, что в первых 5 результатах есть ссылка на tensor.ru:
        assert self.is_element_present(*BasePageLocators.DATA_CID_1) \
               or self.is_element_present(*BasePageLocators.DATA_CID_2) \
               or self.is_element_present(*BasePageLocators.DATA_CID_3) \
               or self.is_element_present(*BasePageLocators.DATA_CID_4) \
               or self.is_element_present(*BasePageLocators.DATA_CID_5), \
            "RESULTS OF SEARCH LINK 'https://tensor.ru' IS NOT PRESENTED..."

    def is_element_present(self, how, what):
        """
        Метод, в котором будем перехватывать исключение. В него будем передавать два аргумента:
        как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        Чтобы перехватывать исключение, нужна конструкция try/except:
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Абстрактный метод, который проверяет, ___ЧТО ЭЛЕМЕНТ НЕ ПОЯВЛЯЕТСЯ___
        на странице в течение заданного времени:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Метод, который проверяет, ___ЧТО ЭЛЕМЕНТ ИСЧЕЗАЕТ___
        Следует воспользоваться явным ожиданием вместе с функцией until_not,
        в зависимости от того, какой результат мы ожидаем:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """ Открытие браузера """
        self.browser.get(self.url)
