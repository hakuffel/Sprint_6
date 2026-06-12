import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage

class TestOrder:

    @allure.title("Проверка на успешное создание заказа")
    def test_success_order(self, driver):
        main_page = MainPage(driver)
        main_page.clik_accept_cookie()

        order_page = OrderPage(driver)
        order_page.click_order_button()
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_station()
        order_page.set_number()
        order_page.click_next_button()
        order_page.set_data()
        order_page.choose_rental()
        order_page.choose_color()
        order_page.add_comment()
        order_page.create_order_click_button()
        order_page.click_yes_for_order_button()

        assert order_page.check_order_complete()
