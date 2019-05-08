import scrapy


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
        for row in response.xpath("//table[@id='curr_table']//tbody//tr"):
            yield {
                'date': row.xpath('td[1]//text()').extract_first(),
                'price': row.xpath('td[2]//text()').extract_first()
            }

            # page = response.url.split('/')[-2]
            # filename = 'prices-%s.html' % page
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            # self.log('Saved file %s' % filename)

# date column xpath = //table[@id='curr_table']//tbody//tr//td[1]
# price column xpath = //table[@id='curr_table']//tbody//tr//td[2]
