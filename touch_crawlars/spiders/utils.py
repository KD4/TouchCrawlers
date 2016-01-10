import re
import itertools
import lxml.html
__all__ = ["convert_to_text","extract","extract_integer","extract_text","extract_url","extract_ids", "extract_texts","extract_ids_for_popong","extract_max_page","extract_agreement_members","extract_oppsition_members","extract_word_id"]

def convert_to_text(e):
    texts = []
    texts.append(e.text.strip())
    for br in e:
        assert br.tag == 'br'
        texts.append('\n')
        if e.tail: texts.append(e.tail.strip())
    return ''.join(texts)

def extract(hxs, xpath):
    result = hxs.select(xpath).extract()
    if not result: return ''
    return result[0]

def extract_integer(hxs, xpath):
    result = hxs.select(xpath).re(r'(?:\d*\.)?\d+')
    if not result: return ''
    return result[0]
    
def extract_agreement_members(hxs, idx):
	xpath = '//td/table/tr[%d]/td[2]/a[contains(@href,"member_seq=")]/@href' % idx
	results = hxs.select(xpath).re(r'member_seq=(\d+)')
	return results

def extract_oppsition_members(hxs, idx):
	xpath = '//td/table/tr[position()>%d]/td[2]/a[contains(@href,"member_seq=")]/@href' % idx
	results = hxs.select(xpath).re(r'member_seq=(\d+)')
	return results

def extract_text(hxs, xpath):
    result = hxs.select(xpath).extract()
    if not result: return ''
    return convert_to_text(lxml.html.fromstring(result[0]))

def extract_ids_for_popong(hxs, key):
    xpath = '//a[contains(@href, "/%s/")]/@href' % key
    return hxs.select(xpath).re(r'/%s/(\d+)' % key)

def extract_ids(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/@href' % key
    return hxs.select(xpath).re(r'%s=(\d+)' % key)

def extract_word_id(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/@href' % key
    return hxs.select(xpath).re(r'%s=(\w+)' % key)

def extract_texts(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/text()' % key
    return hxs.select(xpath).extract()

def extract_url(url, key):
    return re.search(r'%s=(\d+)' % key, url).group(1)

def extract_max_page(hxs, key):
	xpath = '//a[contains(@href, "%s")]/@href' % key
	result = hxs.select(xpath).re(r'%s\((\d+)' % key)
	if not result: return ''
	return result[-1]
	

