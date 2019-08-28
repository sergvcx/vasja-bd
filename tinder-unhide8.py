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
from selenium.webdriver.chrome.options import Options 
 
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver.implicitly_wait(10) # seconds





#chrome_options = Options()
#chrome_options.add_argument("--user-data-dir=chrome-data")
#driver = webdriver.Chrome(options=chrome_options)
#chrome_options.add_argument("user-data-dir=chrome-data") 
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data8881")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
#chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get("https://tinder.com/")

#time.sleep(160)  # Time to enter credentials





#print("load cookies")
#cookies = pickle.load(open("tinder2.pkl","rb"))
#for cookie in cookies:
#    driver.add_cookie(cookie)
#

#driver.refresh()	
#time.sleep(5)
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button/span")))
#print("======== log in ================================")
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='button__text Pos(r) Z(1)' and contains(text(), 'Log in')]")))
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='button__text Pos(r) Z(1)']")))

#time.sleep(5)
#driver.refresh();
#exit();
#time.sleep(5)

#element = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element("Log in"))
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'button__text.Pos(r).Z(1).D(ib)')))
#element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div/button/span/span')
#print("text=",element.text)
#print("class=",element.get_attribute("class"))
#element.click();

#print("====== login by phone number ==================================")
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button/span/span")))
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='button__text Pos(r) Z(1) D(ib)' and contains(text(), 'Log in with phone number')]")))
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='button__text Pos(r) Z(1) D(ib)']")))
#print(element.text)
#element.click();


#print("======= enter phone number =================================")
#time.sleep(5)
#element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div/input")))
#element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/input')
#print(element.text)
#element.send_keys("")
#element.send_keys(Keys.RETURN)
#time.sleep(30)

#print("======= save coockies =================================")
#all_cookies = driver.get_cookies()
#pickle.dump(all_cookies, open("tinder2.pkl","wb"))
#print("cookies=",all_cookies)


print("======= open hidden pics =================================")
#element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div[2]/div[1]/div[1]/div[1]/a/div/div[2]/div")))
#element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, " /html/body/div[1]/div/div[1]/div/aside/nav/div/div/div/div[2]/div[1]/div[1]/div[1]/a/div/div[2]")))
time.sleep(2)
element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "StretchedBox.CenterAlign")))

#element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/input')
print(element)
print(element.text)
time.sleep(2)
#print("******* click ")
element.click()


element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "Expand.enterAnimationContainer")))
#print(element)
#print(element.text)

#element = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[2]/div')
#element.send_keys(Keys.PAGE_DOWN)



elements = driver.find_elements_by_class_name('Expand.enterAnimationContainer')
i=0



#print("start scrool")
#time.sleep(5)
#driver.switch_to.frame(driver.find_element_by_css_selector("frame[name='nav']"))

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
	#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	pic.location_once_scrolled_into_view
	#time.sleep(1)
	print("*****************",i)
	style=pic.get_attribute("style")
	#print("style=",i,style)
	ss=re.split("\"",style)
	#print(ss, len(ss))
	#f (len(ss)>0):
	url=ss[1]
	print(url)
	urllib.request.urlretrieve(url, str(i)+".jpg")
	i=i+1

#driver.quit()









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