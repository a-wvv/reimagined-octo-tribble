from base_page import BasePage
from locators import SecondPageLocators
from random import sample


class SecondPage(BasePage):
    def fill_movie_list(self):
        def get_list_movies(movies):
            mov_rand = sample(movies, 3)
            s = f'''{movies[0]} {movies[1]} {movies[2]} {movies[3]} {movies[4]}
{mov_rand[0]} {mov_rand[1]} {mov_rand[2]}'''.format(*movies)
            return s
        area = self.browser.find_by_css(SecondPageLocators.MOVIE_FIELD)
        movies = ['A', 'B', 'C', 'D', 'E']
        area.fill(get_list_movies(movies))

    def chose_collor(self):
        self.browser.find_by_css(SecondPageLocators.COLOR_LIST).click()
        self.browser.find_by_css(
            '.exportSelectPopup > div:nth-child(4)').click()

    def go_to_first_page(self):
        self.browser.find_by_css(SecondPageLocators.PREV_BUTTON).click()

    def go_to_last_page(self):
        self.browser.find_by_css(SecondPageLocators.NEXT_BUTTON).click()
