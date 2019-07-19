from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
#访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)
time.sleep(1)
#访问新闻页面
second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)
time.sleep(1)

#返回（后退）到百度首页
print("back to %s "%(first_url))
driver.back()
time.sleep(1)

#前进到新闻页
print("forward to %s"%(second_url))
driver.forward()
time.sleep(1)
