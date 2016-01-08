# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class ActMemberSpider(BaseSpider):

    name = 'actMemberSpider'

    def start_requests(self):
        yield Request(urls.member_index, method='POST')
        

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        ids = extract_ids(hxs, 'member_seq')
        names = extract_texts(hxs, 'member_seq')
        for id, name in zip(ids, names):
            tempText = name.encode('utf-8').split('(')
            realName = tempText[0].strip()
            local = tempText[1][:-1]
            yield items.ACT_MEMBER_ITEM(id=id, name=realName, local=local)