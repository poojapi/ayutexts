import scrapy


class Spider:
	def request(self):
		selector = scrapy.Selector(response=response)
		VIEWSTATE= selector.xpath('//@[id="__VIEWSTATE"]/@value').extract_first()
		EVENTVALIDATION = selector.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first()
		VIEWSTATEGENERATOR = selector.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
		script = 'ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$btnSearch'
		print(VIEWSTATE)

		return scrapy.FormRequest.from_response(response,
		url = 'http://ayutexts.dharaonline.org/frmread.aspx',
		formdata = ("__EVENTARGUMENT": "",
 	    	"__VIEWSTATE": VIEWSTATE,
 	    	"__EVENTVALIDATION": EVENTVALIDATION,
 	   	"ctl00$ContentPlaceHolder1$script": script,
		"ctl00$ContentPlaceHolder1$ddbook": 1,
		"ctl00$ContentPlaceHolder1$ddsection": 1,
		"ctl00$ContentPlaceHolder1$ddchapter":'', 
		"__ASYNCPOST": "true",
		"ctl00$ContentPlaceHolder1$btnSearch": "Search"),
		callback=self.callback)	


s = Spider()
s.request()
