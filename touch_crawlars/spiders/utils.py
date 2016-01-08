import re
import itertools
import lxml.html

__all__ = ["extract_ids", "extract_texts","extract_ids_for_popong"]

def extract_ids_for_popong(hxs, key):
    xpath = '//a[contains(@href, "/%s/")]/@href' % key
    return hxs.select(xpath).re(r'/%s/(\d+)' % key)

def extract_ids(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/@href' % key
    return hxs.select(xpath).re(r'%s=(\d+)' % key)

def extract_texts(hxs, key):
    xpath = '//a[contains(@href, "%s=")]/text()' % key
    return hxs.select(xpath).extract()
