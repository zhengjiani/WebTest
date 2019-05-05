# -*- coding: UTF-8 -*-
from __future__ import absolute_import

import time
import unittest


from bok_choy.web_app_test import WebAppTest
from projects.litemall_page2 import LoginPage,SearchPage,UserPage
from ddt import ddt,unpack,data
@ddt
class Test(WebAppTest):
    def setUp(self):
        super(Test, self).setUp()
        self.login_page = LoginPage(self.browser)
        self.login_page.visit().login("","")
    @data(['use','222'])
    @unpack
    def test_search(self,username,phone):
        self.search_page = SearchPage(self.browser)
        if username == 'user123' and phone == '222':
            UserPage(self.browser).visit()
            self.search_page.enter_search_items(username,phone)
if __name__=='__main__':
    unittest.main()
