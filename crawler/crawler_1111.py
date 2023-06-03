from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.keys import Keys

options = Options()

options.chrome_executable_path = "chromedriver.exe"

# options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


driver = webdriver.Chrome(options=options)
driver.get("https://www.1111.com.tw/")

searchkey = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"ks")))
searchkey.send_keys("大數據")
check = driver.find_element(By.ID,"searchjobBtn")
check.click()
y=800
while True:
    time.sleep(1)
    y+=800
    driver.execute_script("window.scrollTo(0,"+str(y)+")") #滑動
    print(y)


# soup = BeautifulSoup(driver.page_source,"html.parser")
# print(soup.find_all("h5",class_="card-title title_6")[0].text)




# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform() 當enter 輸入



