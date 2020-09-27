"""
  @Author : zhangyong2625
  @Email : 1293271923@qq.com
"""

import requests
import csv
from lxml.html import etree


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
    # 获取电影title
    list_title = obj.xpath('//div/a/span[@class="title"]/text()')
    # 获取电影的作者，年份等信息
    list_con = obj.xpath('//div[@class="bd"]/p/text()')
    # 获取下一页的url
    next_url = obj.xpath('//span[@class="next"]/a/@href')
    return list_title, list_con, next_url


# 将结果写入csv文件中
def write_csv(list_movie, list_author):
    with open("movie.csv", "w", newline='', encoding="utf-8") as f:  # 加入参数newline='' ：避免出现空行
        # fieldnames定义列名
        writer = csv.DictWriter(f, fieldnames=['top', 'moive', 'author'])
        list_result = []
        for i in range(len(list_movie)):
            d = {'top': i + 1, 'movie': list_movie[i], 'author': list_author[i]}
            list_result.append(d)
        writer.writeheader()
        writer.writerows(list_result)


# 处理作者和年份信息
def get_author_year(con):
    author = []
    year = []
    for value in con:
        author.append(value.split("/")[0])
        year.append(value.split("/")[-1])
    return author, year

if __name__ == "__main__":
    url = r"https://movie.douban.com/top250"
    # 存储电影名
    movie = []
    # 存储作者信息
    author = []
    new_url = url
    while new_url:
        print(new_url)
        result = get_url(new_url)
        list_name, con, pre_url = get_result(result)
        print(pre_url)
        movie.extend(list_name)
        author.extend(con)
        if not pre_url:
            break
        new_url = url + pre_url[0]
    print(movie)
    print(author)
    write_csv(movie, author)
