
"""

Torrent Widow 


TorrentWidow is a torrent spider that searches torrent websites and collects the most current magnet links and metadata into 
a json file. 

This implementation searches through kat.cr and collects the latest torrents for the day in specified sections. 
You can mark to look at different times and etc. 


Enter the shows you want to watch into the config file. The spider will then compare the config file and the collected json file. 
The spider will then start downloading the magnet links in it's collected json file that are specified by the json file. 


There are three json files at the end. The crawling.config file that sets up the options for the spider's magnet collection, and how to update/clear the next json file. The 
spiderweb.json which lists the magnet links caught in the specification, you can direct options to clear its contents or etc through crawling.config. And then there is the venom.json 
which is created by the user to select the torrents wanted. 

Venom.json and Spiderweb.json are where the torrents selected using different options.  



Files to have: 

TorrentWidow.py
Crawling.config
Spiderweb.json
Venom.json
SpiderThread.py - this will organize and download the selected files in the system 
crontab/windows instructions

"""


__author__ = "Kyle Calica"

import scrapy 
import json
import pprint
from torrent import Torrent

class TorrentSpider(scrapy.Spider):
	name = "TorrentSpider"
	start_urls = ["https://www.kat.cr"]

	def parse(self, resp):
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

				
		#add magnet links to the spiderweb.json 
		return

