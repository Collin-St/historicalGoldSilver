import scrapy
import calendar
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

            # grab commodity, date, and price from table using xpath
            commodity = response.xpath(
                "//h2[@class='float_lang_base_1 inlineblock']//text()").extract_first().split(' ')[0]
            date = row.xpath('td[1]//text()').extract_first()
            price = row.xpath('td[2]//text()').extract_first()

            # convert abbreviated date into numeric date with calendar
            year = date.split(' ')[2]
            month = list(calendar.month_abbr).index(date.split(' ')[0])
            day = date.split(' ')[1].split(',')[0]
            newDate = '{year}-{month}-{day}'.format(
                year=year, month=month, day=day)

            items['commodity'] = commodity
            items['date'] = newDate
            items['price'] = price

            yield items


# date column xpath = //table[@id='curr_table']//tbody//tr//td[1]
# price column xpath = //table[@id='curr_table']//tbody//tr//td[2]
