# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json 
from urllib import quote
from blackwidow.items import BlackwidowItem


class KatSpider(scrapy.spiders.CrawlSpider):
		name = "kat"
		allowed_domains = ['kat.cr']
	
		def CollectStartUrls():
			kat_search = 'https://kat.cr/usearch/'
			start_urls = []
			
			log = open('spider.log', "a+") 
					#must read the crawling.config 
			with open('C:\Users\kacalica\Desktop\TorrentWidow\TorrentWidow\TorrentWidow\crawling.config') as config: 
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
		
		
		start_urls = CollectStartUrls() 
		
		
		  
		def parse(self, response):
			s = Selector(response)
			item = BlackwidowItem()
			item['title'] =  s.css(".cellMainLink").xpath('@href').extract()[0]
			item['magnet'] =  s.css("a[title='Torrent magnet link']").xpath('@href').extract()[0]
			item['url'] = response.request.url
			#log = open('spider.log', "a+") 
			#log.write("title:	\t"+ str(item['title']) +"\n")
			#log.write("url:	\t"+ response.request.url +"\n")
			#log.write("magnet:	\t" + str(item['magnet']) +"\n")
			yield item
		
	