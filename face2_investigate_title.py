##person title 

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

 #文字
def investigation_test():
    report = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/ul/li[2]')
    report.click()
    investigation = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/ul/li[2]/ul/li[3]/a')
    investigation.click()
    time.sleep(5)

    correct_functions = ["時間", "人員資訊來源", "人員編號",
                        "人員姓名", "卡號", "群組名稱", "通行模式", "分數", "抓拍照片", "備註"]
    side_function_element = driver.find_element(by=By.CLASS_NAME, value="vxe-cell--title")
    time.sleep(5)
    side_functions= [tmp.text for tmp in side_function_element.find_elements(By.CLASS_NAME, "vxe-cell--title")]
    time.sleep(5)
    try:
        assert side_functions == correct_functions
        print("標題正確!")
        time.sleep(5)

    except AssertionError as title_error:
        print(title_error)
        time.sleep(5)

investigation_test()
time.sleep(10)
    