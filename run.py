from bs4 import BeautifulSoup as bsp
import requests as rq
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as dc



dcap=dict(dc.CHROME).copy()
dcap['chrome.switches']=('--user-agent=Demo bot')
url="https://www.amazon.in/gp/goldbox?ref_=nav_topnav_deals"
option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(desired_capabilities=dcap,chrome_options=option,service_args=['--ssl-protocol=any','--ignore-ssl-errors=true'])
driver.get(url)

html=driver.page_source
soup=bsp(html,'html.parser')



with open('url.txt','r') as f:
    url=f.read()


driver.get(url)

import telegram
bot = telegram.Bot(token='907325483:AAGA3AVlak3GCnMoo9AuB4BKHkXs41lFRhA')


#print(status)

def return_data():
    #print(driver.current_url)
    title=driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
    price=driver.find_element(By.XPATH,'//*[@id="priceblock_dealprice"]').text
    merchant_info=driver.find_element(By.XPATH,'//*[@id="merchant-info"]').text

    image_url=driver.find_element(By.XPATH,'//*[@id="landingImage"]').text

    new_url=driver.current_url
    tmp_url_2=new_url.split('/')
    final_url=tmp_url_2[0]+"//"+tmp_url_2[2]+"/"+tmp_url_2[4]+"/"+tmp_url_2[5]+"/?tag=letstri-21"
    return title,price,merchant_info,final_url,image_url


element=soup.find_all(attrs={'class':'a-section a-spacing-none tallCellView gridColumn3 singleCell'})
wait=WebDriverWait(driver,20)
page=0
for elm in element:
    url2=driver.find_elements(By.XPATH, '//*[@id="dealImage"]')[page]
    page+=1
    href=url2.get_attribute('href')
    driver.get(href)
    try:
        title,price,merchant_info,final_url,image_url=return_data()
        print("Product: "+title)
        print("Click Here"+final_url)
        print("Only at: "+price)
        print(image_url)
        print(merchant_info)
        print("-"*20)
        message="<b> "+title+'\n \n Only at:- '+price+"</b>\n \n \n  <a href='"+final_url+"'>"+final_url+"</a>"+'\n' +merchant_info
        bot.send_message(chat_id="@alfaguria", text=message, parse_mode=telegram.ParseMode.HTML)
        #bot.send_photo(chat_id="@alfaguria",photo=image_url)
    except:
        pass

    driver.execute_script("window.history.go(-1)")


