import scrapy

class AyuSpider(scrapy.Spider):
	name="ayutexts"
	url = 'http://ayutexts.dharaonline.org/frmread.aspx'

	def start_requests(self):
		yield scrapy.Request(url=self.url, callback=self.parseForm)

	def parseForm(self, response):
		self.logger.info('in parseForm')
		selector = scrapy.Selector(response=response)
		VIEWSTATE= selector.xpath('//@[id="__VIEWSTATE"]/@value').extract_first()
		EVENTVALIDATION = selector.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()
		VIEWSTATEGENERATOR = selector.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
		script = 'ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$btnSearch'
		self.logger.info(VIEWSTATE)

 	   	# It's fine to use this method from page 1 to page 5
		formdata={
 	    	 # change pages here
 	    	#"__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddbook",
 	    	"__EVENTARGUMENT": "",
 	    	"__VIEWSTATE": VIEWSTATE,
 	    	"__EVENTVALIDATION": EVENTVALIDATION,
 	   	"ctl00$ContentPlaceHolder1$script": script,
		"ctl00$ContentPlaceHolder1$ddbook": 1,
		"ctl00$ContentPlaceHolder1$ddsection": 1,
		"ctl00$ContentPlaceHolder1$ddchapter":'', 
		"__ASYNCPOST": "true",
		"ctl00$ContentPlaceHolder1$btnSearch": "Search"
		}
		#yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.parse_0_5)

 	   # After page 5, you should try this
 	   # get page 6
		formdata["__EVENTTARGET"] = "ctl00$ContentPlaceHolder1$dgFullText$ctl14$ctl01"
		#formdata["ctl00$ContentPlaceHolder1$script"] = "ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$dgFullText$ctl14$ctl01"
		yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.parse)

	def parse(self, response):
  	  # use a metadata to control when to break
		#currPage = response.meta["PAGE"]
		#if (currPage == 15):
		#	return

	  	  # extract names here
		self.logger.info('in parse')
		selector = scrapy.Selector(response=response)
		names = selector.xpath('//*[@id="ctl00_ContentPlaceHolder1_updatepanelread"]').extract()
		self.logger.info(names)
		self.logger.error(names)
		yield names
	 #  	  # parse VIEWSTATE and EVENTVALIDATION again, 
	 #  	  # which contain current page
		# VIEWSTATE = selector.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first()
		# EVENTVALIDATION = selector.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()

	 #  	  # get next page
		# formdata = {
	 #  	    # 06 is the next 1 page, 07 is the next 2 page, ...
		# 	"__EVENTTARGET": "ctl00$ContentPlaceHolder1$RepeaterPaging$ctl06$Pagingbtn",
		# 	"__EVENTARGUMENT": "",
		# 	"__VIEWSTATE": VIEWSTATE,
		# 	"__EVENTVALIDATION": EVENTVALIDATION,
		# 	}
		# yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.parse, meta={"PAGE": currPage+1})

	def parse_0_5(self, response):
		selector = scrapy.Selector(response=response)
  		  # only extract name
		names = selector.xpath('/html/body/form/div[3]/table/tbody/tr/td/div/div/div[2]/table/tbody/tr/td/table/tbody').extract()
		print(names)
		self.logger.error(names)

