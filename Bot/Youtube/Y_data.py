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

video_tab = driver.find_element(By.XPATH,"//*[@id=\"tabsContent\"]/tp-yt-paper-tab[2]").click()

list = []
video_title = driver.find_elements(By.CLASS_NAME,"style-scope ytd-rich-grid-renderer")
for i in video_title:
    title = i.find_element(By.XPATH,".//*[@id=\"video-title\"]")
    list.extend(list)

print(list)
#(video_title)
'''for i in video_title:
    text_title = i.text
    list.extend(text_title)
print(list)'''



