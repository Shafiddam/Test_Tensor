from selenium.webdriver.common.by import By


class BasePageLocators():
    INPUT_BOX = (By.CSS_SELECTOR, "input.input__control.input__input.mini-suggest__input")
    INPUT_BOX_SUGGEST_LIST = (By.CSS_SELECTOR, "input[aria-activedescendant^='suggest-list']")
    ID_SEARCH_RESULTS = (By.CSS_SELECTOR, "li#search-results")
    LINK_SEARCH_RESULT = (By.CSS_SELECTOR, "a[href^='https://tensor.ru']")
    DATA_CID_1 = (By.CSS_SELECTOR, 'li[data-cid="1"] a[href^="https://tensor.ru"]')
    DATA_CID_2 = (By.CSS_SELECTOR, 'li[data-cid="2"] a[href^="https://tensor.ru"]')
    DATA_CID_3 = (By.CSS_SELECTOR, 'li[data-cid="3"] a[href^="https://tensor.ru"]')
    DATA_CID_4 = (By.CSS_SELECTOR, 'li[data-cid="4"] a[href^="https://tensor.ru"]')
    DATA_CID_5 = (By.CSS_SELECTOR, 'li[data-cid="5"] a[href^="https://tensor.ru"]')


