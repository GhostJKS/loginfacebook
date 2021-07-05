from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


# basic login facebook with selelium 
browser = webdriver.Chrome()    

browser.get("https://vi-vn.facebook.com/")


# find username and password with tags
username = browser.find_element_by_id("email")
username.send_keys("")

password = browser.find_element_by_id("pass")
password.send_keys("")

sleep(5)

password.send_keys(Keys.ENTER)


## logout facebook 

# sleep(5)

# choose_setting = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]/i")

# sleep(5)

# choose_setting.click()

# sleep(5)

# log_out = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span")


# sleep(2)

# log_out.click()








