import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step("Проскроллить страницу к FAQ")
    def scroll_to_faq(self, timeout=5):
        element = self.wait_until_present(MainPageLocators.FAQ_SECTION, timeout)
        self.scroll_into_view(element)
        return element

    @allure.step("Кликнуть по вопросу")
    def click_question(self, index, timeout=5):
        question_locator = MainPageLocators.faq_question(index)
        question = self.wait_until_clickable(question_locator, timeout)
        question.click()

    @allure.step("Взять текст ответа")
    def get_answer_text(self, index, timeout=5):
        answer_locator = MainPageLocators.faq_answer(index)
        answer = self.wait_until_visible(answer_locator, timeout)
        return answer.text

    @allure.step("Принять куки")
    def clik_accept_cookie(self, timeout=5):
        cookie_button = self.wait_until_clickable(MainPageLocators.COOKIE_BUTTON, timeout)
        cookie_button.click()

    @allure.step("Кликнуть на лого самоката")
    def click_samokat_logo(self, timeout=5):
        samokat_logo = self.wait_until_clickable(MainPageLocators.LOGO_SAMOKAT)
        samokat_logo.click()

    @allure.step("Кликнуть на лого яндекса")
    def click_yandex_logo(self, timeout=5):
        yandex_logo = self.wait_until_clickable(MainPageLocators.LOGO_YANDEX)
        yandex_logo.click()
