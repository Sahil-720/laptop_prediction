from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/sahil/OneDrive/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=s)      # Launch Chrome
driver.get("https://www.smartprix.com/laptops")
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[4]/input').click()
time.sleep(2)

#driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
#time.sleep(2)

#driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
#time.sleep(3)


old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    try:
        # Try clicking "Load More" button if it exists
        load_more = driver.find_element(By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
        load_more.click()
        print("Clicked Load More")
    except :
        print("No more Load More button found. Exiting loop.")
        break

    # Wait and check if height changes
    time.sleep(4)
    new_height = driver.execute_script('return document.body.scrollHeight')

    print("Old Height:", old_height)
    print("New Height:", new_height)

    if new_height == old_height:
        print("No more content to load. Ending.")
        break

    old_height = new_height

time.sleep(5)

html = driver.page_source

with open('smartprix_24.html','w',encoding='utf-8') as f:
    f.write(html)