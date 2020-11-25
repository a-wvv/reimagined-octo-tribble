from datetime import timedelta
from first_page import FirstPage
from second_page import SecondPage
from thrid_page import ThridPage
import pytest
import time
# time = datetime.date.today()
# print(time.month)
g_url = ['https://docs.google.com/forms/d/e/1FAIpQLSeY_W-zSf2_JxR4drhbgIxdEwdbUbE4wXhxHZLgxZGiMcNl7g/viewform?']
class TestFirstPage():
    
    @pytest.mark.parametrize('link', g_url)   
    def test_fill_movie_list(self,browser, link):
        self.page = FirstPage(browser, link)
        self.page.open()
        self.page.add_5_days()
        self.page.chose_this()
        self.page.fill_month()
        self.page.go_to_second_page()
        self.page = SecondPage(browser, link)
        self.page.fill_movie_list()
        self.page.chose_collor()
        self.page.go_to_first_page()
        self.page = FirstPage(browser, link)
        self.page.reverse_text_in_3th_question()
        time.sleep(5)
        self.page.go_to_second_page()
        self.page = SecondPage(browser, link)
        self.page.go_to_last_page()
        self.page = ThridPage(browser, link)
        self.page.final_question()
        self.page.submit()
