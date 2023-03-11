from selenium import webdriver
from selenium.webdriver.common.by import By

class movie_scrap(webdriver.Chrome):
    def __init__(self,teardown = False):
        super(movie_scrap,self).__init__()
        self.teardown = teardown
        self.implicitly_wait(10)
        #self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
            self.quit()
    def home_page(self):
        self.get("https://hdhub4u.show/")

    def movies(self):
        movie_list_element = self.find_elements(By.CLASS_NAME,"col-md-2")

        for movie in movie_list_element:
            list_movie = movie.find_element(By.CSS_SELECTOR,'p').text
            print(list_movie)

    def get_genre(self):
        genre_link = self.get('https://hdhub4u.show/the-last-of-us-season-1-english-webrip-all-episodes/')
        genre_list = self.find_elements(By.CLASS_NAME,'page-meta')
        #print(len(genre_list))

        for tag in genre_list:
            list_genre = self.find_elements(By.CSS_SELECTOR, 'em')
            result=tag.text
            print(result)

with movie_scrap() as bot:
    #bot.home_page()
    #bot.movies()
    #bot.get_genre()