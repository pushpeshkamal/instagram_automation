import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
opts= Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

email ="techcartels.dots"
pas ="soontobefamous"

driver.get("https://www.instagram.com")
#time.sleep(2)

login_btn= driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]")
login_btn.click()

enter_email = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")
enter_email.send_keys(email)

enter_pass = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input")
enter_pass.send_keys(pas)

login_btn_final= driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]")
login_btn_final.click()
