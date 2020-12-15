# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import pytest
from time import sleep

#from web_project.public.myunit import MyTest
from ..public.myunit import MyTest

sendtext ="安通+测试消息Send"
# friendAccount = "xuxiaojing5"                    #好友帐号，有昵称，无备注
# friendAccountNickname="xiaoxu"                    #好友的昵称
# friendAccount = "5051183"                    #好友帐号，有昵称，无备注
friendAccount = "7329342"                    #好友帐号，有昵称，无备注
# friendAccountNickname="啊呀呀"                    #好友的昵称
friendAccountNickname="十三"                    #好友的昵称
account = '7338021'
password = 'a111111'

class TestSet(MyTest):
    '''安通+设置测试'''

    # def test_set01(self):
    #     '''登录成功，退出登录'''
    #     N=1
    #     for i in range(0,N):
    #         self.Set.enter_to_settind_page()
    #         sleep(3)
    #         self.Set.click_main_menu_settings_logout()
    #         sleep(2)
    #         self.Set.click_logout_hint_okbutton()
    #         sleep(5)
    #         self.driver.assert_true(self.Login.loginbutton_isdisplay())

    def test_set02(self):
        '''切换发送快捷键为Ctrl+Enter，并发送消息'''
        # self.Login.login(account, password)
        # sleep(5)
        self.Set.enter_to_settind_page()
        sleep(3)
        self.Set.click_main_menu_setting_shortcut()
        sleep(1)
        self.Set.click_main_menu_setting_shortcut_select()
        sleep(1)
        self.Set.click_main_menu_setting_shortcut_ctrlenter()
        sleep(1)
        self.Set.click_main_menu_setting_paper()
        sleep(2)
        self.Contact.click_main_menu_contact()
        sleep(1)
        self.Contact.click_contactlist_friendlistandgrouplist(friendAccountNickname)
        sleep(1)
        self.Contact.click_main_friend_detal_dialog_sendEnmessage()
        sleep(2)
        self.Chat.input_main_chat_inputbox(sendtext)
        sleep(3)
        self.Chat.shortcuts_main_chat_sendctrl()
        sleep(5)
        self.driver.assert_equal(self.Chat.main_chat_send_messageinfo_text(), sendtext)
        sleep(1)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),sendtext)
        self.Set.click_main_menu_settings()
        sleep(3)
        self.Set.click_main_menu_setting_shortcut()
        sleep(1)
        self.Set.click_main_menu_setting_shortcut_select()
        sleep(1)
        self.Set.click_main_menu_setting_shortcut_enter()
        sleep(1)
        self.Set.click_main_menu_setting_paper()

if __name__=="__main__":
    pytest.main("-v set_test.py::TestSet::test_set02")