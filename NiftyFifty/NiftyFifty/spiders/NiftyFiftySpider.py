import scrapy
import json
from ..items import NiftyFiftyItem


class NiftyFiftySpider(scrapy.Spider):
    name = 'NiftyFifty'
    # the start url is the request that NSE sends to get a json file
    # that provides the live/current details of all the nifty stocks
    start_urls = [
        'https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json'
    ]

    def parse(self, response):
        items = NiftyFiftyItem()
        raw_data = response.body
        data = json.loads(raw_data)         # loads the raw data that is in json format to data in dictionary
        stocks_details = data['data']       # unwinding the nested dictionary
        for stock_detail in stocks_details:
            items['symbol'] = stock_detail['symbol']
            items['open'] = stock_detail['open']
            items['high'] = stock_detail['high']
            items['low'] = stock_detail['low']
            items['oneYearHigh'] = stock_detail['wkhi']
            items['oneYearLow'] = stock_detail['wklo']
            items['turnoverValue'] = stock_detail['ntP']
            items['turnoverVolume'] = stock_detail['trdVol']
            items['oneYearChange'] = stock_detail['yPC']
            yield items
