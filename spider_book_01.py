"""
  @Author : zhangyong2625
  @Email : 1293271923@qq.com
"""

"""
https://www.kanunu8.com/book3/6879
通过多线程爬取每一章的内容
1.使用requests获取网页源代码
2.使用正则表达式获取内容
3.文件操作
"""
import re
import time
import requests
from lxml.html import etree
from multiprocessing import Pool

url = r"https://www.kanunu8.com/book3/6879"


def get_html(url):
    # 获取url网页内容
    content = requests.get(url).content.decode("gbk")
    return content


def write_content(list_result):
    # 爬取章节内容 并写入文件
    print(url+"/"+list_result[0])
    result = get_html(url+r"/"+list_result[0])
    obj = etree.HTML(result)
    content = obj.xpath('//p/text()')
    content_new = "".join(content)
    pattern = '[\n\r]'
    content_new.replace(pattern, "")
    with open(list_result[1]+".txt", "w", encoding="utf-8") as f:
        f.write(content_new)


def get_content():
    # 爬取主页内容
    str_html = get_html(url)
    # 将HTML解析成为对象
    obj = etree.HTML(str_html)
    list_file = obj.xpath('//tr[@bgcolor="#ffffff"]/td/a/text()')
    list_html = obj.xpath('//tr[@bgcolor="#ffffff"]/td/a/@href')
    list_result = []
    for i in range(len(list_html)):
        list_result.append((list_html[i],list_file[i]))
    return list_result


if __name__ == "__main__":
    # 利用多线程去爬取章节内容
    time_start = time.time()
    pool = Pool(3)
    pool.map(write_content, get_content())
    time_end = time.time()
    print("多线程爬虫运行时间：%s" % (time_end - time_start))