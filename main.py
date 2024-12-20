from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.maximize_window()

datas = []
driver.get("https://letterboxd.com/aliblade/films/diary/")
data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody")
datas.append(data.text)

'''
try:
    older_button = driver.find_element(By.CLASS_NAME,"next")
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/section[2]/div[2]/div[3]/ul')))
    pages = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[2]/div[2]/div[3]/ul')
    for i in range(len(pages.text.splitlines())):
        print("im here",len(pages.text.splitlines()))
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"next")))
        older_button.click()
        time.sleep(2)
        data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody") #/html/body/div[1]/div/section[2]/div[2]/div[3]/ul /html/body/div[1]/div/section[2]/table/tbody /html/body/div[1]/div/section[2]/div[2]/div[3]/ul /html/body/div[1]/div/section[2]/div[2]/div[3]/ul
        datas.append(data.text)
        print(datas)

except:
    pass

'''

try:
    older_button = driver.find_element(By.CLASS_NAME,"next")
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/section[2]/div[2]/div[3]/ul')))
    pages = driver.find_element(By.XPATH,'/html/body/div[1]/div/section[2]/div[2]/div[3]/ul')
    for i in range(1,len(pages.text.splitlines())+ 1):
        driver.get(f"https://letterboxd.com/aliblade/films/diary/page/{i}/")
        time.sleep(2)
        data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody")
        datas.append(data.text)
    print(datas)

except:
    pass








'''
while driver.find_element(By.CLASS_NAME,"next"):
    older_button.click()
    data = driver.find_element(By.XPATH,"/html/body/div[1]/div/section[2]/table/tbody")
    datas.append(data.text)

print(datas)


findsnothing.send_keys("Barisc36.")
findsnothing.send_keys(Keys.ENTER)
#WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.NAME,"btnK")))

#search_button.click()
'''
time.sleep(30)
