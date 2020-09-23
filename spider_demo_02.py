"""
https://www.kanunu8.com/book3/6879/
通过多线程爬取每一章的内容
1.使用requests获取网页源代码
2.使用正则表达式获取内容
3.文件操作
"""
import re
from multiprocessing import Pool

# 爬取章节内容 并写文件
def write_content(d):
    return

# get a dict(key:value-->file_name:html)
def get_content(url):
    return

#利用多线程去爬取章节内容
if __name__ == "__main__":
    url = r"https://www.kanunu8.com/book3/6879/"
    pool = Pool(3)
    pool.map(write_content,get_content(url))
