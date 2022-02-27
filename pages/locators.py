from selenium.webdriver.common.by import By


class BasePageLocators():
    INPUT_BOX = (By.CSS_SELECTOR, "input.input__control.input__input.mini-suggest__input")
    INPUT_BOX_SUGGEST_LIST = (By.CSS_SELECTOR, "input[aria-activedescendant^='suggest-list']")







