from selenium.webdriver.common.by import By

class MainPageLocators:

    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"

    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SAMOKAT = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
