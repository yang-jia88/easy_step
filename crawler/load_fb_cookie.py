from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json as jason
p = "24154589"

options = Options()

options.chrome_executable_path = "chromedriver.exe"

prefs = {'profile.default_content_setting_values' :{'notifications' : 2}}
options.add_experimental_option('prefs', prefs)

# options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")
cookiefile = open("fuck_cookie.json")
cookies = jason.loads(cookiefile.read())
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
cookiefile.close

# account = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"email")))
# account.send_keys("hong055180@gmail.com")
# secret = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"pass")))
# secret.send_keys(p)
# login_button = driver.find_element(By.CLASS_NAME,"_6ltg")
# login_button.click()

# cookie = driver.get_cookies()
# jcookie = jason.dumps(cookie)
# with open ("fuck_cookie.json","w") as file:
#     file.write(jcookie)

i= 1
while i >0 :
    continue