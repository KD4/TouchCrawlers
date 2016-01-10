# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class ActBillVoteSpider(BaseSpider):

    name = 'actBillVoteSpider'

    def start_requests(self):
        yield Request(urls.bill_index, method='GET')

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        max_page = extract_max_page(hxs,'goToPage')
        print("extracted page is %s" % max_page)
        for i in range(1, int(max_page)+1):
            yield Request(urls.bill_index_per_page % i, callback=self.parse_bill_vote)


    def parse_bill_vote(self, response):
        hxs = HtmlXPathSelector(response)
        ids = extract_ids(hxs, 'mbill')
        for id in ids:
            yield Request(urls.bill_vote % int(id), callback=self.parse_bill_vote_per_member)

    def parse_bill_vote_per_member(slef, response):
        id = extract_url(response.url, 'mbill')
        hxs = HtmlXPathSelector(response)
        agreement_members = extract_agreement_members(hxs,2)
        opposition_members = extract_oppsition_members(hxs,2)
        for member in agreement_members:
            yield items.ACT_BILL_VOTE(bill_id=id, member_id=member, vote_code=1)

        for member in opposition_members:
            yield items.ACT_BILL_VOTE(bill_id=id, member_id=member, vote_code=0)
