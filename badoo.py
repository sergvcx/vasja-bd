import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

	
driver = webdriver.Firefox()
#driver.wait = WebDriverWait(driver, 10)
driver.get("http://www.badoo.com")
#assert "metro" in driver.title

#try:
#button = driver.wait.until(EC.element_to_be_clickable(By.CLASS_NAME,"btn btn--xsm btn--glass js-inside-link js-signin-link"))
#button = driver.wait.until(EC.element_to_be_clickable(By.CLASS_NAME,"btn__content"))
#button = driver.wait.until(EC.element_to_be_clickable(By.CLASS_NAME,"/html/body/div[2]/div[2]/div[3]/div/div[1]/header/div/div[2]/div/div/a/div"))
time.sleep(10)
print("start find")
content = driver.find_elements_by_class_name('btn.btn--xsm.btn--glass.js-inside-link.js-signin-link')
# !!! content = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div/div[1]/header/div/div[2]/div/div/a')
# !!! content = driver.find_element_by_css_selector('a.btn--xsm')

print("find=",content)
print("LEN=",len(content))
content[0].click()
#button[0].click()
  
  #/html/body/div/div[4]/div[3]/div/div[1]/div[2]
  #body > div > div.c-branding-layer.c-layer.metro > div.footer > div > div.c-branding-button.icon-left.join > div.text
  
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.NAME, "btnK"))
#element.click();
#except TimeoutException:
 #       print("Button not found")
 
#finally:
time.sleep(10)

driver.close()

	
#assert "metro" in driver.page_source
#
##elem = driver.find_element_by_name("q")
#time.sleep(10)
#results = driver.find_elements_by_class_name('text')
#print(results[0].text)
#
#results[0].click()
#
#time.sleep(20)
#
#results = driver.find_elements_by_class_name('interaction_button_quiz')
#print(results[0].text)
#
#time.sleep(5)
#
#results[0].click()
#
#time.sleep(10)
#results = driver.find_elements_by_class_name('mt-banner-fullscreen__button-close')
#print(results[0].text)
#


#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()