#device
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import csv
import os
import requests
from requests import get

#prevent web close****************
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://192.168.10.86/#/login")

#download
prefs={"download.default_directory":" ~/Downloads"}
options.add_experimental_option("prefs", {
    "download.default_directory": " ~/Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


driver = webdriver.Chrome(service=service, options=options)
    #web IP for 192.168.10.122
driver.get("http://192.168.10.86/#/login")

title = driver.title
driver.implicitly_wait(10)

#login
def login():
    driver.set_window_size(1936, 1056)

    #user input
    text_box = driver.find_element(by=By.CLASS_NAME, value="form-control")
    text_box.send_keys("Admin")
    

    #password input
    #*[@id="uid-xxxxxxxxxx"]
    #/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[2]/div/input
    psword_box = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[2]/div/input')
    psword_box.send_keys("123456")
    time.sleep(5)

    #button submit
    submit_btn = driver.find_element(by=By.XPATH, value='/html/body/div/div/div/main/div/div/div/div/div/div/div/form/div[5]/div/div[2]/div[1]/button')
    submit_btn.click()

login()

 #影像設備
def device():
    device = driver.find_element(By.XPATH, value = '/html[1]/body[1]/div[1]/div[1]/ul[1]/li[4]')
    device.click()
    time.sleep(3)

    camera = driver.find_element(By.XPATH, value = '/html[1]/body[1]/div[1]/div[1]/ul[1]/li[4]/ul[1]/li[1]')
    camera.click()
    time.sleep(3)


    
    device_name - driver.find_element(By.XPATH, value=)
    #if camera ==


       #else: 
        

    #edit_camera

    tablet = driver.find_element(By.XPATH, value = '/html[1]/body[1]/div[1]/div[1]/ul[1]/li[4]/ul[1]/li[2]')
    tablet.click()
    time.sleep(3)

    device_group = driver.find_element(By.XPATH, value = '/html[1]/body[1]/div[1]/div[1]/ul[1]/li[4]/ul[1]/li[3]')
    device_group.click()
    time.sleep(3)

device()