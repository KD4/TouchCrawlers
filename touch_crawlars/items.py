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

class ACT_MEMBER_REPORT(Item):
	id=Field()
	attendance_rate=Field()
	proposal=Field()

class ACT_BILL_ITEM(Item):
	id=Field()
	link_id=Field()

class ACT_BILL_VOTE(Item):
	bill_id = Field()
	member_id = Field()
	vote_code = Field()