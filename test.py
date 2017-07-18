import urllib.parse
import os

path_dir_this = os.path.abspath(os.path.dirname(__file__))
print(path_dir_this)

url = 'https://docs.python.jp/3/license.html#sockets'
url = 'https://docs.python.jp/3/howto/index.html'
path = urllib.parse.urlparse(url).path
# os.path.joinするとき引数に絶対パスがあるとそのパスは無視されてしまう。`/...`のように先頭にスラッシュがあると絶対パスとみなされ無視される
# http://qiita.com/FGtatsuro/items/1ab9ebf6505bef1834f8
# ふつう、こういう細かいパス文字列の違いをうまいことやってくれるからパスAPIを使うと思うのだが…。Pythonは使いづらいAPIが多い。とくにパス関係。
if '/' == path[0]:
    path = path[1:]
fragment = urllib.parse.urlparse(url).fragment
print(path)
print(fragment)
print(os.path.dirname(path))
print(os.path.join(path_dir_this, path)) # /tmp, 3/howto/index.html
print(os.path.join('/a', 'b'))


