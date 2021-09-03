#importing the packages and libraries

import time
from pyautogui import press
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#simulating the mobile agents

opts= Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
driver.get("https://www.instagram.com")

#credentials of your instagram
username = "username"
pasw = "password"

# paving the way to the next page

press('tab')
time.sleep(0.3)
press('tab')
time.sleep(0.3)
press('tab')
press('return')

#entering credentials using xpath from inspect element

enter_email = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")
enter_email.send_keys(username)
enter_pass = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input")
enter_pass.send_keys(pasw)
press('tab')
press('tab')
press('tab')
press('return')
time.sleep(4)

#eliminating save info to browser popup by "tab" navigation

press('tab')
press('return')
