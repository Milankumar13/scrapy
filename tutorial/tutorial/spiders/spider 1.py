import scrapy
import os
class UVPSpider(scrapy.Spider):
    name = 'UVP'
    def start_requests(self):
        urls = ['https://www.uvp-verbund.de/freitextsuche?rstart=0&currentSelectorPage=1']
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)
    
    def parse(self,response):
        mainUrl = 'https://www.uvp-verbund.de/'
        subUrl = []
        fullSubUrl = []
        for eachPage in response.css('div.data'):
            x = eachPage.css('a::attr(href)').getall()
            subUrl.append(x[0])
        for eachUrl in subUrl:
            fullUrl = mainUrl+eachUrl
            fullSubUrl.append(fullUrl)

        print(fullSubUrl)

        with open('ListOfSubUrl.txt', 'w') as f:
            for item in fullSubUrl:
                f.write("%s\n" % item)

class UVPSubExtraction(scrapy.Spider):
    name = 'subPage'
    def start_requests(self):
        # urls = ['https://www.uvp-verbund.de/freitextsuche?rstart=0&currentSelectorPage=1']
        subUrlFile = open('ListOfSubUrl.txt', 'r')
        links = subUrlFile.readlines()
        for url in links:
            yield scrapy.Request(url=url, callback = self.parse, meta={'filepath': url})
    
    def parse(self,response):
        ### Sub Task 1 ###
        filename = 'HTML File.txt'
        path = 'subPage1'
        if (os.path.isdir(path) == False):
            os.mkdir(path)
        
        with open(path+"/"+filename, "wb") as fp:
            fp.write(response.body)
        
        ### SUb Task 2 ###
        metaDir = "Meta Information"
        metaDir = path+"/"+metaDir
        if (os.path.isdir(metaDir) == False):
            os.mkdir(metaDir)

        with open(metaDir+"/title", "w") as fp:
            for eachDiv in response.css('div.page-wrapper'):
                title = eachDiv.css('h1::text').get()
                fp.write(title)

        with open(metaDir+"/date", "w") as fp:
            for eachDiv in response.css('div.page-wrapper'):
                date = eachDiv.css('span::text').getall()
                fullDate = date[2]
                onlyDate = fullDate[-10:]
                fp.write(onlyDate)

        ### SUb Task 3 ###
        descDir = "Description File"
        descDir = path+"/"+descDir
        file_url = response.css('a::attr(href)').getall()
        print("###############################################################")
        print(file_url)
        print("###############################################################")

        # for eachBtn in response.css('div.ic-ic-download'):
        #             x = eachBtn.css('a::attr(href)').get()
        #             print("###############################################################")
        #             print(x)
        #             print("###############################################################")
        # if (os.path.isdir(descDir) == False):
        #     os.mkdir(descDir)


        





         