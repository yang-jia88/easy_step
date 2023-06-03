from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 
import wget

from selenium.webdriver.common.keys import Keys

options = Options()

options.chrome_executable_path = "chromedriver.exe"

# options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
searchkey = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"q")))
searchkey.send_keys("twice momo")

check = driver.find_element(By.CLASS_NAME,"gNO89b")
check.click()
driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
elements = driver.find_elements(By.CLASS_NAME,'wXeWr')
i = 0
href = []
for e in elements[:10]:
        time.sleep(1)
        e.click()
        time.sleep(1)
        href.append(e.get_attribute("href"))
        i+=1
print(href)
src = []
for link in href[:10]:
    driver.get(link)
    time.sleep(1)
    bigpic = driver.find_element(By.CLASS_NAME,"r48jcc")
    src.append(bigpic.get_attribute("src"))

filepath = "pic"
if not os.path.isdir("pic"):
    os.mkdir("pic")


save_as = os.path.join(filepath,"1.jpg")
wget.download(src[0],save_as)

while True:
    continue

#driver.find_element(By.XPATH,'//*[text()="圖片"]').click()
# driver.find_element(By.XPATH,'//*[text()="工具"]').click()
# driver.find_element(By.XPATH,'//*[text()="大小"]').click()
# driver.find_element(By.XPATH,'//*[text()="大"]').click()