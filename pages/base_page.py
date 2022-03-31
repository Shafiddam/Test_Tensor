import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators

current_url = None


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        # self.current_url = browser.current_url
        self.url = url

    def should_be_search_field(self):
        """ Проверка, что есть поле поиска. """
        assert self.is_element_present(*BasePageLocators.INPUT_BOX), "INPUT BOX IS NOT PRESENTED..."

    def enter_word_tensor(self):
        """ вводим в поле поиска слово "Тензор": """
        word = "Тензор"
        btn = self.browser.find_element(*BasePageLocators.INPUT_BOX)
        btn.send_keys(word)
        time.sleep(2)
        btn.send_keys(Keys.ENTER)  # нажимаем клавишу Enter

    def should_be_link_tensor(self):
        """ проверяем, что в первых 5 результатах есть ссылка на tensor.ru: """
        assert self.is_element_present(*BasePageLocators.DATA_CID_1) \
               or self.is_element_present(*BasePageLocators.DATA_CID_2) \
               or self.is_element_present(*BasePageLocators.DATA_CID_3) \
               or self.is_element_present(*BasePageLocators.DATA_CID_4) \
               or self.is_element_present(*BasePageLocators.DATA_CID_5), \
            "RESULTS OF SEARCH LINK 'https://tensor.ru' IS NOT PRESENTED..."

    def should_be_link_images_presented(self):
        """ Проверяем, что ссылка «Картинки» присутствует на странице. Кликаем на нее: """
        assert self.is_element_present(*BasePageLocators.LINK_SEARCH_IMAGES), "LINK SEARCH IMAGES IS NOT FOUND..."
        btn = self.browser.find_element(*BasePageLocators.LINK_SEARCH_IMAGES).click()

    def should_be_current_link_is_yandex_images(self, browser):
        """ Проверить, что перешли на url https://yandex.ru/images/ """
        browser.switch_to.window(browser.window_handles[1])
        assert 'https://yandex.ru/images/' in browser.current_url, "CURRENT_LINK IS NOT YANDEX_IMAGES..."

    def open_first_category(self):
        """ Открыть 1 категорию, проверить что открылась, в поиске верный текст. """
        # сохраним название 1 категории:
        text_category_0 = self.browser.find_element(*BasePageLocators.TEXT_CATEGORY_0).text
        print('\n \ntext_category_0 = ', text_category_0)
        btn = self.browser.find_element(*BasePageLocators.LINK_CATEGORY_0).click()
        time.sleep(2)
        text_search_0 = self.browser.find_element(*BasePageLocators.TEXT_SEARCH_0).text
        print('text_search_0 = ', text_search_0)
        # assert text_category_0 in text_search_0, "CURRENT_TEXT_SEARCH IS NOT CORRECT..."
        time.sleep(2)

    def open_first_image(self, browser):
        """ Открыть 1 картинку, проверить что открылась. """
        btn = self.browser.find_element(*BasePageLocators.LINK_IMAGE_0).click()
        time.sleep(2)
        # проверяем тем, что присутствует кнопка клика на следующую картинку:
        assert self.is_element_present(*BasePageLocators.CIRCLEBUTTON_TYPE_NEXT), "IMAGE IS NOT LOAD..."
        # используем глобальную переменную, чтобы позже передать ее значение в другой метод:
        global current_url
        # сохраним текущий урл:
        current_url = browser.current_url
        print("текущий урл первой картинки - ", current_url)
        time.sleep(2)

    def open_next_image(self):
        """ При нажатии кнопки вперед картинка изменяется """
        btn = self.browser.find_element(*BasePageLocators.CIRCLEBUTTON_TYPE_NEXT).click()
        time.sleep(2)

    def open_prev_image(self):
        """ При нажатии кнопки назад картинка изменяется на предыдущее изображение. """
        btn = self.browser.find_element(*BasePageLocators.CIRCLEBUTTON_TYPE_PREV).click()
        time.sleep(2)

    def should_be_first_images(self, browser):
        """ Необходимо проверить, что это то же изображение """
        print("ТЕКУЩИЙ УРЛ после кликов вперед-назад = ", browser.current_url)
        time.sleep(2)
        # проверяем, что текущий урл тот же, что и сохраненный через глобал.переменную пару шагов назад:
        assert current_url == browser.current_url, "IT'S NOT THE SAME IMAGE..."
        time.sleep(3)

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
