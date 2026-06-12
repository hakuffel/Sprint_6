import allure
import pytest
from data import FAQ_RESPONSES
from pages.main_page import MainPage

class TestFAQ:

    @allure.title("Проверка ответа на вопрос FAQ #{index}")
    @pytest.mark.parametrize("index, response", FAQ_RESPONSES)
    def test_faq_responses(self, driver, index, response):
        main_page = MainPage(driver)

        main_page.clik_accept_cookie()
        main_page.scroll_to_faq()
        main_page.click_question(index)
        response_text = main_page.get_answer_text(index)

        assert response_text == response
