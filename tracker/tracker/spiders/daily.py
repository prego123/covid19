import scrapy
from ..items import TrackerItem
class DailyUpdate(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    def parse(self, response):

        items = TrackerItem()

        all_div_quotes = response.css("div.quote")
        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css(".tag::text").extract()

            items['title']=title
            items['author']=author
            items['tag']=tag
            yield items
