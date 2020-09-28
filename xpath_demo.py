"""
xpath使用例子 
"""

from lxml import etree

source = """
<?xml version="1.0" encoding="UTF-8"?>
 
<bookstore>
 
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
 
<book>
  <title lang="cn">Learning XML</title>
  <price>39.95</price>
</book>
 
</bookstore>
"""

# 将HTML解析成为对象
obj = etree.HTML(source)
# 使用xpath方法获取标签的属性
content1 = obj.xpath('//book/title/@lang')
print(content1)
# 使用xpath方法获取标签的内容
content2 = obj.xpath('//book/title[@lang="eng"]/text()')
content3 = obj.xpath('//book/price/text()')
print(content2)
print(content3)

