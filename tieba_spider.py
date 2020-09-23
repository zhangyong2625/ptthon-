"""
https://tieba.baidu.com/p/6972849748?red_tag=2913427813
1.在浏览器中查看网页源代码
2.使用python读文本文件
3.正则表达式的应用
4.先抓大再抓小的匹配技巧
5.使用Python写CSV文件
"""
import re
import csv

# 将
def list_to_dict(user,content,column):
    count = min(len(user),len(content))
    lst = []
    for i in range(count):
        d = {}
        d[column[0]] = user[i]
        d[column[1]] = content[i]
        lst.append(d)
    return lst

def result(file,column):
    file = r"source.txt"
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    pattern_user = 'username="(.*?)" class='
    pattern_content = '(\S*?)</div><br>'
    user = re.findall(pattern_user, content, re.S)
    content = re.findall(pattern_content, content, re.S)
    return list_to_dict(user,content,column)

def tieba(file,column):
    with open("tieba.csv","w",newline='',encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=column)
        writer.writeheader()
        writer.writerows(result(file,column))

if __name__ == "__main__":
    file = "source.txt"
    column = ['name','content']
    tieba(file,column)