import scrapy
from ..items import TrackerItem
class DailyUpdate(scrapy.Spider):
    name = 'track'
    start_urls = [
        'https://api.covid19india.org/'
    ]
    def parse(self, response):

        items = TrackerItem()

        all_div =  response.css(".highlighter-rouge:nth-child(7)::text").extract()

        items['all_div'] = all_div
        yield items

