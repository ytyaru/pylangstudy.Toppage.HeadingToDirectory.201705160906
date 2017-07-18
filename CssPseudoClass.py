#!python3
#encoding: utf-8
import requests
from bs4 import BeautifulSoup
import os.path
"""
BeautifulSoupでは擬似クラスはnth-of-typeしか実装されていないらしい。
NotImplementedError: Only the following pseudo-classes are implemented: nth-of-type.
ここではその代わりとなる関数を実装する。
"""
class CssPseudoClass(object):
    def __init__(self):
        pass
    """
    parentがchildを持っているか。
    @param {HtmlElement} parentは対象のHTML要素
    @param {str} childはparentが持つchildの要素名
    @return {boolean} 所持の是非
    """
    def Has(self, parent, child):
        for c in parent.children:
            if child == c.name:
                return True
        return False
