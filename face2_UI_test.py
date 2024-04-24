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

#download
prefs={"download.default_directory":"\download"}
options.add_experimental_option("prefs", prefs)


#********************************************

driver = webdriver.Chrome(service=service, options=options)
    #web IP for 192.168.10.122
driver.get("http://192.168.10.122/#/login")

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


#UI for Face2
def UI_xs():
 
    title = driver.title
    driver.implicitly_wait(10)

    #sidebar click
    #出勤
    def attendance():
        sidebar= driver.find_element(by=By.LINK_TEXT, value="出勤")
        sidebar.click()
        time.sleep(5)
    attendance()
    
                            
    #daily atterdance
    def daily_attend():
        sidebar_daily = driver.find_element(by=By.LINK_TEXT, value="日出勤")
        sidebar_daily.click()
        time.sleep(5)
    daily_attend()
    
    #Export excel_daily
    def daily_export():
        excel_exp = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/button[1]')
        excel_exp.click()
        driver.implicitly_wait(10)
        #export setting & export          
        daily_export_download= driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/footer[1]/button[2]')
        daily_export_download.click()
        time.sleep(5)

        #finish download and close setting window
        close_setting = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/footer[1]/button[1]')
        close_setting.click()
        time.sleep(5)
    daily_export()

    
    #monthly atterdance
    def monthly_attend():
        sidebar_monthly = driver.find_element(by=By.LINK_TEXT, value="月出勤")
        sidebar_monthly.click()
        time.sleep(5)
    monthly_attend()

    #Export excel_monthly
    def monthly_export():
        excel_exp = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/button[1]')
        excel_exp.click()
        time.sleep(5)

        #export setting & export          
        month_export_download= driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/footer[1]/button[2]')
        month_export_download.click()
        time.sleep(5)

        #finish download and close setting window
        close_setting = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/footer[1]/button[1]')
        close_setting.click()
        time.sleep(5)
    monthly_export()

    #出勤設定
    def attendance_setting():
        attendance_setting = driver.find_element(by=By.LINK_TEXT, value="出勤設定")
        attendance_setting.click()
        time.sleep(5)
    attendance_setting()

    #出勤操作
    def change_attendance():
        change_attendance = driver.find_element(by=By.LINK_TEXT, value="出勤操作")
        change_attendance.click()
        time.sleep(5)

        #search 
        search = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/col[1]/button[1]')
        search.click()
        time.sleep(10) 
    change_attendance()

    #報表
    def report():
        report = driver.find_element(by=By.LINK_TEXT, value="報表")
        report.click()
        time.sleep(5)

        person_report = driver.find_element(by=By.LINK_TEXT, value="人員報表")
        person_report.click()
        time.sleep(5)

        visitor_report = driver.find_element(by=By.LINK_TEXT, value="訪客報表")
        visitor_report.click()
        time.sleep(5)

        investigate = driver.find_element(by=By.LINK_TEXT, value="調查")
        investigate.click()
        time.sleep(5)

    report()

    #人員
    def person_sidebar():
        person = driver.find_element(by=By.CLASS_NAME, value='c-sidebar-nav-dropdown-toggle')
        person.click()
        time.sleep(5)
        
        person1 = driver.find_element(by=By.XPATH, value='/html[1]/body[1]/div[1]/div[1]/ul[1]/li[3]/ul[1]/li[1]/a[1]')
        person1.click()
        time.sleep(5)

        visitor1 =driver.find_element(by=By.LINK_TEXT, value="訪客")
        visitor1.click()
        time.sleep(5)

        person_group = driver.find_element(by=By.LINK_TEXT, value="群組")
        person_group.click()
        time.sleep(5)

    person_sidebar()








        


























UI_xs()