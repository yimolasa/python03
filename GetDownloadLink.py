from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json
reqheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}


# M1
# url = 'http://www.zhaifu.tv/dongman/3694.html'

# html = requests.get(url).text
# #print(html)
# bs = BeautifulSoup(html, 'lxml')
# alist = bs.find_all('a')
# #print(repr(alist))

# with open('tmp.txt', 'a') as f:
#     for al in alist:
#         f.write(al.get('href'))

# M2
# url = 'http://www.btbtdy.me/btdy/dy6403.html'
url = 'https://www.btbtdy.me/btdy/dy11748.html'

# start chrome browser
browser = webdriver.Chrome()
options = webdriver.ChromeOptions()
# 不加载图片, 加速,但是无法对抗反爬虫
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2
#     }
# }
# options.add_experimental_option('prefs', prefs)
# 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"')
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

# BeautifulSoup

html = browser.page_source
spanlist = BeautifulSoup(html, 'lxml').find('ul', class_="p_list_02").find_all('a', class_="d1")

# Native selenium

# html = browser.find_elements_by_tag_name('a')
# # html = browser.find_elements_by_xpath("//a[@href]")
# for each in html:
#     print(each.get_attribute('href'))
# print(repr(spanlist))

with open('tmp2.txt', 'a') as f:
    for sl in spanlist:
        print(repr(sl.get('href')))
        f.write(sl.get('href') + "\n")



