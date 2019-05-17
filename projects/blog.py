#_*_coding:utf-8_*_
# author : zhengjiani
# Date : 2019/5/14 上午9:36
# File : blog.py
# IDE ： PyCharm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://zhengjiani.github.io/")
assert "love" in driver.title

