import lxml
import time
from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://zhengjiani.cn:8080/#/login?redirect=%2Fdashboard')
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
