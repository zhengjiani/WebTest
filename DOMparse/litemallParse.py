import lxml
from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("http://localhost:9527/#/login?redirect=%2Fdashboard")
#登录
driver.find_element_by_xpath("//*[@id='app']/div/form/div[2]/div/div/input").send_keys('')
driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/div/input").send_keys('')
driver.find_element_by_xpath("//*[@id='app']/div/form/button").click()
time.sleep(2)
cookie_list = driver.get_cookies()
for item in cookie_list: driver.add_cookie(
    {
        'domain': 'localhost',
        'httpOnly': False,
        'name': 'X-Litemall-Admin-Token',
        'path': '/',
        'secure': False,
        'value': '1fpzctbhesj4eqfg5e2k6gkg77m2u220'
    }
)
time.sleep(5)
#取出只含有可操作元素的部分
def get_all_path(html):
    dom = etree.HTML(html)
    dom_str=dom.xpath('//*')
    for i in dom_str:
        tree=lxml.etree.ElementTree(i)
        list_xpath=tree.getpath(i)
        print(list_xpath)
def get_diff_path(html1,html2):
    dom1 = etree.HTML(html1)
    dom1_str=dom1.xpath('//*')
    dom2 = etree.HTML(html2)
    dom2_str=dom2.xpath('//*')
    ret_dom=list(set(dom2_str).difference(set(dom1_str)))
    for i in ret_dom:
        tree = lxml.etree.ElementTree(i)
        list_xpath = tree.getpath(i)
        print(list_xpath)
#Alert(driver).dismiss()
htm1=driver.page_source
#获取所有可点击元素
li1=driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]/li").click()



driver.close()