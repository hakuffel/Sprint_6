from selenium.webdriver.common.by import By

class FAQPageLocators:

    FAQ_SECTION = (By.CLASS_NAME, "Home_FourPart__1uthg")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"
