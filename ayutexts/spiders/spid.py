import scrapy
import json

class AyuSpider(scrapy.Spider):
	name="ayutexts"
	url = "http://ayutexts.dharaonline.org/frmread.aspx"

	def start_requests(self):
		yield scrapy.Request(url=self.url, callback=self.parseBooks)

	def parseBooks(self, response):
		selector = scrapy.Selector(response=response)
		VIEWSTATE= selector.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first()
		EVENTVALIDATION = selector.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()
		VIEWSTATEGENERATOR = selector.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
		script = 'ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$ddbook'
		
 	   	formdata={
 	    	 # change pages here
 	    	"__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddbook",
 	    	"__LASTFOCUS":"",
 	    	"__VIEWSTATE": VIEWSTATE,
 	    	"__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
 	    	"__EVENTVALIDATION": EVENTVALIDATION,
 	   		"ctl00$ContentPlaceHolder1$ddbook": "1",
			"__ASYNCPOST": "true"
		}
		header = {'User-Agent': u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
				'Cookie': 'ASP.NET_SessionId=3ikackn3wx5ujb5hc2d4y3cx',
				'X-MicrosoftAjax': 'Delta=true',
				'X-Requested-With': 'XMLHttpRequest'}
		
		yield scrapy.FormRequest(url=self.url, formdata=formdata, headers=header, callback=self.parseSections)

	def parseSections(self, response):

		print('response ', response.text)
		selector = scrapy.Selector(response=response)
		VIEWSTATE= selector.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first()
		EVENTVALIDATION = selector.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()
		VIEWSTATEGENERATOR = selector.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
		script = "ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$ddsection"
		
 	   	formdata={
 	    	 # change pages here
 	    	"ctl00$ContentPlaceHolder1$script": script,
 	    	"ctl00$ContentPlaceHolder1$ddbook": "1",
 	    	"ctl00$ContentPlaceHolder1$ddsection": "1",
 	   		"__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddsection",
 	   		"__EVENTARGUMENT": "",
 	    	"__LASTFOCUS": "",
 	    	"__VIEWSTATE": VIEWSTATE,
 	    	"__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
 	    	"__EVENTVALIDATION": EVENTVALIDATION,
 	   	#"ctl00$ContentPlaceHolder1$ddchapter":'', 
			"__ASYNCPOST": "true&"
		#"ScriptManager.SupportsPartialRendering": "true",
		#"ctl00$ContentPlaceHolder1$btnSearch": "Search"
		}
		
		header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
				'Cookie': 'ASP.NET_SessionId=3ikackn3wx5ujb5hc2d4y3cx',
				'X-MicrosoftAjax': 'Delta=true',
				'X-Requested-With': 'XMLHttpRequest',
				'Referer': 'http://ayutexts.dharaonline.org/frmread.aspx',
				'Origin': 'http://ayutexts.dharaonline.org',
				'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'Connection': 'keep-alive'}

		self.logger.info(self.url)
		yield scrapy.FormRequest(url=self.url, formdata=formdata, headers=header, callback=self.parseChapters)

	def parseChapters(self, response):
		self.logger.info('in parse')
		#selector = scrapy.Selector(response=response)
		#yield selector
		self.logger.info(response.text)

		selector = scrapy.Selector(response=response)
		VIEWSTATE= selector.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first()
		EVENTVALIDATION = selector.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()
		VIEWSTATEGENERATOR = selector.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
		script = 'ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$ddsection'
		
 	   	formdata={
 	    	 # change pages here
 	    	"ctl00$ContentPlaceHolder1$script": script,
 	    	"ctl00$ContentPlaceHolder1$ddbook": "1",
 	    	"ctl00$ContentPlaceHolder1$ddsection": "1",
 	   		"__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddsection",
 	   		"__EVENTARGUMENT": "",
 	    	"__LASTFOCUS":"",
 	    	"__VIEWSTATE": VIEWSTATE,
 	    	"__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
 	    	"__EVENTVALIDATION": EVENTVALIDATION,
 	   	#"ctl00$ContentPlaceHolder1$ddchapter":'', 
			"__ASYNCPOST": "true&",
		#"ScriptManager.SupportsPartialRendering": "true",
		#"ctl00$ContentPlaceHolder1$btnSearch": "Search"
		}

		yield {'data': response.text}
		

spider = AyuSpider(scrapy.Spider("AyuSpider"))
spider.start_requests()

