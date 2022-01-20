try :
    from lib2to3.pgen2 import driver
    import time
    from selenium.webdriver.chrome.options import Options
    from xml.dom.minidom import Element
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import undetected_chromedriver.v2 as uc
    print('all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))

time.sleep(1)

#driver = webdriver.Chrome('chromedriver.exe')
driver = uc.Chrome(use_subprocess=True)
driver.delete_all_cookies()

# Config
options = Options()
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")





# Url Selection
url = ("https://omi.veve.me/")
driver.get(url);


# E-mail selector
em_xp = ("//input[@name='email']")
time.sleep(1)
email = driver.find_element_by_xpath(em_xp)
email.click()
email.send_keys("philipp.fritz4@gmail.com")
	

# Passwort Selctor
pw_xp = ("//input[@name = 'password']")

Passwd = driver.find_element_by_xpath(pw_xp)
Passwd.send_keys("1Qay2wsx3edc!")



# Press login Button
lg_xp = ("//*[@id='root']/div/header/div/div/header/div/div/div/div[3]/button")

login = driver.find_element_by_xpath(lg_xp)
login.click();

time.sleep(5)

# 2FA Auth 

factor_auth = ("/html/body/div[2]/div[3]/div/div[2]/div/div/div[1]/input]");

auth_input = driver.find_element_by_class("jss9");
auth_input.send_keys(2);

time.sleep(5)


driver.quit()
