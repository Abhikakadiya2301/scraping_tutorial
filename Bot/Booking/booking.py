from selenium import webdriver
from selenium.webdriver.common.by import By
import Bot.Booking.constant as const
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking(webdriver.Chrome):
    def __init__(self,teardown = False):
        super(Booking,self).__init__()
        self.teardown = teardown
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def currency_change(self,currancy=None):
        currancy_element =  self.find_element(By.CSS_SELECTOR,'button[class="fc63351294 a822bdf511 e3c025e003 cfb238afa1 c334e6f658 e634344169"]'
        )
        currancy_element.click()
        change_currancy = self.find_element(By.CLASS_NAME,"cf67405157")

    def select_place_to_go(self,place_to_go):
        search = self.find_element(By.ID,':Ra9:')
        search.clear()
        search.send_keys(place_to_go)

        first_result = self.find_element(By.CLASS_NAME,"a80e7dc237")
        first_result.click()

    def select_date(self):
        check_in = self.find_element(By.CSS_SELECTOR,f'td["data-date="2023-04-14"]')
        date_selection = self.find_element(By.CSS_SELECTOR,'button[class="d47738b911 e246f833f7 fe211c0731"]')
        date_selection.click()