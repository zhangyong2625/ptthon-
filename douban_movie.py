"""
  @Author : zhangyong2625
  @Email : 1293271923@qq.com
"""

import requests
import csv
from lxml.html import etree
import re


# 获取url请求内容
def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    content = requests.get(url, headers=headers).content.decode("utf-8")
    return content


# 利用xpath提取网页内容
def get_result(result):
    # 将HTML解析成为对象
    obj = etree.HTML(result)
    # 获取电影名
    list_title = obj.xpath('//div[@class="hd"]/a/span[@class="title"]/text()')
    # 获取电影的导演、主演信息
    list_con = obj.xpath('//div[@class="info"]/div[@class="bd"]/p/text()')
    # 获取下一页的url
    next_url = obj.xpath('//span[@class="next"]/a/@href')
    return list_title, list_con, next_url


# 将结果写入csv文件中
def write_csv(list_movie, list_author):
    with open("movie.csv", "w", newline='', encoding="utf-8") as f:  # 加入参数newline='' ：避免出现空行
        # fieldnames定义列名
        writer = csv.DictWriter(f, fieldnames=['top', 'movie', 'author'])
        list_result = []
        for i in range(len(list_movie)):
            d = {'top': i + 1, 'movie': list_movie[i], 'author': list_author[i]}
            list_result.append(d)
        writer.writeheader()
        writer.writerows(list_result)


# 处理导演信息
def get_author(con):
    pattern = '[ \n]'
    for i in range(len(con)):
        con[i] = re.sub(pattern, "", con[i])
    new_con = [x for x in con if x != ""]
    return new_con[::2]


# 无效电影名去除
def get_name(movie):
    list_movie = []
    for value in movie:
        if "\xa0" not in value:
            list_movie.append(value)
    return list_movie


# 爬虫主方法
def main():
    url = r"https://movie.douban.com/top250"
    movie = []
    author = []
    new_url = url
    while new_url:
        content = get_url(new_url)
        pre_movie, pre_author, pre_url = get_result(content)
        movie.extend(get_name(pre_movie))
        author.extend(get_author(pre_author))
        if not pre_url:
            break
        new_url = url + pre_url[0]
    # print(movie, len(movie))
    # print(author, len(author))
    write_csv(movie, author)


if __name__ == "__main__":
    main()
