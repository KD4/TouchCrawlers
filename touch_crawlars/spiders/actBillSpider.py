# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class ActBillSpider(BaseSpider):

    name = 'actBillSpider'

    def start_requests(self):
        yield Request(urls.bill_index, method='GET')

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        max_page = extract_max_page(hxs,'goToPage')
        print("extracted page is %s" % max_page)
        for i in range(1, int(max_page)+1):
            yield Request(urls.bill_index_per_page % i, callback=self.parse_bill)


    def parse_bill(self, response):
        hxs = HtmlXPathSelector(response)
        ids = extract_ids(hxs, 'mbill')
        for id in ids:
            yield Request(urls.bill_vote % int(id), callback=self.parse_bill_detail)

    def parse_bill_detail(self, response):
        id = extract_url(response.url, 'mbill')
        hxs = HtmlXPathSelector(response)
        link_id = extract_word_id(hxs,'bill_id')
        yield items.ACT_BILL_ITEM(id=id,link_id=link_id)