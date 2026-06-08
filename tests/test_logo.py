import allure
from pages.base_page import BasePage
from pages.order_page import OrderPage
from data import BASE_URL

class TestLogo:

    @allure.title("Проверка редиректа при нажатии на лого Яндекса")
    def test_redirect_yandex_logo(self, driver):

        base_page = BasePage(driver)
        base_page.clik_accept_cookie()
        base_page.click_yandex_logo()
        base_page.switch_to_new_window()

        assert "ya.ru" in driver.current_url

    @allure.title("Проверка загрузки главной страницы при нажатии лого самоката")
    def test_redirect_samokat_logo(self, driver):

        base_page = BasePage(driver)
        base_page.clik_accept_cookie()
        order_page = OrderPage(driver)
        order_page.click_order_button()
        base_page.click_samokat_logo()

        assert driver.current_url == BASE_URL
