# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

class MemberItem(Item):
	id=Field()
	wiki=Field()
	image=Field()
	birthday=Field()
	address=Field()
	name_en=Field()
	education=Field()
	facebook=Field()
	name=Field()
	gender=Field()
	name_cn=Field()
	homepage=Field()
	twitter=Field()

class ACT_MEMBER_ITEM(Item):
	id=Field()
	name=Field()
	local=Field()