# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from web_project.pages.chat_page import Chat
from web_project.pages.login_page import Login
# from ..pages.chat_page import Chat
# from ..pages.login_page import Login
from .base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import traceback
from selenium.webdriver.common.action_chains import ActionChains

class Contact(Page):

    # 封装登录，登录成功后，点击联系人按钮进入联系人页面
    def enter_to_chat_page(self):
        # self.Login = Login(self.driver)
        # self.Login.login()
        # sleep(5)
        self.click_main_menu_contact()#选择联系人
        sleep(2)

    # 封装点击好友，发送加密消息，断言聊天对话头与好友名称是否一致
    def click_friendlist_sendmsg(self, friend):
        self.Chat = Chat(self.driver)
        # self.enter_to_chat_page()#点击左侧联系人
        self.click_main_menu_contact()
        sleep(2)
        self.click_contactlist_friendlistandgrouplist(friend)#查找指定联系人
        sleep(1)
        self.click_main_friend_detal_dialog_sendEnmessage()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_chat_head_name_text(), friend)
        sleep(1)
        self.driver.switch_to_frame(self.Chat.main_chat_iframe_input_loc)
        sleep(1)
        self.driver.clear(self.Chat.main_chat_inputbox_loc)
        sleep(2)
        self.driver.switch_to_frame_out()

    # 封装添加查找好友
    def add_or_search_friend(self, friend):
        self.Chat = Chat(self.driver)
        self.click_main_contactlist_addfriendornewgroup()
        sleep(2)
        self.Chat.input_main_addfriend_inputbox(friend)
        sleep(2)
        self.Chat.click_main_addfriend_OKbutton()
        sleep(1)

    # 封装集团通讯录好友详情页面
    def Select_person(self, name, groups, group):
        self.enter_to_chat_page()# 打开联系人
        sleep(2)
        self.main_windowMax()
        sleep(2)
        self.click_main_contactlist_person()
        sleep(2)
        self.click_mian_contact_personlist_group(groups)
        sleep(2)
        self.click_mian_contact_personlist_group(group)
        sleep(4)
        self.click_mian_contact_personlist_group_friend(name)

    #封装群组列表
    def click_grouplist(self,groupname):
        self.enter_to_chat_page()
        sleep(1)
        self.click_main_contactlist_group()
        sleep(1)
        self.click_contactlist_friendlistandgrouplist(groupname)
        sleep(2)

    #封装创建群组页面
    def create_group(self):
        self.enter_to_chat_page()
        sleep(2)
        self.click_main_contactlist_group()
        sleep(2)
        self.click_main_contactlist_addfriendornewgroup()

    #左侧边栏联系人
    main_menu_contact_loc = "class=>at-menu-contact"
    def click_main_menu_contact(self):
        self.driver.click(self.main_menu_contact_loc)
    def main_menu_contact_attribute(self,attribute):
        return self.driver.get_attribute(self.main_menu_contact_loc,attribute)

    #联系人列表中新好友页面中的最新的验证消息
    main_messagelist_newfriend_row_loc= "//li[@class='list-item context-menu newfriends-notice ng-scope']"
    main_messagelist_newfriend_row_account_loc= "//li[@class='list-item context-menu newfriends-notice ng-scope']/div[2]/p/span"
    main_messagelist_newfriend_row_verifyinfo_loc= "class=>desc-nowrap"
    #取指定行的帐户信息
    def main_messagelist_newfriend_row_account_text(self,i):
        elements = self.driver.get_elements(self.main_messagelist_newfriend_row_loc)
        return self.driver.get_text(self.driver.get_sub_element(elements[i],self.main_messagelist_newfriend_row_account_loc))

    #取指定行的验证信息
    def main_messagelist_newfriend_row_verifyinfo_text(self,i):
        elements = self.driver.get_elements(self.main_messagelist_newfriend_row_loc)
        return self.driver.get_text(self.driver.get_sub_element(elements[i],self.main_messagelist_newfriend_row_verifyinfo_loc))

    #联系人列表中的好友
    main_contactlist_friend_loc = "//li[@ng-class='{'active':indexId === 'friend'}']"
    def click_main_contactlist_friend(self):
        self.driver.click(self.main_contactlist_friend_loc)
    def main_contactlist_friend_attribute(self,attribute):
        return self.driver.get_attribute(self.main_contactlist_friend_loc,attribute)

    # 我的好友中点击安通+团队
    #根据名称name点击好友，没有则返回异常
    main_contactlist_antong_loc = "class=>info-txt"
    def click_contactlist_antonglist(self, name):
        self.Chat = Chat(self.driver)
        # self.enter_to_chat_page()#点击左侧联系人
        self.click_main_menu_contact()
        sleep(2)
        lists = self.driver.get_elements(self.main_contactlist_antong_loc)
        found = 0
        for list in lists:
            if name in list.text:
                list.click()
                found = 1
                break
        if found != 1:
            raise Exception("没有找到对象")

    #单击好友或者群组列表，会弹出好友或群组详情
    main_contactlist_friendlistandgrouplist_loc = "class=>info-txt"
    def click_contactlist_friendlistandgrouplist(self,name):
        lists = self.driver.get_elements(self.main_contactlist_friendlistandgrouplist_loc)
        found = 0
        for list in lists:
            if list.text == name:
                list.click()
                found = 1
                break
        if found!=1:
            raise Exception("没有找到对象")

    #点击添加好友或新建群组按钮
    main_contactlist_addfriendornewgroup_loc= "class=>addfrisend-icon"
    def click_main_contactlist_addfriendornewgroup(self):
        self.driver.click(self.main_contactlist_addfriendornewgroup_loc)

    #联系人列表中的新好友
    main_contactlist_newfriend_loc = "//div[@class='conv-lists-box ng-isolate-scope']/ul/li/div/span"
    def click_main_contactlist_newfriend(self):
        self.driver.click(self.main_contactlist_newfriend_loc)
    def main_contactlist_newfriend_attribute(self,attribute):
        return self.driver.get_attribute(self.main_contactlist_newfriend_loc,attribute)

    # 联系人列表中新好友页面的顶部信息
    main_contactlist_newfriend_title_loc = "//span[@class='text-black']/span"
    # main_contactlist_newfriend_title_loc = (By.XPATH,"//div[@class='content-pannel-head']/p/span/span/span")
    def main_contactlist_newfriend_title_text(self):
        return self.driver.get_text(self.main_contactlist_newfriend_title_loc)

    #联系人列表中的好友
    main_contactlist_friend_loc = "//div[@class='conv-lists-box ng-isolate-scope']/ul/li[3]/div/span"
    def click_main_contactlist_friend(self):
        self.driver.click(self.main_contactlist_friend_loc)

    def main_contactlist_friend_attribute(self,attribute):
        return self.driver.get_attribute(self.main_contactlist_friend_loc,attribute)

    #联系人列表中的群组
    main_contactlist_group_loc = "//div[@class='conv-lists-box ng-isolate-scope']/ul/li[4]/div/span"
    def click_main_contactlist_group(self):
        self.driver.click(self.main_contactlist_group_loc)
    def main_contactlist_group_attribute(self,attribute):
        return self.driver.get_attribute(self.main_contactlist_group_loc,attribute)

    #好友信息对话中的发送加密消息
    # main_friend_detal_dialog_sendEnmessage_loc=(By.XPATH,"//button[@ng-show='isFriend && !isCurrentUser && !isAtTeam']")
    main_friend_detal_dialog_sendEnmessage_loc= "//button[@ng-show='(member.personId && member.account || isFriend) && !isCurrentUser && !isAddFriend && !isAtTeam']"
    def click_main_friend_detal_dialog_sendEnmessage(self):
        self.driver.click(self.main_friend_detal_dialog_sendEnmessage_loc)

    #好友信息对话中的添加好友
    # main_friend_detal_dialog_addfriend_loc=(By.XPATH,"//button[@ng-show='!isFriend && !isAddFriend && !isCurrentUser && !isAtTeam']")
    main_friend_detal_dialog_addfriend_loc= "//button[@ng-show='member.account && !isFriend && !isAddFriend && isCurrentUser == false && !isAtTeam']"
    def click_main_friend_detal_dialog_addfriend(self):
        self.driver.click(self.main_friend_detal_dialog_addfriend_loc)

    #好友页面的帐户信息头
    main_friend_detal_dialog_head_loc= "//div[@class='friend-detal-dialog-profile']/p[@class='ng-binding']"
    def main_friend_detal_dialog_head_text(self):
        return self.driver.get_text(self.main_friend_detal_dialog_head_loc)

    #好友页面的帐户信息
    main_friend_detal_dialog_account_loc = "//div[@class='detailRow']/div[2]/label"
    def main_friend_detal_dialog_account_text(self):
        return self.driver.get_text(self.main_qfriend_detal_dialog_account_loc)

    #好友页面的昵称
    main_friend_detal_dialog_nickname_loc = "//div[@class='row nickName']/label"
    def main_friend_detal_dialog_nickname_text(self):
        return self.driver.get_text(self.main_friend_detal_dialog_nickname_loc)

    #好友页面的备注
    main_friend_detal_dialog_comment_loc = "//div[@class='row comment']/label/span[@ng-bind='displayRemark']"
    def main_friend_detal_dialog_comment_text(self):
        return self.driver.get_text(self.main_friend_detal_dialog_comment_loc)

    #好友页面的备注编辑按钮
    main_friend_detal_dialog_comment_editbutton_loc = "class=>edit-icon"
    def click_main_friend_detal_dialog_comment_editbutton(self):
        self.driver.click(self.main_friend_detal_dialog_comment_editbutton_loc)

    #好友页面的备注编辑输入框和快捷键enter确定按钮
    main_friend_detal_dialog_comment_edit_inputbox_loc = "//div[@ng-show='isEditRemark']/input"
    def input_main_friend_detal_dialog_comment_edit_inputbox(self,text):
        self.driver.clear(self.main_friend_detal_dialog_comment_edit_inputbox_loc)
        sleep(1)
        self.driver.input(self.main_friend_detal_dialog_comment_edit_inputbox_loc,text)
    def click_main_friend_detal_dialog_comment_edit_OKbutton(self):
        self.driver.input(self.main_friend_detal_dialog_comment_edit_inputbox_loc,Keys.ENTER)

    #好友页面的备注编辑确定按钮
    # main_friend_detal_dialog_comment_edit_OKbutton_loc = (By.XPATH,"//div[@ng-show='isEditRemark']/button")
    # def click_main_friend_detal_dialog_comment_edit_OKbutton(self):
    #     self.find_element(*self.main_friend_detal_dialog_comment_edit_OKbutton_loc).click()

    #添加好友发送信息输入框
    main_friend_detal_dialog_addfriend_inputbox_loc= "class=>person-discription-input"
    def input_main_friend_detal_dialog_addfriend_inputbox(self,text):
        self.driver.input(self.main_friend_detal_dialog_addfriend_inputbox_loc,text)

    #添加好友发送信息输入框的清空按钮
    main_friend_detal_dialog_addfriend_inputbox_deletebutton_loc= "class=>delete-discription-input"
    def click_main_friend_detal_dialog_addfriend_inputbox_deletebutton(self):
        self.driver.click(self.main_friend_detal_dialog_addfriend_inputbox_deletebutton_loc)

    #添加好友发送信息的发送按钮
    main_friend_detal_dialog_addfriend_sendbutton_loc= "class=>edit-person-discription"
    def click_main_friend_detal_dialog_addfriend_sendbutton(self):
        self.driver.click(self.main_friend_detal_dialog_addfriend_sendbutton_loc)

    #好友信息对话安通+团队中的进入
    #文件传输助手详情消息页面中点击进入
    main_friend_detal_dialog_enter_loc = "//button[@ng-show='isAtTeam']"
    def click_main_friend_detal_dialog_enter(self):
        self.driver.click(self.main_friend_detal_dialog_enter_loc)

    main_friend_details_sendmessage_loc = "//button[.='发送加密消息']"
    def click_main_friend_details_sendmessage(self):
        '''点击发送加密消息按钮'''
        self.driver.click(self.main_friend_details_sendmessage_loc)

    #创建群组中搜索框
    main_newgroup_searchbox_loc= "class=>search-input"
    def input_main_newgroup_searchbox(self,text):
        self.driver.input(self.main_newgroup_searchbox_loc,text)

    # 创建群组中勾选好友的复选框
    main_newgroup_checkbox_loc = "class=>choose-icon-content"
    def check_main_newgroup_checkbox(self,i):
        elements = self.driver.get_elements(self.main_newgroup_checkbox_loc)
        self.driver.click(elements[i])

    #创建群组中显示好友的昵称
    main_newgroup_friendname_loc = "//div[@class='choose-info-txt ng-binding']"
    def main_newgroup_friendname_text(self,i):
        elements = self.driver.get_elements(self.main_newgroup_friendname_loc)
        return self.driver.get_text(elements[i])

    # 发起群聊页面显示搜索结果
    # 0.3.2.10版本上适用
    main_newgroup_searchresult_loc = "//div[@class='tab-pane ng-scope active']/ul[2]/li/div/div[2]"
    def main_newgroup_searchresult_text(self,name):
        texts = self.driver.get_elements(self.main_newgroup_searchresult_loc)
        exits = "false"
        for text in texts:
            # 此if方法还是进行精确搜索，可能查看不在搜索列表的第一位，但是无法进行模糊搜索
            # if(text.text == name):
            #     exits = "true"
            if name in text.text:
                exits = "true"
        return exits

    #创建群组中勾选第几个好友的复选框并返回此好友的昵称
    def check_main_newgroup_checkbox_returnfriendname(self,i):
        self.check_main_newgroup_checkbox(i)
        return self.main_newgroup_friendname_text(i)

    #创建群组中显示勾选几个联系人
    main_newgroup_sidetoptext_loc = "class=>side-top-word"
    def main_newgroup_sidetoptext(self):
        return self.driver.get_text(self.main_newgroup_sidetoptext_loc)

    #创建群组中确定按钮
    main_newgroup_OKbutton_loc = "class=>btn-confirm"
    def click_main_newgroup_OKbutton(self):
        self.driver.click(self.main_newgroup_OKbutton_loc)

    # 创建群组中取消按钮
    main_newgroup_cancelbutton_loc = "class=>btn-cancel"
    def click_main_newgroup_cancelbutton(self):
        self.driver.click(self.main_newgroup_cancelbutton_loc)

    #联系人-集团通讯录
    main_main_contactlist_person_loc = "//div[@class='conv-lists-box ng-isolate-scope']/ul/li[5]"
    def click_main_contactlist_person(self):
        self.driver.click(self.main_main_contactlist_person_loc)

    #集团通讯录列表顶部
    main_contactlist_personname_text_loc = "//p[@class='head-title conv-title']/span"
    def main_contactlist_personname_text(self):
        return self.driver.get_text(self.main_contactlist_personname_text_loc)
    #集团通讯录-Test_A
    main_contact_personlist_group_loc = "//h4[@class='panel-title']/a/span"
    def click_mian_contact_personlist_group(self,group):
        messages = self.driver.get_elements(self.main_contact_personlist_group_loc)
        found = 0
        for message in messages:
            if message.text == group:
                message.click()
                found = 1
                break
        if found != 1:
            raise Exception("没有找到对象")
    #集团通讯录-TestB-autoTest
    main_contact_personlist_group_friend_loc = "//ul[@ng-repeat='member in item.person']/li/div[2]/p"
    def click_mian_contact_personlist_group_friend(self,name):
        messages = self.driver.get_elements(self.main_contact_personlist_group_friend_loc)
        found = 0
        for message in messages:
            if message.text == name:
                message.click()
                found = 1
                break
        if found != 1:
            raise Exception("没有找到对象")

    # 窗口最大化
    main_windowMax_loc = "id=>openExpandMini"
    def main_windowMax(self):
        self.driver.click(self.main_windowMax_loc)