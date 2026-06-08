import allure
import pytest
from data import FAQ_RESPONSES
from pages.base_page import BasePage
from pages.FAQ_page import FAQpage

class TestFAQ:

    @allure.title("Проверка ответа на вопрос FAQ #{index}")
    @pytest.mark.parametrize("index, response", FAQ_RESPONSES)
    def test_faq_responses(self, driver, index, response):
        base_page = BasePage(driver)
        faq_page = FAQpage(driver)

        base_page.clik_accept_cookie()
        faq_page.scroll_to_faq()
        faq_page.click_question(index)
        response_text = faq_page.get_answer_text(index)

        assert response_text == response
