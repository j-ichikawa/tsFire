import os
import sys
import time

from jsmin import jsmin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

login_id = sys.argv[1]
password = sys.argv[2]

userdata_dir = 'UserData'
os.makedirs(userdata_dir, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=' + userdata_dir)

with webdriver.Chrome(executable_path='./chromedriver', options=options) as driver:
    driver.get('https://ap.salesforce.com/home/home.jsp')

    # Login
    driver.find_element_by_name('username').send_keys(login_id)
    driver.find_element_by_name('pw').send_keys(password)
    driver.find_element_by_name('Login').click()

    kinmu_tab_id = '01r100000009qXD_Tab'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, kinmu_tab_id)))
    driver.find_element_by_id(kinmu_tab_id).click()

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'largeTable')))
    time.sleep(3)

    with open('kinmu_inputter.js') as f:
        js_min = jsmin(f.read())
        driver.execute_script(js_min)
        time.sleep(300)  # during execute js
