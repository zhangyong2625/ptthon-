import requests

import lxml.html

url = r"https://www.kanunu8.com/book3/6879/"
source = requests.get(url).content.decode("gbk")
print(source)
selector = lxml.html.fromstring(source)
content = selector.xpath('/html/body/div[1]/table[9]/tbody/tr[4]/td/table[1]/tbody/tr[2]/td/text()')
print("--"*50)
print(content)
for each in content:
    print(each)


