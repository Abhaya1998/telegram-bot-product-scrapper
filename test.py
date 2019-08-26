from bs4 import BeautifulSoup as bsp
import requests as rq
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url="https://www.amazon.in/gp/goldbox?ref_=nav_topnav_deals"
option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome()
driver.get(url)
#r=rq.get(url)
#print(r)
html=driver.page_source
soup=bsp(html,'html.parser')


element=soup.find_all(attrs={'class':'a-section a-spacing-none tallCellView gridColumn3 singleCell'})
for elm in element:
    container=elm.find(attrs={'class':'a-section dealContainer'})
    layer=container.find(attrs={'class':'a-section layer'})
    image=layer.find(attrs={'id':'dealImage'})
    image_url=image.attrs['href']
    #print(image_url)
    price_tag=layer.find(attrs={'class':'a-row priceBlock unitLineHeight'})
    #print(price_tag.text)
    name_tag=layer.find(attrs={'class':'a-declarative'})
    span=layer.find('span',{'data-action':'gbdeal-actionrecord'})

    #print(len(span.text))
    #print(driver.find_element_by_class_name('a-declarative').get_attribute('innerHTML'))

    #print(name_tag)
    span_text=driver.find_element(By.XPATH, '//*[@id="dealTitle"]/span').get_attribute('innerHTML')
    print(span_text)
    #print(span.span)
    #print(name_tag.find_element_by_class_name('/a-declarative').text)
    #time.sleep(0.4)
