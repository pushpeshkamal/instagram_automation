from selenium import webdriver
#from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

opts= Options()

opts.add_argument("--user-agent=Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

driver.get("https://www.instagram.com")

