"""
  @Author : zhangyong2625
  @Email : 1293271923@qq.com

https://tieba.baidu.com/p/6972849748?red_tag=2913427813
1.获取网页源代码
2.正则表达式的应用
3.先抓大再抓小的匹配技巧
4.使用Python写CSV文件
"""
import re
import csv
import requests


def result(content):
    pattern_user = 'username="(.*?)" class='
    user = re.findall(pattern_user, content, re.S)
    print(user)
    return user


def tieba(file):
    with open("tieba.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames="name")
        writer.writeheader()
        writer.writerows(result(file))


if __name__ == "__main__":
    url = r"https://tieba.baidu.com/p/6972849748?red_tag=2913427813"
    source = requests.get(url).content.decode("utf-8")
    tieba(source)