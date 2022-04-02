import scrapy

class UVPSpider(scrapy.Spider):
    name = 'quotes'
    def start_requests(self):
#        urls = ['http://quotes.toscrape.com/page/1','http://quotes.toscrape.com/page/2',]
        urls = ['https://www.uvp-verbund.de/freitextsuche?rstart=0&currentSelectorPage=1']
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)
    
    def parse(self,response):
        page = response.url.split("/")[-2]
        filename = 'suburl-%s.html' % page
        filename2 = 'suburl'
        print("###############################################################################################################")
        # x = response.xpath('//*[@id="results"]/div[3]').get()
        # y = x.css('a::attr(href)')[0].get()
        # print(y)
        mainUrl = 'https://www.uvp-verbund.de/'
        subUrl = []
        fullSubUrl = []
        for eachPage in response.css('div.data'):
            yield{
                # 'text' : eachPage.css('span.text::text').get()
            }
            x = eachPage.css('a::attr(href)').getall()
            subUrl.append(x[0])
            # print(x[0])
        for eachUrl in subUrl:
            fullUrl = mainUrl+eachUrl
            fullSubUrl.append(fullUrl)

        print(fullSubUrl)

        with open('your_file.txt', 'w') as f:
            for item in fullSubUrl:
                f.write("%s\n" % item)
                f.write(",")

        print("###############################################################################################################")

class UVPSpider2(scrapy.Spider):
    name = 'subPage'
    def start_requests(self):
#        urls = ['http://quotes.toscrape.com/page/1','http://quotes.toscrape.com/page/2',]
        urls = ['https://www.uvp-verbund.de/freitextsuche?rstart=0&currentSelectorPage=1']
        file1 = open('your_file.txt', 'r')
        links = file1.readlines()
        for url in links:
            yield scrapy.Request(url=url, callback = self.parse)
    
    def parse(self,response):
        page = response.url.split("/")[-2]
        filename = 'suburl-%s.html' % page
        filename2 = 'suburl'
        with open("myfile.txt", "wb") as fp:
            fp.write(response.body)
        print("###############################################################################################################")
        print(response.body)
        
         