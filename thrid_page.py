from locators import ThridPageLocators
from base_page import BasePage

class ThridPage(BasePage):
    def final_question(self):
        self.browser.find_by_css(ThridPageLocators.RADIOBOX).click()

    def submit(self):
        self.browser.find_by_css(ThridPageLocators.SUBMIT).click()
