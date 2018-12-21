from requests import get
from bs4 import BeautifulSoup
import selenium as se
from selenium import webdriver
import json

tag_list = []

options = se.webdriver.ChromeOptions()
options.add_argument('headless')
driver = se.webdriver.Chrome(chrome_options=options)
driver.get('https://giphy.com/gifs/LTFbyWuELIlqlXGLeZ')

tags = driver.find_elements_by_class_name('_27zOZRTX_QHrDk1ECyWgdY')
for item in tags:
	print (item.text)
	tag_list.append(item.text)
json.dump(tag_list,open('tags.json','w'),indent=2)







