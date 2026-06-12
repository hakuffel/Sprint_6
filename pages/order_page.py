import allure
from locators.order_page_locators import OrderFormLocators
from pages.base_page import BasePage
import random

class OrderPage(BasePage):

    @allure.step("Нажать на кнопку заказа")
    def click_order_button(self, timeout=5):
        order_button = self.wait_until_clickable(OrderFormLocators.ORDER_BUTTON, timeout)
        order_button.click()

    @allure.step("Ввести имя заказчика")
    def set_name(self, timeout=5):
        names = ['Катя', 'Ян']
        name_field = self.wait_until_clickable(OrderFormLocators.INPUT_NAME, timeout)
        name_field.click()
        name_field.send_keys(random.choice(names))

    @allure.step("Ввести фамилию заказчика")
    def set_surname(self):
        surnames = ['Аш', 'Шварц']
        self.driver.find_element(*OrderFormLocators.INPUT_SURNAME).send_keys(random.choice(surnames))

    @allure.step("Ввести адрес")
    def set_address(self):
        self.driver.find_element(*OrderFormLocators.INPUT_ADDRESS).send_keys('Улица Пушкина, дом Колотушкина')

    @allure.step("Выбрать станцию")
    def set_station(self, timeout=5):
        stations = ['Комсомольская', 'Лубянка']
        station_name = random.choice(stations)
        metro_field = self.wait_until_clickable(OrderFormLocators.INPUT_METRO, timeout)
        metro_field.click()
        metro_field.send_keys(station_name)
        metro_select = self.wait_until_clickable(OrderFormLocators.METRO_SELECT_LIST, timeout)
        metro_select.click()

    @allure.step("Ввести адрес")
    def set_number(self, timeout=5):
        number = '+7' + str(random.randint(1000000000, 9999999999))
        phone_field = self.wait_until_clickable(OrderFormLocators.INPUT_PHONE, timeout)
        phone_field.click()
        phone_field.send_keys(number)

    @allure.step("Кликнуть по кнопке 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*OrderFormLocators.BUTTON_NEXT).click()

    @allure.step("Ввести дату заказа")
    def set_data(self, timeout=5):
        dates = ['17.08.2026', '29.09.2026']
        data = self.wait_until_clickable(OrderFormLocators.INPUT_DATE, timeout)
        data.click()
        data.send_keys(random.choice(dates))
        self.driver.find_element(*OrderFormLocators.BODY).click()

    @allure.step("Выбрать период аренды")
    def choose_rental(self, timeout=5):
        rental_dropdown = self.wait_until_clickable(OrderFormLocators.RENTAL_PERIOD_DROPDOWN, timeout)
        rental_dropdown.click()

        rental_option = random.choice(OrderFormLocators.RENTAL_PERIOD)
        rental_element = self.wait_until_clickable(rental_option, timeout)
        rental_element.click()

    @allure.step("Выбрать цвет самоката")
    def choose_color(self):
        color_option = random.choice(OrderFormLocators.COLORS)
        self.driver.find_element(*color_option).click()

    @allure.step("Добавить комментарий к заказу")
    def add_comment(self):
        comments = ['', 'коммент']
        comment_field = self.driver.find_element(*OrderFormLocators.COMMENT)
        comment_field.click()
        comment_field.send_keys(random.choice(comments))

    @allure.step("Нажать на кнопку 'Заказать'")
    def create_order_click_button(self):
        self.driver.find_element(*OrderFormLocators.CREATE_ORDER_BUTTON).click()

    @allure.step("Нажать на кнопку подтверждения заказа")
    def click_yes_for_order_button(self, timeout=5):
        button_yes = self.wait_until_clickable(OrderFormLocators.BUTTON_YES, timeout)
        button_yes.click()

    @allure.step("Проверить наличие модального окна об успешном создании заказа")
    def check_order_complete(self, timeout=5):
        success_modal = self.wait_until_visible(OrderFormLocators.SUCCESS_MODAL, timeout)
        header = success_modal.find_element(*OrderFormLocators.MODAL_HEADER)
        return 'Заказ оформлен' in header.text
