from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

open_site = driver.get("https://app.buissmaster.com/")
driver.maximize_window()
driver.implicitly_wait(20)

login_details = ["jayvaghasiya175@gmail.com","Buiss@123"]
detail_input = driver.find_elements(By.CSS_SELECTOR,"input")

for i in detail_input:
    for j in login_details:
        if detail_input.index(i) != login_details.index(j):
            continue
        else:
            i.send_keys(j)

login_button = driver.find_element(By.XPATH,"//*[@id=\"login\"]")
login_button.click()

claim_button = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div/div[2]")
claim_button.click()

meesho_button = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/ul/div[2]/div/div/div/a[1]/div[2]")
meesho_button.click()

select_account = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div[3]/main/div/div/div/div/div[1]/div[1]/div/div/div/div/button").click()
drop_down = driver.find_element(By.CSS_SELECTOR,"input")
drop_down.send_keys(Keys.DOWN)
drop_down.send_keys(Keys.ENTER)

ticekt_button = driver.find_elements(By.XPATH,"//*[@id=\"mui-p-71585-P-PENDI_Not_Rec\"]/div[2]/div[2]/table/tbody/tr[2]/td/div/div/div/div/div[5]/button")
for i in ticekt_button:
    if ticekt_button.index(i) < 2:
        continue
    else:
        i.click()
driver.quit()

