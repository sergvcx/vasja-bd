import urllib.request
import re
import time
import datetime
import pickle
import codecs
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
chrome_options.add_argument("--user-data-dir=chrome-badoo")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
#chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get("https://badoo.com/search")

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
#time.sleep(2)



#element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/input')
#print(element)
#print(element.text)

#print("******* click ")
#element.click()


#element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "Expand.enterAnimationContainer")))
#print(element)
#print(element.text)

#element = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[2]/div')
#element.send_keys(Keys.PAGE_DOWN)

#<figure class="user-card  js-folders-user-card js-tutorial-user-card" data-user-id="675811994" data-user-position="1" data-my-vote="1">    <div class="user-card__photo">        <img class="user-card__img" src="https://pd1eu.badoocdn.com/p47/10169/5/7/1/675811994/d1644/t1546896910/c_e74VoxduGl74YZFOe-bBuyrxM90IVbmAl8bCP91jMKxI8KEsDkGtwg/1644951/dfs_180x180/sz_191x191.jpg?jpegq=80&amp;t=30.1.0.00" srcset="https://pd1eu.badoocdn.com/p47/10169/5/7/1/675811994/d1644/t1546896910/c_e74VoxduGl74YZFOe-bBuyrxM90IVbmAl8bCP91jMKxI8KEsDkGtwg/1644951/dfs_180x180/sz_191x191.jpg?jpegq=80&amp;t=30.1.0.00 1x, https://pd1eu.badoocdn.com/p47/10169/5/7/1/675811994/d1644/t1546896910/c_e74VoxduGl74YZFOe-bBuyrxM90IVbmAl8bCP91jMKxI8KEsDkGtwg/1644951/dfs_180x180/sz_191x191.jpg?jpegq=80&amp;t=30.1.0.00 2x" alt="Юлия">                <div class="user-card__photo-counter">            <div class="photo-counter">                <div class="photo-counter__icon">                    <i class="icon"><svg class="icon-svg"><use xlink:href="#icon-camera-contour"></use></svg></i>                </div>                <span class="photo-counter__text">4</span>            </div>        </div>                <div class="user-card__marks">                                </div>    </div>            <a class="user-card__link app js-folders-user-profile-link" href="/profile/0675811994?from=search&amp;folder=25&amp;section_id=3&amp;p=1" rel="profile-view" title="Юлия"></a>                            <figcaption class="user-card__caption">        <div class="user-card__actions  js-user-card-actions">            <div class="user-card-actions">                                <div class="user-card-actions__item js-user-action-vote-yes-wrap js-user-card-actions-item js-hp-view-element is-ready" data-element-name="vote-yes">                    <div class="profile-action profile-action--sm profile-action--yes js-user-action-vote-yes">                        <i class="icon icon--spread"><svg class="icon-svg"><use xlink:href="#icon-action-yes-inner"></use></svg></i>                    </div>                </div>                                                                <div class="user-card-actions__item js-user-card-actions-item js-hp-view-element is-ready" data-element-name="chat">                    <div class="profile-action profile-action--sm profile-action--chat js-user-action-chat">                        <i class="icon icon--spread">                            <svg class="icon-svg">                                <use xlink:href="#icon-action-chat-inner"></use>                            </svg>                        </i>                    </div>                </div>                                            </div>        </div>        <div class="user-card__info">            <div class="user-card-caption">                                <div class="user-card-caption__account">                    <span class="user-card-caption__name" dir="auto">Юлия</span>                                        <span class="user-card-caption__age"><span class="comma">,</span> 24</span>                                    </div>                                <div class="user-card-caption__online-status"><!--  --><i class="online-status online-status--offline" data-control-type="tooltip"><span class="tooltip">        <span class="tooltip__content">            Ваш статус скрыт        </span>    </span></i><!--  --></div>                                <div class="user-card-caption__like  js-like-icon">                    <i class="icon icon--like">                        <svg class="icon-svg">                            <use xlink:href="#icon-like-circle"></use>                        </svg>                    </i>                </div>                                                <div class="user-card-caption__like user-card__like--match  js-match-icon" data-control-type="tooltip">                    <i class="icon icon--like">                        <svg class="icon-svg">                            <use xlink:href="#icon-match-circle"></use>                        </svg>                    </i>                    <div class="tooltip">                        <span class="tooltip__content">Это взаимно!</span>                    </div>                </div>                                <div class="user-card-caption__verify"></div>            </div>        </div>                <span class="user-card__location" dir="auto">~30 км от вас</span>                            </figcaption></figure>

i=0



#print("start scrool")
#time.sleep(5)
#driver.switch_to.frame(driver.find_element_by_css_selector("frame[name='nav']"))


fs = codecs.open('badoo.xml', 'w',  "utf-8")
#fs.write(codecs.BOM_UTF8)
fs.write('<?xml version="1.0" ?>\n');
fs.write('<?xml-stylesheet type="text/xsl" href="badoo.xsl"?>\n');
fs.write('<table name="badoo">\n');

for pages in range(100):
	time.sleep(1)
	element = WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.CLASS_NAME, "users-list__column")))
	elements = driver.find_elements_by_class_name('user-card.js-folders-user-card.js-tutorial-user-card')
	for e in elements:
		#print("e e=",e)
		#print("e tag=",e.tag_name)
		#print("e class=",e.get_attribute("class"))
		#print("e style=",e.get_attribute("style"))
		#print("e text=",e.text)
		data_user_id=e.get_attribute("data-user-id")
		img = e.find_element_by_class_name("user-card__img");
		src = img.get_attribute("src")
		print("data_user_id=",i,data_user_id,src)
		#print("pic tag=",pic.tag_name)
		#print("pic class=",pic.get_attribute("class"))
		#print("pic style=",pic.get_attribute("style"))
		#print("pic text=",pic.get_attribute("href"))
		#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		#pic.location_once_scrolled_into_view
		#time.sleep(1)
		#print("*****************",i)
		#style=pic.get_attribute("style")
		#print("style=",i,style)
		#ss=re.split("\"",style)
		#print(ss, len(ss))
		#f (len(ss)>0):
		#url=ss[1]
		#print(url)
		imgPreview=str(i)+".jpg"
		urllib.request.urlretrieve(src, imgPreview)
		name = e.find_element_by_class_name("user-card-caption__name").text
		e_age = e.find_element_by_class_name("user-card-caption__age");
		age = e_age.text
		e_location=e.find_element_by_class_name("user-card__location")
		location= e_location.text
		url = "https://badoo.com/profile/"+data_user_id
		score=str(i);
		want="x3"
		#fs.write('<girl img="'+imgPreview+'"  name="'+name+'"  age="'+age+'" url="'+url+'">\n');
		fs.write('<girl img="'+imgPreview+'"  name="'+name+'"  age="'+age+'" score="'+score+'" url="'+url+'" location="'+location+'">');
		#fs.write(info,'a');
		fs.write('</girl>\n');
		i=i+1
	#WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.CLASS_NAME, "pagination__item.pagination__item--next.app.js-pages")))
	element = driver.find_element_by_class_name('pagination__item.pagination__item--next.app.js-pages')
	print("********* click ********")
	element.click()
		
	
fs.write('</table>\n');	

fs.close()
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