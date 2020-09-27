"""
  @Author : zhangyong2625
  @Email : 1293271923@qq.com
"""

import requests
import csv
from lxml.html import etree


# 获取url请求内容
def get_url(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    content = requests.get(url, headers=header).content.decode("utf-8")
    return content


# 利用xpath提取网页内容
def get_result(result):
    # 将HTML解析成为对象
    obj = etree.HTML(result)
    # 获取书籍title
    list_title = obj.xpath('//table/tr/td[@valign="top"]/div/a/@title')
    # 获取书籍的作者，价格等信息
    list_con = obj.xpath('//table/tr/td/p[@class="pl"]/text()')
    # 获取下一页的url
    next_url = obj.xpath('//span[@class="next"]/a/@href')
    return list_title, list_con, next_url


# 将结果写入csv文件中
def write_csv(list_book, list_author, list_price):
    with open("book.csv", "w", newline='', encoding="utf-8") as f:  # 加入参数newline='' ：避免出现空行
        # fieldnames定义列名
        writer = csv.DictWriter(f, fieldnames=['top', 'book', 'author', 'price'])
        list_result = []
        for i in range(len(list_book)):
            d = {'top': i + 1, 'book': list_book[i], 'author': list_author[i], 'price': list_price[i]}
            list_result.append(d)
        writer.writeheader()
        writer.writerows(list_result)


# 处理作者和价格信息
def get_author_price(con):
    author = []
    price = []
    for value in con:
        author.append(value.split("/")[0])
        price.append(value.split("/")[-1])
    return author, price

if __name__ == "__main__":
    url = r"https://book.douban.com/top250"
    # 存储书籍名
    book = []
    # 存储作者信息
    author = []
    # 存储价格信息
    price = []
    while url:
        print(url)
        result = get_url(url)
        list_name, con, url = get_result(result)
        pre_author, pre_price = get_author_price(con)
        book.extend(list_name)
        author.extend(pre_author)
        price.extend(pre_price)
        if not url:
            break
        url = url[0]
    # print(book)
    # print(author)
    # print(price)
    write_csv(book, author, price)
