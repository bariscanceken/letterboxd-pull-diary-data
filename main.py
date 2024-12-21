from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os

#os
base_dir = os.path.dirname(os.path.abspath(__file__))
path_diarydata = os.path.join(base_dir, 'diarydata.txt')

#selenium
driver = webdriver.Chrome()
driver.maximize_window()
datas = []
who = input("Enter Username: ")
link = f"https://letterboxd.com/{who}/films/diary/"
driver.get(link)
data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody")
datas.append(data.text)
driver.get(link)

try:
    data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody")
    datas.append(data.text)
    older_button = driver.find_element(By.CLASS_NAME,"next")
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/section[2]/div[2]/div[3]/ul')))
    pages = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[2]/div[2]/div[3]/ul')
    with open(path_diarydata, 'a',encoding="utf-8") as dosya:
        dosya.write(datas[0])
    for i in range(2,len(pages.text.splitlines())+ 1):
        driver.get(f"{link}page/{i}/")
        time.sleep(2)
        data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody")
        datas.append(data.text)
        with open(path_diarydata, 'a',encoding="utf-8") as dosya:
            dosya.write(datas[i])
except:
    with open(path_diarydata, 'a',encoding="utf-8") as dosya:
        dosya.write(datas[0])