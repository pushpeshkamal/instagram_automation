from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)

driver.get("https://www.instagram.com")
elem = driver.find_element_by_id("txtEmailAddress")
elem.clear()
elem.send_keys("Username")
elem = driver.find_element_by_id("txtPassword")
elem.send_keys("1234")
print("Password Entered")
driver.find_element_by_id("btnSignIn").click()
print("Logged In")