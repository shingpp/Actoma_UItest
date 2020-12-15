# -*-coding:utf_8-*-
import  unittest,sys

import pytest

sys.path.append("./models")
sys.path.append("./page_obj")
from web_project.public.myunit import MyTest
# from ..public.myunit import MyTest
from  time import sleep

FRIEND_AND_GROUP = "搜索好友/群组"
PERSON = "搜索联系人(仅支持姓名)"
SEARCH_TEST = "5035447"           #搜索帐号
SEARCH_TESTRESULT = "备注"   #搜索结果（备注）
WRONG_TEST = "fhfhdfhghdhdh"   #不存在的内容
PERSON_NAME = "autoTest"           #集团通讯录好友名称
CONTENT = "安通+测试消息Send"      #发送消息内容


class TestSearch(MyTest):
    '''全局搜索'''

    def test_search01(self):
        '''搜索框获取焦点，选择好友/群组，搜索框显示：搜索好友/群组'''
        self.Search.click_search_friend_or_group()
        sleep(1)
        retext = self.Search.main_search_input_text()
        # print(retext)
        sleep(1)
        self.driver.assert_equal(retext, FRIEND_AND_GROUP)

    def test_search02(self):
        '''搜索框获取焦点，选择集团通讯录，搜索框显示：搜索联系人(仅支持姓名)'''
        self.Search.click_search_person()
        sleep(1)
        retext = self.Search.main_search_person_input_text()
        sleep(1)
        self.driver.assert_equal(retext, PERSON)

    def test_search03(self):
        '''搜索存在的备注或昵称,进行模糊搜索，搜索结果中只居中显示备注或昵称'''
        self.Search.click_search_friend_or_group()
        sleep(1)
        self.Search.main_search_input(SEARCH_TESTRESULT)
        sleep(2)
        self.driver.assert_equal(self.Search.main_search_result_list(SEARCH_TESTRESULT),"true")

    def test_search04(self):
        '''搜索不存在的内容，搜索列表为空'''
        self.Search.click_search_friend_or_group()
        sleep(1)
        self.Search.main_search_input(WRONG_TEST)
        sleep(2)
        self.driver.assert_equal(self.Search.main_search_result_null(),"未搜索到相关结果")

    def test_search05(self):
        '''搜索存在账号，同时又有备注或者昵称,进行模糊搜索'''
        self.Search.click_search_friend_or_group()
        sleep(1)
        self.Search.main_search_input(SEARCH_TEST)
        sleep(2)
        self.driver.assert_equal(self.Search.main_search_result_RemarkOrNickname(SEARCH_TESTRESULT),"true")
        self.driver.assert_equal(self.Search.main_search_result_account(SEARCH_TEST),"true")

    def test_search06(self):
        '''搜索集团联系人，进入会话发送消息'''
        self.Search.click_search_person()
        sleep(1)
        self.Search.main_search_person_input_name(PERSON_NAME)
        sleep(1)
        self.Search.mian_search_input_click_button()
        sleep(10)
        self.Search.main_search_result_click_person_name(PERSON_NAME)
        sleep(3)
        # print(qu.main_chat_head_name_text())
        self.driver.assert_equal(self.Chat.main_chat_head_name_text(), PERSON_NAME)
        sleep(1)
        self.Chat.input_main_chat_inputbox(CONTENT)
        sleep(3)
        self.Chat.shortcuts_main_chat_send()
        self.driver.assert_equal(self.Chat.main_chat_send_messageinfo_text(), CONTENT)
        sleep(3)
        text1 = self.Chat.main_messagelist_first_newmessage()
        self.driver.assert_equal(CONTENT, text1)

if __name__=="__main__":
    pytest.main("-v search_test.py::TestSearch::test_search06")



