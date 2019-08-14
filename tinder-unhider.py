import urllib.request
import re
import time
import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
 
 
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver.implicitly_wait(10) # seconds



driver.get("https://tinder.com/")
#time.sleep(5)
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div/button/span/span")))
#results = driver.find_elements_by_class_name('button__text Pos(r) Z(1) D(ib)')
#element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div/button/span/span')
print(element)
print(element.text)
element.click();

element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button/span/span")))
#element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button/span/span')
print(element)
print(element.text)
element.click();

#time.sleep(5)
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div/input")))
#element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/input')
print(element)
print(element.text)
#element.send_keys("")
#element.send_keys(Keys.RETURN)

time.sleep(30)

all_cookies = driver.get_cookies()
print("cookies=",all_cookies)

#element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div[2]/div[1]/div[1]/div[1]/a/div/div[2]/div")))
element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, " /html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div[2]/div[1]/div[1]/div[1]/a/div/div[2]")))
#element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "StretchedBox.CenterAlign")))

#element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/input')
print(element)
print(element.text)
element.click()




element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "Expand.enterAnimationContainer")))
print(element)
print(element.text)
elements = driver.find_elements_by_class_name('Expand.enterAnimationContainer')
i=0
for e in elements:
	#print("e e=",e)
	#print("e tag=",e.tag_name)
	#print("e class=",e.get_attribute("class"))
	#print("e style=",e.get_attribute("style"))
	#print("e text=",e.text)
	pic = e.find_element_by_xpath(".//div");
	#print("pic tag=",pic.tag_name)
	#print("pic class=",pic.get_attribute("class"))
	#print("pic style=",pic.get_attribute("style"))
	#print("pic text=",pic.get_attribute("href"))
	style=pic.get_attribute("style")
	print("style=",i,style)
	ss=re.split("\"",style)
	print(ss, len(ss))
	if (len(ss)>0):
		url=ss[1]
		print(url)
		urllib.request.urlretrieve(url, str(i)+".jpg")
	i=i+1











#element = driver.find_element_by_class_name("button__text Pos(r) Z(1) D(ib)")
#try:
#	#element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "button__text Pos(r) Z(1) D(ib)")))
#	element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "button__text Pos(r) Z(1)")))
#except TimeoutException:
#	print('Timeout')
#print(element)
#element.click();



##driver.get("https://mail.ru")
##time.sleep(60)
##cookies = pickle.load(open("what.pkl", "rb"))
##cookies = pickle.load(open("mail.pkl", "rb"))
##for cookie in cookies:
##   driver.add_cookie(cookie)
#total_online=0;
#dt =1
#f = open("tinder.log",'w',encoding='utf-8')
#
#try:
#    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "button__text Pos(r) Z(1) D(ib)")))
#except TimeoutException:
#	print('Timeout')
#else:
#	print('OK')
#finally:
#    driver.quit()
	
#try:
    #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.className, "button__text Pos(r) Z(1) D(ib)")))
	#	element.click()
#finally:
#	print ("Error")
 #   driver.quit()
	
	
#while 1:
#	time.sleep(dt);		
#	page= driver.page_source
#	ret=page.find("")
#	#ret=page.find("")
#	if ret>0:
#		start_online =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#		while 1:
#			time.sleep(dt);		
#			page= driver.page_source
#			#ret=page.find("")
#			ret=page.find("")
#			total_online = total_online+dt;
#			if ret==-1:
#				stop_online =  datetime.datetime.now().strftime("%H:%M:%S")
#				#stop_online =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#				line= start_online + " = " + stop_online + " "+str(total_online)
#				print(line)
#				print(line,file=f)
#				f.flush()
#				break;
#	
#pickle.dump( driver.get_cookies() , open("what.pkl","wb"))
#pickle.dump( driver.get_cookies() , open("mail.pkl","wb"))
#driver.quit()