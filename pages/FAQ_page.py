import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FAQPageLocators

class FAQpage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проскроллить страницу к FAQ")
    def scroll_to_faq(self, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(FAQPageLocators.FAQ_SECTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step("Кликнуть по вопросу")
    def click_question(self, index, timeout=5):
        question_locator = FAQPageLocators.faq_question(index)
        question = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(question_locator)
        )
        question.click()

    @allure.step("Взять текст ответа")
    def get_answer_text(self, index, timeout=5):
        answer_locator = FAQPageLocators.faq_answer(index)
        answer = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return answer.text
