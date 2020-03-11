from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

# # Set Proxy
# # options = webdriver.ChromeOptions()
# # options.add_argument('--proxy-server=127.0.0.1:1080')
# # browser = webdriver.Chrome(chrome_options=options)
# # browser.get('http://baidu.com')

# # browser = webdriver.PhantomJS()
# # browser = webdriver.Safari()
# # browser = webdriver.Chrome()
# # browser = webdriver.Ie()
# # browser = webdriver.PhantomJs()


# # html = requests.get(url='http://baidu.com',proxies={'http': 'http://127.0.0.1:1080'}).text
# # print(html)
# header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
#         }
# html = requests.get(url = 'http://www.xicidaili.com/nn/',headers=header).text
# # print(html)
# soup = BeautifulSoup(html, 'lxml')
# ip_list = soup.find(id='ip_list').find_all('tr')
# # print(len(ip_list))
# for ip_info in ip_list: 
#     print(repr(ip_info))



# print(browser.title)

# browser.save_screenshot("baidu.png")
# browser.find_element_by_id("kw").send_keys("fff")
# browser.find_element_by_id("su").click()
# browser.

url = 'http://www.zhaifu.tv/dongman/3694.html'
browser = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"')
browser = webdriver.Chrome(chrome_options=options)
browser.get(url)
html = browser.find_elements_by_tag_name('a')
# html = browser.find_elements_by_xpath("//a[@href]")
for each in html:
    print(each.get_attribute('href'))
