import scrapy
from ..items import HistoricalgoldsilverItem


class PricesSpider(scrapy.Spider):
    name = "prices"

    def start_requests(self):
        urls = [
            'https://www.investing.com/commodities/gold-historical-data/',
            'https://www.investing.com/commodities/silver-historical-data/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        items = HistoricalgoldsilverItem()

        for row in response.xpath("//table[@id='curr_table']//tbody//tr"):

            metal = response.xpath(
                "//h2[@class='float_lang_base_1 inlineblock']//text()").extract_first()
            date = row.xpath('td[1]//text()').extract_first()
            price = row.xpath('td[2]//text()').extract_first()
            mean = '1'
            variance = '1'

            items['metal'] = metal
            items['date'] = date
            items['price'] = price
            items['mean'] = mean
            items['variance'] = variance

            yield items


# date column xpath = //table[@id='curr_table']//tbody//tr//td[1]
# price column xpath = //table[@id='curr_table']//tbody//tr//td[2]
