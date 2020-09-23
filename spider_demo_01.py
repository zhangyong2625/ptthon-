import requests
import time
from multiprocessing.dummy import Pool

time1 = time.time()
url = r"https://www.baidu.com/"
html_str = requests.get(url).content.decode()
print(html_str)
time2 = time.time()
print("请求一个网页的时间：%.3f秒"%(time2-time1))

# 请求一个网页
def query(url):
    requests.get(url)

# 单线程查询一个网页100次
time_start = time.time()
for i in range(100):
    # print("--->%d"%(i+1))
    query(url)
time_end = time.time()
print("单线程请求一个网页100次的时间：%.3f秒"%(time_end-time_start))

# 多线程查询一个网页100次
time_start = time.time()
url_list = []
for i in range(100):
    url_list.append(url)
pool = Pool(4) # 初始化了一个有4个线程的线程池
pool.map(query,url_list)
time_end = time.time()
print("多线程请求一个网页100次的时间：%.3f秒"%(time_end-time_start))

"""
某一次的运行结果：
请求一个网页的时间：0.054秒
单线程请求一个网页100次的时间：5.070秒
多线程请求一个网页100次的时间：1.473秒

结果分析：
4个线程的运行时间其实比1个线程运行时间的1/4多一点，这多出的一点时间其实是线程切换的时间。从侧边也反映了python的多线程
在微观上还是单行的。

python多线程--->伪多线程（微观上单线程，宏观上多线程）  GIL(Global Interpreter Lock)全局解释器锁
"""