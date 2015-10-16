
import scrapy 
import json
import sys
from pprint import pprint
from urllib import quote
log = open('spider.log', "a+") 

with open('../crawling.config') as config: 
	try:
		config = json.load(config)
		#print(config["torrents"][0]["type"]) 
	except ValueError, e:
		log.write("\nError during JSON file parsing: \n")
		log.write(str(e)) 
		sys.exit()
kat_search = 'https://kat.cr/usearch/'
start_urls = []
torrents  = config["torrents"]

for torrent in torrents:
	surl = kat_search +  quote(torrent['name']) + quote(" ") + quote("category:") + torrent['category']
	start_urls.append(surl)
	
	
	
