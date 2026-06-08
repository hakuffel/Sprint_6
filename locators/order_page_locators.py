from selenium.webdriver.common.by import By

class OrderFormLocators:

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")

    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")

    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")

    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")

    METRO_SELECT_LIST = (By.CLASS_NAME, "select-search__select")

    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    CREATE_ORDER_BUTTON = (By.XPATH,
                    "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    RENTAL_PERIOD = [(By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='сутки']"), (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='двое суток']")]

    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")

    COLORS = [(By.XPATH, "//input[@id='black']"), (By.XPATH, "//input[@id='grey']")]

    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    BUTTON_YES = (By.XPATH,
                  "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Да']")

    BUTTON_NO = (By.XPATH,
                 "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and contains(@class, 'Button_Inverted') and text()='Нет']")

    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")

    MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    ORDER_NUMBER_TEXT = (By.XPATH, "//div[contains(@class, 'Order_Text')]")

    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    BODY = (By.TAG_NAME, "body")

    @staticmethod
    def metro_station_click(metro):
        return By.XPATH, f"//div[contains(@class, 'select-search__select')]//button[text()='{metro}']"
