
import scrapy 
import json
import sys
from pprint import pprint

log = open('spider.log', "a+") 

with open('crawling.config') as config: 
	try:
		config = json.load(config)
		#print(config["torrents"][0]["type"]) 
	except ValueError, e:
		log.write("\nError during JSON file parsing: \n")
		log.write(str(e)) 
		sys.exit()

torrents  = config["torrents"]

for torrent in torrents:
	pprint(torrent) 
	print("\n")