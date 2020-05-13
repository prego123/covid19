import scrapy
from ..items import TrackerItem
class DailyUpdate(scrapy.Spider):
    name = 'track'
    start_urls = [
        'https://api.covid19india.org/csv/'
    ]
    def parse(self, response):

        items = TrackerItem()

        all_div =  response.css("tr:nth-child(1) td:nth-child(3)::text").extract()

        items['all_div'] = all_div
        yield items

