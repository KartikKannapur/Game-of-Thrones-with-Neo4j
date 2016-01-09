__author__ = "Sachin Saligram"


# Code to extract data from 'http://awoiaf.westeros.org/index.php/List_of_characters'
# Written by: Sachin Saligram
# Date: 06/01/2016

import urllib, requests
from bs4 import BeautifulSoup
from pyquery import PyQuery

url = "http://awoiaf.westeros.org/index.php/List_of_characters#V"

page = requests.get(url).text

soup = BeautifulSoup(page)
count = 0
# for a in soup.find_all('a', href=True):
# 	if '/index.php' in a["href"]:
# 		print a
# 		print "http://awoiaf.westeros.org/" + a["href"]
# 		if count == 10:
# 			exit()
# 		count += 1
#print soup


for a in soup.find_all('li'):
	print a