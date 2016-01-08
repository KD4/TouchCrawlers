# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
import json
from .. import items
from . import urls
from . import xpaths
from .utils import *

class MemberSpider(BaseSpider):

    name = 'memberSpider'

    def start_requests(self):
        yield Request(urls.popong_person, method='GET')
        

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        ids = extract_ids(hxs, 'person')
        for id in ids:
            yield Request(urls.popong_api_person % id, callback=self.parse_member_info)


    def parse_member_info(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        yield items.MemberItem(
                id=jsonresponse["id"],
                wiki=jsonresponse["wiki"],
                image=jsonresponse['image'],
                birthday=jsonresponse['birthday'],
                facebook=jsonresponse['facebook'],
                address=jsonresponse['address'],
                name_en=jsonresponse['name_en'],
                education=jsonresponse['education'],
                name=jsonresponse['name'],
                gender=jsonresponse['gender'],
                name_cn=jsonresponse['name_cn'],
                homepage=jsonresponse['homepage'],
                twitter=jsonresponse['twitter']
            )