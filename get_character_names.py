__author__ = "Sachin Saligram"


# Code to extract data from 'http://awoiaf.westeros.org/index.php/List_of_characters'
# Written by: Sachin Saligram
# Date: 06/01/2016

# #Python Modules
import urllib, requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

def character_description(var_url):
	page = requests.get(var_url).text
	soup = BeautifulSoup(page)

	data_character = {}

	###########################
	# #         Name          #
	###########################
	# print soup.find('title').string
	data_character['name'] = soup.find('title').string

	###########################
	# #      Description      #
	###########################
	for var_name in soup.find_all('meta'):
		if 'description' in var_name.attrs.values():
			# print i.attrs['content']
			data_character['description'] = var_name.attrs['content']

	###########################
	# #         Table         #
	###########################
	# for var_elem in soup.find_all('table'):
	# 	for i in  list(var_elem):


	
	print data_character
character_description("http://awoiaf.westeros.org/index.php/Joffrey_Baratheon")


def get_characters():
	url = "http://awoiaf.westeros.org/index.php/List_of_characters"
	page = requests.get(url).text
	soup = BeautifulSoup(page)

	# #Dictionary with Character Names and their respective URLS
	data_character_names_urls = {}
	for var_name in soup.find_all('li'):
		# print list(var_name)[1]
		try:
			if "/index.php/" in list(var_name)[1]["href"]:
				# print list(var_name)[1]["href"]
				# print list(var_name)[1]["title"]
				# print "\n\n"
				data_character_names_urls[list(var_name)[1]["title"]] = "http://awoiaf.westeros.org" + list(var_name)[1]["href"]
		except Exception as e:
			print e
			print list(var_name)
			print "\n"


	# for key, value in data_character_names_urls.iteritems():
	# 	print "Character Name: " + key
	# 	print "URL: " + value
	# 	print "\n\n"
