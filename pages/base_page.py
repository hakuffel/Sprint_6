import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import HeaderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принять куки")
    def clik_accept_cookie(self, timeout=5):
        cookie_button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(HeaderLocators.COOKIE_BUTTON)
        )
        cookie_button.click()

    @allure.step("Кликнуть на лого самоката")
    def click_samokat_logo(self, timeout=5):
        samokat_logo = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(HeaderLocators.LOGO_SAMOKAT)
        )
        samokat_logo.click()

    @allure.step("Кликнуть на лого яндекса")
    def click_yandex_logo(self, timeout=5):
        yandex_logo = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(HeaderLocators.LOGO_YANDEX)
        )
        yandex_logo.click()

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(2)
        )
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

        WebDriverWait(self.driver, timeout).until(
            EC.url_contains("ya.ru")
        )
