from locators import FirstPageLocators
from base_page import BasePage
from datetime import timedelta, date, datetime

class FirstPage(BasePage):

    def add_5_days(self):
        time = date.today() + timedelta(days=5)
        form = self.browser.find_by_xpath(
            FirstPageLocators.MONTH_FIELD)
        form.fill(str(time.month) + '-' + str(time.day) + '-' + str(time.year))

    def chose_this(self):
        buttons = self.browser.find_by_css(FirstPageLocators.CHECKBOX_VALUE)
        buttons_length = len(buttons)
        for i in range(0, buttons_length):
            self.browser.find_by_css(
                FirstPageLocators.CHECKBOX_VALUE)[i].click()

    def fill_month(self):
        area = self.browser.find_by_css(FirstPageLocators.MOUNTH_NAME_FIELD)
        area.fill(date.today().strftime('%B'))

    def go_to_second_page(self):
        buttons = self.browser.find_by_css(FirstPageLocators.NEXT_BUTTON)
        buttons.click()

    def reverse_text_in_3th_question(self):
        area = self.browser.find_by_css(FirstPageLocators.MOUNTH_NAME_FIELD)
        area_value = area.value
        area.fill(area_value[::-1])
