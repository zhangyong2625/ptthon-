"""
https://book.qidian.com/info/1018027842#Catalog
通过多线程爬取每一章的内容
1.使用requests获取网页源代码
2.使用正则表达式获取内容
3.文件操作
"""
import re
import time
import requests
from multiprocessing import Pool

url = r"https://book.qidian.com/info/1018027842#Catalog"

def get_html(url):
    # 获取url网页内容
    return requests.get(url).content.decode()


def write_content(list_result):
    # 爬取章节内容 并写入文件
    result = get_html("http:"+list_result[0])
    pattern = '<div class="read-content j_readContent">(.*?)<div class="admire-wrap">'
    content = re.search(pattern, result, re.S).group()
    content_new = re.sub(r'["<br />"\r\t\f"p"]', '', content)
    with open(list_result[1]+".txt", "w", encoding="utf-8") as f:
        f.write(content_new)


def get_content():
    # 爬取主页内容，返回一个(章节名,html后缀)的列表集合(采用先抓大再抓小的策略来匹配)
    str_html = get_html(url)
    pattern = '分卷阅读(.*?)30天内更新30万字以上'
    s1 = re.search(pattern, str_html, re.S).group() # 匹配到章节名和对应html后缀的段落
    # print(s1)
    pattern_html = '<li data-rid="[0-9]{1,3}"><a href="(.*?)" target="_blank" data-eid="qd_G55"'
    pattern_file = '章节字数：[0-9]{4}">(.*?)</a>'
    list_html = re.findall(pattern_html, s1, re.S) # 匹配章节名保存到列表中
    list_file = re.findall(pattern_file, s1, re.S) # 匹配html后缀保存到列表中
    list_result = []
    for i in range(len(list_file)):
        list_result.append((list_html[i],list_file[i]))
    print(list_result)
    return list_result


if __name__ == "__main__":
    # 利用多线程去爬取章节内容
    time_start = time.time()
    pool = Pool(3)
    pool.map(write_content, get_content())
    time_end = time.time()
    print("多线程爬虫运行时间：%s"%(time_end - time_start))


