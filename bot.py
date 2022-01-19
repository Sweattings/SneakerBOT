import email
from optparse import Option
import time
from xml.dom.minidom import Element
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe', options=options)

# Url Selection
url = "https://omi.veve.me/";
driver.get(url)

# E-mail slector
button = driver.find_element_by_class_name("MuiInputBase-input")
button.click()


button2 = driver.find_element_by_class_name("c-form-field--email")
button2.click()


time.sleep(1)


driver.quit()

