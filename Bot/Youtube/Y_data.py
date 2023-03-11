from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.implicitly_wait(10)

search_element = driver.find_element(By.CSS_SELECTOR,"input")
search_element.click()
search_element.send_keys("statquest")
search_element.send_keys(Keys.ENTER)

enter_channel = driver.find_element(By.ID,'main-link').click()

video_tab = driver.find_elements(By.XPATH,'//*[@id="tabsContent"]/tp-yt-paper-tab[2]')
for link in video_tab:
    link.click()

videos = driver.find_elements(By.ID,"contents")

for video in videos:
    title = driver.find_element(By.ID,"video-title")
    #views = driver.find_element(By.CLASS_NAME,"inline-metadata-item").text
    #print(title)

driver.quit()