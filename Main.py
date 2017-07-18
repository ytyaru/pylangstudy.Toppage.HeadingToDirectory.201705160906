#!python3
#encoding: utf-8
import requests
from bs4 import BeautifulSoup
import os
import os.path
import urllib.parse
import CssPseudoClass
"""
https://docs.python.jp/3/contents.htmlから見出しの木構造を取り出してディレクトリ構造にする。
* `/whatsnews/3.6.hmlt`の`3.6`もディレクトリにする
    * 葉ノードでない場合で.htmlファイルにリンクがある場合、そのファイル名をディレクトリにする。
        * index.htmlは対象外
    * リンクが見出し(`https://docs.python.jp/3/whatsnew/3.6.html#pep-498-formatted-string-literals`)`#pep-498-formatted-string-literals`の場合、それをディレクトリにする
        * その見出しディレクトリの配下に、1つ以上の課題が入る
            * 課題で生じた疑問についてはどんな構造にするか
                * `/見出し/課題/question_index.html`, `/見出し/課題/疑問1/index.html`
                * `/見出し/.questions/疑問1.html`
"""
class Main(object):
    def __init__(self):
        self.__base_dir = os.path.abspath(os.path.dirname(__file__))
    
    def Run(self):
        self.__MakeDirectories(self.__HttpGetPyDocToC())
    
#    def GetLeafNodePyDocToC(self):
#        return self.__GetLeafNoeds(self.__HttpGetPyDocToC())
    
    def __HttpGetPyDocToC(self):
        if not os.path.isfile(self.__GetHtmlFilePath()):
            url = 'https://docs.python.jp/3/contents.html'
            r = requests.get(url)
            r.raise_for_status()
            print(r.encoding) # ISO-8859-1
            r.encoding = r.apparent_encoding # http://qiita.com/nittyan/items/d3f49a7699296a58605b
            print(r.encoding) # utf-8
            with open(self.__GetHtmlFilePath(), 'w', encoding='utf-8') as f:
                f.write(r.text)
        with open(self.__GetHtmlFilePath()) as f:
            return BeautifulSoup(f.read(), 'lxml') # html.parser, lxml
            
    def __GetHtmlFilePath(self):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), 'PyDoc.Contents.html')
            
    def __MakeDirectories(self, soup):
        tree = soup.find('div', class_='toctree-wrapper compound') # 2個目に取得できるものは空だから1個目を取る
        selector = CssPseudoClass.CssPseudoClass()
        for li in tree.find_all('li'):
            dir_path = os.path.join(self.__base_dir, self.__GetRelativePath(li))
            if not os.path.isdir(dir_path):
                print(dir_path)
                os.makedirs(dir_path)

    def __GetRelativePath(self, li):
        path = urllib.parse.urlparse(li.a.get('href')).path
        fragment = urllib.parse.urlparse(li.a.get('href')).fragment
        # 相対パスにする(先頭のスラッシュを削除する)
        # https://docs.python.jp/3/の`3/`がHTML上にはない。`2/`,`4/`などでも同じ構成のHTMLにするためと思われる。ここでは`3/`に対して行うため付与する
        if '/' == path[0]:
            path = path[1:]
        path = os.path.join('3', path)
        print(path)
        if fragment:
            path = path.replace('.html', '/' + fragment)
        elif path.endswith('index.html'):
            path = os.path.dirname(path)
        elif path.endswith('.html'):
            path = path.replace('.html', '')
        return path


if __name__ == '__main__':
    m = Main()
    m.Run()

