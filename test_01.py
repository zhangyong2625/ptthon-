import requests

import lxml.html

url = r"https://www.kanunu8.com/files/writer/130.html"
source = requests.get(url).content.decode("gbk")
selector = lxml.html.fromstring(source)
content = selector.xpath('/html/body/div[1]/table[9]')[0]
for each in content:
    print(each)


