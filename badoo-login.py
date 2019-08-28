#http://chromedriver.chromium.org/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-badoo")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
#driver = webdriver.Chrome()
chrome_options.add_argument("user-data-dir=chrome-badoo") 
driver.get("https://badoo.com/")
time.sleep(200)
driver.quit()
