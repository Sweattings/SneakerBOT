import email
from lib2to3.pgen2.token import OP
import time
from selenium.webdriver.chrome.options import Options
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Config
options = Options()
options = webdriver.ChromeOptions()
# Webdriver
driver = webdriver.Chrome('chromedriver.exe', options=options)

# Headless
options.headless = True
#options.addArguments("--headless", "--disable-gpu", "--window-size=1920,1200","--ignore-certificate-errors","--disable-extensions","--no-sandbox","--disable-dev-shm-usage");

# Url Selection
url = "https://omi.veve.me/";
driver.get(url);


# E-mail selector
em_xp = ("//input[@name='email']")
time.sleep(1)
email = driver.find_element_by_xpath(em_xp)
email.click()
email.send_keys("philipp.fritz4@gmail.com")
time.sleep(3)


# Passwort Selctor
pw_xp = ("//input[@name = 'password']")
time.sleep(3)
Passwd = driver.find_element_by_xpath(pw_xp)
Passwd.send_keys("1Qay2wsx3edc!")
time.sleep(2)


# Press login Button
lg_xp = ("//*[@id='root']/div/header/div/div/header/div/div/div/div[3]/button")

login = driver.find_element_by_xpath(lg_xp)
login.click()




time.sleep(5)
driver.quit()

