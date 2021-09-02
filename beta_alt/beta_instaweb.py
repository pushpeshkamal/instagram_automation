#from _typeshed import Self
import selenium
import time
from pyautogui import press

from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

import keyboard
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

opts= Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
driver.get("https://www.instagram.com")

username = "if you like it,star it"
pasw = "subscribe to techcartels"
time.sleep(1)

press('tab')
press('tab')
press('tab')
press('return')
#login_element = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]")
#driver.execute_script('arguments[0].click();', login_element )


enter_email = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")
enter_email.send_keys(username)

enter_pass = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input")
enter_pass.send_keys(pasw)

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]").click()
time.sleep(1)

#press('tab')
press('return')

#def login(driver,username,pas):
#    bot = driver.bot
#    bot.get("https://www.instagram.com")
#    time.sleep(2)
#    login_btn= bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]")
#    login_btn.click()
#    time.sleep(2)
#
#    )
#    login_btn_final= bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]")
#    login_btn_final.click()
#    time.sleep(2)
#
#login(self.bot,email,pasw)