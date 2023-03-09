from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://hdhub4u.show/")
driver.maximize_window()
driver.implicitly_wait(10)

current_url = driver.current_url
new_url = current_url.replace('https://hdhub4u.show/','https://hdhub4u.show/farzi-season-1-hindi-webrip-all-episodes/')
url_2 = current_url.replace('https://hdhub4u.show/','https://carelife4u.com/')

driver.get(new_url)
driver.get(url_2)

url_2_1 = driver.find_element(By.ID,"soralink-human-verif-main")
url_2_1.click()
#url_3 = current_url.replace('https://hdhub4u.show/','https://carelife4u.com/quick-claim-settlement-with-top-car-insurance-companies/#generate')
#driver.get(url_3)

#url_4 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="showlink"]')))
#url_4.click()



#link = driver.find_element(By.XPATH,'/html/body/section/div/section/main/div[3]/h3[2]/a')

#download = driver.find_element(By.XPATH,'//*[@id="soralink-human-verif-main"]')

#download = driver.find_element(By.XPATH,'//*[@id="generater"]/img')


