# To successfully run this test you should have connected android device
# This script will just open AliExpress Android app on your android device
# AliExpress app should be already installed.
  
 
import unittest
import time
import re
import os
from sys import getdefaultencoding
import codecs


from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from PIL import Image



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'nitrogen_land'

desired_caps['appPackage'] = 'com.tinder'
desired_caps['appActivity'] = 'com.tinder.activities.MainActivity'
desired_caps['noReset'] = 'true'
desired_caps['fullReset'] = False


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



time.sleep(5)

#def swipe_left:

#def swipe_sown:




while 1>0:
	#print("swipe right...")
	#driver.swipe(10, 640, 710, 640, 500)
	time.sleep(2)
	f= codecs.open("tinder.xml","a+",'utf8')
	#print("info...")
	#like=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.ImageView");
	#try:
	elements=driver.find_elements_by_id("com.tinder:id/info_icon")
	if len(elements)>0:
		elements[0].click()
		time.sleep(2)
	else:
		#except NoSuchElementException:
		print("===========no info ==========================")
		driver.swipe(665, 885, 665, 105, 709)
		time.sleep(2)
		continue
	
	if os.path.isfile('screenshot.png'):
		os.remove('screenshot.png')
	if os.path.isfile('screenshot.jpg'):
		os.remove('screenshot.jpg')
	driver.save_screenshot('screenshot.png')
	im = Image.open('screenshot.png')
	im.convert('RGB').save('screenshot.jpg',"JPEG") #this converts png image as jpeg
	
	
	elements=driver.find_elements_by_id("com.tinder:id/profile_text_name")
	if len(elements)>0:
		name=elements[0].get_attribute('text')
		print(name)
		m = re.search('(\w+),', name)	
		if m:
			name = m.group(1)
		else:
			print("================ error regex 70, click X ================")
			info=driver.find_element_by_id("com.tinder:id/gamepad_pass")
			info.click()
			#driver.swipe(665, 885, 665, 105, 709)
			#time.sleep(2)
			#driver.swipe(665, 885, 665, 105, 709)
			#time.sleep(2)
			continue
	
	elements=driver.find_elements_by_id("com.tinder:id/profile_text_age")
	if len(elements)>0:
		age=elements[0].get_attribute('text')
		
	elements=driver.find_elements_by_id("com.tinder:id/profile_text_location")
	if len(elements)>0:
		location=elements[0].get_attribute('text')
		if m:
			m = re.search('\d*', location)	
			location = m.group(0)
		else:
			print("================ error regex , swipe left ================")
			driver.swipe(665, 885, 665, 105, 709)
			time.sleep(2)
			continue
	
	print("swipe down...")
	driver.swipe(665, 885, 665, 105, 709)
	time.sleep(2)
	
	
	print("share...")
	elements=driver.find_elements_by_id("com.tinder:id/recommend_title")
	if len(elements)>0:
		elements[0].click()
		time.sleep(2)
	else:
		print("===========no shares==========================")
		print("swipe left...")
		driver.swipe(665, 885, 665, 105, 709)
		time.sleep(2)
		continue

	
	print("icons...")
	icons=driver.find_elements_by_id("android:id/icon")
	#print(icons, len(icons))
	time.sleep(2)
	
	if len(icons)<4:
		continue
		
	print("click icon...")
	icons[4].click()
	time.sleep(2)
	
	
	print("get clipboard...")
	go=driver.get_clipboard_text()
	#print(go)
	
	
	#element=driver.find_element_by_id("com.tinder:id/text_view_bio")
	#bio=element.get_attribute('text')
	
	
	m = re.search('(https.+)', go)
	if m:
		url = m.group(1)
		print(url)
		#f.write(url)
		#f.write('\n')
		
		m = re.search('com/(...........)-',url)
		if m:
			filename = m.group(1)
			print(filename, age, name, location)
			if os.path.isfile(filename+'.jpg'):
				os.remove(filename+'.jpg')
			os.rename('screenshot.jpg', filename+'.jpg')
			f.write('<girl img="'+filename+'.jpg" age="'+age+'" location="'+location+'" name="'+name+'" url="'+url+'"></girl>' )
			f.write('\n')
	f.close()
	print("pass...")
	#like=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.ImageView");
	elements=driver.find_elements_by_id("com.tinder:id/gamepad_pass")
	if len(elements)>0:
		elements[0].click()
		time.sleep(2)
	else:
		print("===========no 888 shares==========================")
		print("back left...")
		driver.back()
		time.sleep(2)



#print("like...")
#like=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.ImageView");
#like=driver.find_element_by_id("com.tinder:id/gamepad_like")
#like.click();

#com.tinder:id/text_view_bio
#com.tinder:id/piv_image
#com.tinder:id/info_icon
#
#com.tinder:id/profile_job
#com.tinder:id/profile_text_location
#com.tinder:id/profile_text_name
#com.tinder:id/profile_text_age
#
#com.tinder:id/gamepad_pass
#com.tinder:id/recommend_title
#android:id/icon
#com.tinder:id/tappable_carousel_imageview




		
