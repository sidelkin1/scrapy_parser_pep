import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        yield from response.follow_all(
            css='section[id=numerical-index] tbody td:nth-of-type(2) a',
            callback=self.parse_pep
        )

    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').re(r'PEP ([\d]+)'),
            'name': response.css('h1.page-title::text').re(r'– (.*)'),
            'status': response.css('dt:contains("Status") '
                                   '+ dd abbr::text').get(),
        }
        yield PepParseItem(data)
