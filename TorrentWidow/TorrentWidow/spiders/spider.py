
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
import torrentutils	


class TorrentWidow(CrawlSpider):
	name = 'spider'
	allowed_domains = ['kat.cr']
	start_urls = torrentutils.CollectStartUrls() 
	

	  
	def parse(self, response, log):
		s = Selector(response)
		item = TorrentItem()
		#.odd to be sure its the first one
		item['title'] = s.css(".markeredBlock .torType .filmType").extract()[0]
		item['url'] =  s.css(".cellMainLink").extract()[0]
		item['magnet'] =  s.css("a[title='Torrent magnet link']").extract()[0]
		
		
	
	

		  #  custom_settings = {
   #         'BOT_NAME': 'torrentwidow',
    #        'DEPTH_LIMIT': 7,
     #       'DOWNLOAD_DELAY': 3
      #  }
	  
		
		

