# historicalGoldSilver

This app fetches historical gold & silver price data from `https://www.investing.com/commodities/gold-historical-data/` and `https://www.investing.com/commodities/silver-historical-data/`, stores the data in MySQL, and outputs the data to `http://localhost:8080` using Flask.

# Run this code

From the terminal, clone this repo:
`git clone https://github.com/Collin-St/historicalGoldSilver.git && cd historicalGoldSilver/historicalGoldSilver/`

Run Scrapy:
`scrapy crawl prices`

Run Flask:
``
