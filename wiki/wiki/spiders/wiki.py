import scrapy

class PaintersSpider(scrapy.Spider):
    name = 'painters'
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    start_urls = [f'https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22{i}%22' for i in letters]


    def parse(self, response):
        for painter in response.css('div.div-col li'):
            yield {
                'painter': painter.get()
            }
