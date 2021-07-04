import scrapy


class NiftyFiftyItem(scrapy.Item):
    symbol = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    oneYearHigh = scrapy.Field()                # 52 week high
    oneYearLow = scrapy.Field()                 # 52 week low
    turnoverValue = scrapy.Field()              # Turnover in crores
    turnoverVolume = scrapy.Field()             # Turnover volume in lacs
    oneYearChange = scrapy.Field()              # Change over the last 1 year
