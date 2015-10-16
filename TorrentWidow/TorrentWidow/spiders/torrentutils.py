
import json
import sys
from pprint import pprint
from urllib import quote

#/?field=seeders&sorder=desc

def CollectStartUrls():
	kat_search = 'https://kat.cr/usearch/'
	start_urls = []
	
	log = open('spider.log', "a+") 
			#must read the crawling.config 
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
		#add order by ascending 
		surl = kat_search +  quote(torrent['name']) + quote(" ") + quote("category:") + torrent['category']
		start_urls.append(surl)
	
	
	return start_urls