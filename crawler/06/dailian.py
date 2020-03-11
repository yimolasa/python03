from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import re

pagesum = 0

# 定义一个taobao类


class taobao_infos:

    # 对象初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        # url = 'https://s.taobao.com/search?q=%E4%BB%A3%E7%BB%83%E6%80%80%E6%97%A7%E6%9C%8D'
        self.url = url
        self.username = "ook.com"
        self.password = "999"
        self.searchword = u'魔兽世界怀旧服代练'

        options = webdriver.ChromeOptions()
        # options.add_experimental_option(
        #     "prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        # options.add_experimental_option('excludeSwitches', ['enable-automation']) # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):

        # 打开网页
        self.browser.get(self.url)
        try:
            input = self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'forget-pwd.J_Quick2Static')))
            # for i in input:
            #     if i.is_displayed():
            #         i.click()
            input.click()
        except Exception as e:
            print(e)
        username = self.browser.find_element_by_id('TPL_username_1')
        # username.click()
        username.send_keys(self.username)
        time.sleep(2)

        password = self.browser.find_element_by_id('TPL_password_1')
        password.send_keys(self.password)
        time.sleep(8)

        self.browser.execute_script(
            "Object.defineProperties(navigator,{webdriver:{get:() => false}})")
        action = ActionChains(self.browser)
        time.sleep(2)
        butt = self.browser.find_element_by_id('nc_1_n1z')
        self.browser.switch_to.frame(
            self.browser.find_element_by_id('_oid_ifr_'))
        self.browser.switch_to.default_content()
        action.click_and_hold(butt).perform()
        action.reset_actions()
        time.sleep(2)
        action.move_by_offset(285, 0).perform()
        time.sleep(2)

        # button = self.wait.until(self.browser.find_element_by_id('J_SubmitStatic')
        button = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#J_SubmitStatic'))
        )
        # time.sleep(8)
        button.click()

    def qrcodelogin(self):
        self.browser.get(self.url)

        time.sleep(10)

    def testpage(self):
        self.browser.get("D:/source/Python/03/taobao.html")

    def jsearch(self):
        # searchbar = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        searchbar = self.wait.until(
            EC.presence_of_element_located((By.ID, 'q')))
        # searchbar = self.browser.find_element_by_id("q")
        searchbar.send_keys(self.searchword)
        searchbar.send_keys(Keys.ENTER)

    def collectitem(self):
        global pagesum
        time.sleep(3)
        print('collecting items')
        prices = self.browser.find_elements_by_tag_name("strong")
        del prices[0]  # delete <strong class="h" id="J_MiniCartNum"></strong>
        # for price in prices:
        #     print(price.text)
        solditems = self.browser.find_elements_by_class_name("deal-cnt")
        # for sitem in solditems:
        #     print(re.findall("\d+", sitem.text)[0])

        if (len(prices) == len(solditems)):
            print("collect successfully")
            for i in range(len(prices)):
                pagesum += float(prices[i].text) * \
                    float(re.findall("\d+", solditems[0].text)[0])
        else:
            print(str(len(prices)), str(len(solditems)))
        print(pagesum)    

    # def nextpage(self):
    #     time.sleep(3)
    #     self.browser.find_element_by_class_name("J_Ajax J_Pager link icon-tag").click()

    def next_page(self, page_number):

        page_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))  # 等待翻页输入框加载完成
        confirm_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        page_input.clear()  # 清空翻页输入框
        page_input.send_keys(page_number)  # 传入页数
        confirm_btn.click()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))  # 确认已翻到page_number页
        time.sleep(5)

    # 模拟向下滑动浏览

    def swipe_down(self, second):
        for i in range(int(second/0.1)):
            js = "var q=document.documentElement.scrollTop=" + str(300+200*i)
            self.browser.execute_script(js)
            time.sleep(0.1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        time.sleep(0.2)


if __name__ == "__main__":

    a = taobao_infos()
    # test page
    # a.testpage()

    # a.login()  # 登录
    a.qrcodelogin()

    a.jsearch()
    a.collectitem()
    for i in range(2, 11):
        a.swipe_down(2)
        try:
            a.next_page(i)
        except TimeoutException:    # 若发生异常，重新调用自己
            a.next_page(i)
        a.collectitem()
    print(str(pagesum))

