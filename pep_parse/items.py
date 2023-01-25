# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PepParseItem(scrapy.Item):
    header_map = {
        'number': 'Номер',
        'name': 'Название',
        'status': 'Статус',
    }

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
