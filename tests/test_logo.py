import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL

class TestLogo:

    @allure.title("Проверка редиректа при нажатии на лого Яндекса")
    def test_redirect_yandex_logo(self, driver):

        main_page = MainPage(driver)
        main_page.clik_accept_cookie()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert "ya.ru" in main_page.get_current_url()

    @allure.title("Проверка загрузки главной страницы при нажатии лого самоката")
    def test_redirect_samokat_logo(self, driver):

        main_page = MainPage(driver)
        main_page.clik_accept_cookie()
        order_page = OrderPage(driver)
        order_page.click_order_button()
        main_page.click_samokat_logo()

        assert main_page.get_current_url() == BASE_URL
