from selenium.webdriver.common.by import By

class HeaderLocators:

    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SAMOKAT = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
