import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import os
from pymongo import MongoClient


# Replace this with the UUID you want to search for
uuid_to_search = "your_uuid_here"
# Launch a Chrome browser
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://192.168.10.86/#/login")
driver.maximize_window()

def downloads():
    prefs={"download.default_directory":"\download"}
    options.add_experimental_option("prefs", prefs)
downloads()

def web_driver():
    title = driver.title
    driver.implicitly_wait(10)
web_driver()

#login
def login():
    #user input#
    text_box = driver.find_element(by=By.CLASS_NAME, value="form-control")
    text_box.send_keys("Admin")
    
    #password input#
    psword_box = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[2]/div/input')
    psword_box.send_keys("123456")
    time.sleep(5)

    #button submit#
    submit_btn = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[5]/div/div[2]/div[1]/button')
    submit_btn.click()
login()

# Locate the search input field and enter the UUID#
def person_search():
    try:
        # 定位搜尋輸入框
        search_input = driver.find_element(By.XPATH,  value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
        search_input.send_keys('Karen')

        # Submit the search query (if necessary)#
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

        #show search result#
        print('相關搜尋:')

        #click detail#
        related = driver.find_element(By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[9]/div[1]/span[1]/div[1]/button[1]')
        related.click()
        time.sleep(3)


        #export related#
        result = driver.find_element(By.XPATH,"//button[contains(text(),'匯出')]")
    
        #Export excel_daily#
        result = driver.find_element(By.XPATH,"//button[contains(text(),'匯出')]")
        result.click()
        driver.implicitly_wait(10)
        time.sleep(10)

        #export setting & export  #        
        export_download= driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[5]/div[1]/div/div/footer/button[2]')
        export_download.click()
        driver.implicitly_wait(10)
        time.sleep(10)
        print("搜尋與下載完成")


        #finish download and close setting window#
        close_setting =driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/main/div/div/div/div/div/div[5]/div[1]/div/div/footer/button[1]')
        close_setting.click()
        driver.implicitly_wait(10)
        time.sleep(10)
        print("關閉下載")
    
    except NoSuchElementException:
        print('定位失敗')
person_search()    

personverifyresult = "/home/aira/product/data"  

######## Mongdb check ##############
# 檢查是否有相對的MongoDB文件#
def check_mongodb_data_files(personverifyresult):
    if os.path.exists(personverifyresult):
        for root, dirs, files in os.walk(personverifyresult):
            for file in files:
                if file.startswith("mongod.") and file.endswith(".ns"):
                    return True
    return False
#check_mongodb_data_files()



# 檢查是否有MongoDB文件 #
mongodb_data_exists = check_mongodb_data_files(personverifyresult)

# 有MongoDB文件讀文件，使用Selenium搜尋網頁#








# Close the browser#
driver.quit()
