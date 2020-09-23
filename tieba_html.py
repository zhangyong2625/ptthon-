"""
view-source:https://tieba.baidu.com/p/6974499436?red_tag=2751345328
1.在浏览器中查看网页源代码
2.使用python读文本文件
3.正则表达式的应用
4.先抓大再抓小的匹配技巧
5.使用Python写CSV文件
"""
import re
import csv

path = r"C:\Users\Administrator\Desktop\source.txt"
with open(path,"r",encoding="utf-8") as f:
    content = f.read()
pattern = 'p_author_name j_user_card(.*?)icon_relative j_user_card'
result = re.findall(pattern, content, re.S)
# print(result)
with open("demo.txt","w",encoding="utf-8") as f:
    for value in result:
        f.write(value+"\n")
        f.write("-----"*30+"\n")
    