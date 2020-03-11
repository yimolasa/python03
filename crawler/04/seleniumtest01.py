from selenium import webdriver
 
# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
# options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(chrome_options=options)

# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()
# browser = webdriver.Chrome()
# browser = webdriver.Ie()
# browser = webdriver.PhantomJs()
 
browser.get('http://baidu.com')
 
print(browser.title)

browser.save_screenshot("baidu.png")
browser.find_element_by_id("kw").send_keys("fff")
browser.find_element_by_id("su").click()

# dcap = dict(DesiredCapabilities.PHANTOMJS)
#             # 不载入图片，爬页面速度会快很多
# dcap["phantomjs.page.settings.loadImages"] = False
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
# browser.get('http://baidu.com')
 
# print(browser.title)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
# driver.quit()