from time import sleep
import sys,random

import pytest

sys.path.append("./models")
sys.path.append("./page_obj")

import os

import time
from selenium import webdriver

from web_project.public.myunit import MyTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from ..public.myunit import MyTest


PictureJS = "document.querySelector('#testPictureBtn').style.width = '19px'"
FileJS="document.querySelector('#testFileBtn').style.width = '19px'"
TEST = "安通+测试消息Send"
GROUP_TEST ="安通+测试群组消息Send"


account = "7341424"
password = "a123123"
# FRIEND = "kl"
# FRIEND = "5085036"
FRIEND = "半步"                 #好友的昵称或备注
FRIEND_MSG_NUM = 20           #二人会话发送的消息数量
FRIEND_PIC_NUM = 2             #二人会话发送的图片数量
FRIEND_FILE_NUM = 1           #二人会话发送的文件数量
WITHDRAW_TEST = "你 撤回了一条消息"         #撤回消息后显示的事件通知
SEND_SUS = "已发送"           #已发送状态
PICTURE = "[图片]"
# GROUP_MSG = "亚尔呀"         #发送消息的群组名称  准生产环境自动化测试消息Group
GROUP_MSG = "123"
GROUP_PIC = "呐呐"         #发送图片的群组名称
GROUP_MSG_NUM = 10               #群组发送消息的最大数量
GROUP_PIC_NUM = 5000                #群组发送图片的最大数量
TEST_A = "安通⁺团队"
LINK = "芯片管家是什么？"
UPLIMIT = "不能插入超过10个文件"
DRAFT = "[草稿]"
FILE = "[文件]"
Text_File_transfer_assistant = "文件传输助手"
Text_Friend_retraction_message = "撤回了一条消息"



class TestChat(MyTest):

    '''
    消息页面测试，包含二人聊天和群组聊天
    '''

    # def test_chat21(self):
    #     '''二人聊天中发送文件---发送非图片文件'''
    #
    #     self.Login.login(account,password)
    #     sleep(5)
    #     # self.driver.assert_true(self.Chat.main_add_attribute_isdisplay())
    #
    #     self.Contact.click_friendlist_sendmsg(FRIEND)  # 进入好友聊天
    #     sleep(2)
    #     fail1 = 0
    #     # self.driver.js(FileJS)
    #     for i in range(0, FRIEND_FILE_NUM):  # 文件数量
    #         self.Chat.click_main_chat_filebutton()
    #         sleep(3)
    #         os.system("D:\\testexe\\uploadFile01.exe")
    #         sleep(2)
    #         self.Chat.shortcuts_main_chat_send()
    #         time1=time.time()
    #         #需要添加一个扫描机制，不停扫描等待发送成功 ball-spin-fade-loader-1
    #         # 我试着添加了一个显示等待，但是每次等待的时间明显过长
    #         WebDriverWait(self.driver.driver,50,0.5).until_not(
    #             EC.presence_of_element_located((By.CLASS_NAME,'ball-spin-fade-loader-1'))
    #         )
    #
    #         time2 = time.time()
    #         time3=time2-time1
    #         print("时间：%s"%time3)
    #         # print()
    #         self.driver.get_screenshot("test_chat21_sendfilefail%s.jpg" % fail1)
    #         text1 = self.Chat.main_messagelist_first_newmessage()
    #         print(text1)
    #         text2 = "[文件] " + self.Chat.main_display_area_lastfile_name()
    #         print(text2)
    #         try:
    #             self.driver.assert_equal(text1, text2)
    #             sleep(2)
    #         except:
    #             fail1 = fail1 + 1
    #             self.driver.get_screenshot("test_chat21_sendfilefail%s.jpg" % fail1)
    #             sleep(2)
    #     if fail1 != 0:
    #         raise Exception("发送失败%s；" % fail1)

    # @pytest.mark.skip
    def test_chat01(self):
        '''2人聊天选择一个好友，点击发送按钮，发送加密消息、加密图片、表情、文件'''
        self.Login.login(account, password)
        a = random.randint(100,1000)
        text = TEST + str(a)

        self.Contact.click_friendlist_sendmsg(FRIEND)
        self.Chat.input_main_chat_inputbox(text)#输入文本
        sleep(3)
        self.Chat.click_main_chat_sendbutton()#发送
        sleep(3)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)

    def test_chat02(self):
        '''2人聊天选择一个好友，Enter,发送加密消息'''
        self.Login.login(account, password)
        a = random.randint(112,10000)
        text = TEST + str(a)
        self.Contact.click_friendlist_sendmsg(FRIEND)#FRIEND好友id
        sleep(2)
        self.Chat.input_main_chat_inputbox(text)#输入文本
        sleep(2)
        self.Chat.shortcuts_main_chat_send()
        sleep(1)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)


    def test_chat03(self):
        '''2人聊天选择一个好友，发送N次加密消息'''
        self.Login.login(account, password)
        self.Contact.click_friendlist_sendmsg(FRIEND)
        fail1=0
        fail2=0
        for i in range(0, FRIEND_MSG_NUM):
            text = TEST + str(i)
            if self.Chat.main_chat_head_name_text() != FRIEND:
                self.Chat.click_main_messagelist_accountname(FRIEND)
            self.Chat.input_main_chat_inputbox(text)
            sleep(2)
            self.Chat.shortcuts_main_chat_send()
            sleep(2)
            try:
                # self.driver.assert_equal(self.Chat.main_chat_send_messageinfo_text(),text)
                self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)
            except:
                fail1 = fail1 + 1
                self.driver.get_screenshot("test_chat03_send%s.jpg" % fail1)
                sleep(2)
            try:
                sleep(1)
                text1 = self.Chat.main_messagelist_first_newmessage()
                self.driver.assert_equal(text,text1)
            except:
                fail2 = fail2 + 1
                self.driver.get_screenshot("test_chat03_lastmsg%s.jpg" % fail2)
                sleep(2)
        if fail1!=0 or fail2 !=0:
            raise Exception("发送失败%s；显示最新消息失败%s"%(fail1,fail2))

    def test_chat04(self):
        '''二人聊天中发送图片'''
        '''
            执行该用例时，将C:\Program Files (x86)\Actoma\AT-APP\views\session\chat目录下的chat.css文件中
              .conv-detail-pannel .send-msg-box-wrapper .input-area .tool-bar .tool-item .file-input层级中 width更改为19px;
            以下脚本中涉及发送图片类的用例都需要更改；
        '''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_friendlist_sendmsg(FRIEND)
        sleep(2)
        fail1=0
        # self.driver.js(PictureJS)
        for i in range(0,FRIEND_PIC_NUM):
            self.Chat.click_main_chat_picturebutton()
            sleep(3)
            #SendKeys第三方库只适用于Python2.7版本
            # SendKeys.SendKeys('D:\\picture.jpg')
            # SendKeys.SendKeys("{Enter}")
            # os.system("D:\\Actoma_autotest\\single_uppicture.exe")
            os.system("F:\\codeProject\\Actoma-autotest\\ext\\test_upload_img_01.exe")
            sleep(2)
            self.Chat.shortcuts_main_chat_send()
            sleep(3)
            text1 = self.Chat.main_messagelist_first_newmessage()
            try:
                self.driver.assert_equal(text1,"[图片]")
                sleep(2)
            except:
                fail1 = fail1 + 1
                self.driver.get_screenshot("test_chat04_sendpicturefail%s.jpg" % fail1)
                sleep(2)
        if fail1!=0:
            raise Exception("发送失败%s；"%fail1)

    # def test_chat05(self):
    #     '''二人聊天中发送超过10张图片'''
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     self.driver.js(PictureJS)
    #     self.Chat.click_main_chat_picturebutton()
    #     sleep(1)
    #     os.system("D:\\Actoma_autotest\\batches_uppicture.exe")
    #     sleep(1)
    #     self.Chat.click_main_chat_picturebutton()
    #     os.system("D:\\Actoma_autotest\\single_uppicture.exe")
    #     sleep(1)
    #     self.Chat.wait_toastMessage_hint_isdisplay(UPLIMIT)
    #     sleep(3)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #
    def test_chat06(self):
        '''
        功能：1.发送一条文本消息，判定已发送状态;
          2.鼠标右键，点击撤回
        编写者：cuihong
        '''
        self.Login.login(account, password)
        self.Contact.click_friendlist_sendmsg(FRIEND)
        sleep(2)
        text = TEST + str(0)
        self.Chat.input_main_chat_inputbox(text)
        sleep(1)
        self.Chat.click_main_chat_sendbutton()
        sleep(3)
        self.Chat.context_click_main_message(-1)
        sleep(2)
        self.Chat.Click_main_callback()
        sleep(2)

    #    # def test_chat07(self):
    #     '''
    #     功能：二人会话，撤回图片消息
    #     编写者：cuihong
    #     :return:
    #     '''
    #     N = 2
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(1)
    #     fail1 = 0
    #     self.driver.js(PictureJS)
    #     for i in range(0,N):
    #         self.Chat.click_main_chat_picturebutton()
    #         sleep(1)
    #         os.system("D:\\Actoma_autotest\\single_uppicture.exe")        #跑脚本时需要在D盘放入该文件
    #         sleep(2)
    #         self.Chat.shortcuts_main_chat_send()
    #         sleep(4)
    #         self.Chat.context_click_main_tpmessage(-1)
    #         sleep(2)
    #         self.Chat.Click_main_callbacktp()
    #         sleep(1)
    #     if fail1!=0:
    #         raise Exception("发送失败%s；"%fail1)
    #
    def test_chat08(self):
        '''
        功能：1.发送多条消息，判定已发送状态;
          2.鼠标右键，点击依次撤回会话中最后一条消息
        '''
        self.Login.login(account, password)
        M = 2
        self.Contact.click_friendlist_sendmsg(FRIEND)
        sleep(2)
        for i in range(0,M):
            text = TEST + str(i)
            if self.Chat.main_chat_head_name_text() != FRIEND:
                self.Chat.click_main_messagelist_accountname(FRIEND)
            self.Chat.input_main_chat_inputbox(text)
            sleep(1)
            self.Chat.shortcuts_main_chat_send()
            sleep(3)
        for x in range(0,M):
            self.Chat.context_click_main_message(-1)
            sleep(2)
            self.Chat.Click_main_callback()
            sleep(2)

    # def test_chat10(self):
    #     '''双击进行快速截图，使用快捷键进行发送'''
    #     self.Login.login(account, password)  # 登录模组
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     #点击截图按钮，选择截图区域
    #     os.system("D:\\AT+autotest\\screenshots.exe")
    #     sleep(3)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #     text1 = self.Chat.main_messagelist_first_newmessage()
    #     self.driver.assert_equal(PICTURE,text1)
    # '''
    # 消息页面测试，群组聊天
    # '''
    #
    # @pytest.mark.skip
    def test_chat11(self):
        '''群组聊天，选择一个群组，点击发送按钮，发送加密消息'''
        self.Login.login(account, password)
        a = random.randint(1000,10000)
        text = GROUP_TEST + str(a)
        self.Contact.click_grouplist(GROUP_MSG)
        sleep(2)
        self.Chat.input_main_chat_inputbox(text)
        sleep(3)
        self.Chat.click_main_chat_sendbutton()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)
        sleep(1)

    def test_chat12(self):
        '''群组聊天，选择一个群组，Enter发送加密消息'''
        self.Login.login(account, password)
        a = random.randint(1000,10000)
        text = GROUP_TEST + str(a)
        self.Contact.click_grouplist(GROUP_MSG)
        sleep(2)
        self.Chat.input_main_chat_inputbox(text)
        sleep(3)
        self.Chat.shortcuts_main_chat_send()
        sleep(5)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)
        sleep(1)

    def test_chat13(self):
        '''群组聊天，选择一个群组，发送N次加密消息'''
        self.Login.login(account, password)
        self.Contact.click_grouplist(GROUP_MSG)
        fail1=0
        fail2=0
        for i in range(0, GROUP_MSG_NUM):
            text = TEST + str(i)
            if self.Chat.main_chat_head_name_text() != GROUP_MSG:
                self.Chat.click_main_messagelist_accountname(GROUP_MSG)
            self.Chat.input_main_chat_inputbox(text)
            sleep(1)
            self.Chat.shortcuts_main_chat_send()
            sleep(1)
            try:
                self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)
            except:
                fail1 = fail1 + 1
                self.driver.get_screenshot("test_chat13_sendmessagefail%s.jpg" %fail1 )
                sleep(1)
            try:
                sleep(1)
                text1 = self.Chat.main_messagelist_first_newmessage()
                self.driver.assert_equal(text,text1)
            except:
                fail2 = fail2 + 1
                self.driver.get_screenshot("test_chat13_latestnewsfail%s.jpg" %fail2 )
                sleep(2)
        if fail1!=0 or fail2 !=0:
            raise Exception("发送失败%s；显示最新消息失败%s"%(fail1,fail2))

    # def test_chat14(self):
    #     '''群组聊天，选择一个群组，发送图片'''
    #     # 点击安通+中图片按钮后，调出windows系统框，选择图片路径后，点击系统框的确定按钮发送
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     fail1=0
    #     self.driver.js(PictureJS)
    #     for i in range(0,GROUP_PIC_NUM):
    #         if self.Chat.main_chat_head_name_text() != GROUP_PIC:
    #             self.Chat.click_main_messagelist_accountname(GROUP_PIC)
    #         self.Chat.click_main_chat_picturebutton()
    #         sleep(3)
    #         os.system("D:\\Actoma_autotest\\single_uppicture.exe")
    #         sleep(2)
    #         self.Chat.shortcuts_main_chat_send()
    #         # self.Chat.main_chat_send_message_button()
    #         # self.Chat.main_chat_send_message_button()
    #         sleep(3)
    #     #     text1 = self.Chat.main_messagelist_first_newmessage()
    #     #     try:
    #     #         self.driver.assert_equal(text1,PICTURE)
    #     #     except:
    #     #         fail1 = fail1 + 1
    #     #         self.driver.get_screenshot("test_chat_sendpicturefail%s.jpg" % fail1)
    #     #         sleep(2)
    #     # if fail1!=0:
    #     #     raise Exception("发送失败%s；"%fail1)
    #
    # def test_chat15(self):
    #     '''群组聊天中发送超过10张图片'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     self.driver.js(PictureJS)
    #     self.Chat.click_main_chat_picturebutton()
    #     sleep(1)
    #     os.system("D:\\Actoma_autotest\\batches_uppicture.exe")
    #     self.Chat.click_main_chat_picturebutton()
    #     os.system("D:\\Actoma_autotest\\single_uppicture.exe")
    #     sleep(1)
    #     self.Chat.wait_toastMessage_hint_isdisplay(UPLIMIT)
    #     sleep(3)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #
    def test_chat16(self):
        '''
        功能：群聊中，发送消息之后，撤回
        编写者：cuihong
        '''
        self.Login.login(account, password)
        self.Contact.click_grouplist(GROUP_MSG)
        sleep(2)
        fail1 = 0
        for i in range(0,2):
            if self.Chat.main_chat_head_name_text() != GROUP_MSG:
                self.Chat.click_main_messagelist_accountname(GROUP_MSG)
            self.Contact.click_grouplist(GROUP_MSG)
            self.Chat.input_main_chat_inputbox(GROUP_TEST)
            sleep(1)
            self.Chat.shortcuts_main_chat_send()
            sleep(3)
            self.Chat.context_click_main_message(-1)
            sleep(1)
            self.Chat.Click_main_callback()
            sleep(1)
            text1 = self.Chat.main_messagelist_first_newmessage()
            try:
              self.driver.assert_equal(text1,WITHDRAW_TEST)
              sleep(2)
            except:
              fail1 = fail1+1
              self.driver.get_screenshot("test_chat16_callbackfail%s.jpg" %fail1)
              sleep(2)
        if fail1 !=0:
            raise Exception("撤回失败%s: "%fail1)
    #
    # def test_chat17(self):
    #     '''消息列表中，点击安通+团队，进入详情页面'''
    #     sleep(1)
    #     self.Login.login()
    #     sleep(5)
    #     self.Chat.click_main_messagelist_accountname(TEST_A)
    #     sleep(2)
    #     self.driver.assert_equal(TEST_A, self.Chat.main_chat_Actoma_title_text())
    #     sleep(2)
    #     self.Chat.click_main_chat_Actoma_WhatIsActoma(LINK)
    #     sleep(2)
    #     # handles = self.driver.window_handles
    #     # mainhandle = self.driver.current_window_handle
    #     # self.driver.switch_to_window(handles[2])
    #     self.driver.switch_to_window(2)
    #     sleep(1)
    #     self.driver.assert_equal(self.Chat.newwindows_whatisActoma_title_text(),LINK)
    #     sleep(2)
    #     self.driver.close()
    #
    # def test_chat18(self):
    #     '''消息列表中，点击安通+团队，进入详情页面,点击关闭'''
    #     self.Login.login()
    #     sleep(5)
    #     self.Chat.click_main_messagelist_accountname(TEST_A)
    #     sleep(2)
    #     self.driver.assert_equal(TEST_A,self.Chat.main_chat_Actoma_title_text())
    #     sleep(2)
    #     self.Chat.click_main_chat_Actoma_WhatIsActoma(LINK)
    #     sleep(2)
    #     self.driver.switch_to_window(2)
    #     sleep(2)
    #     self.Chat.close_windows()
    #     sleep(2)
    #
    # def test_chat19(self):
    #     '''
    #     功能：编辑框中输入@
    #           @弹框中最后一位联系人
    #          发送
    #     编写：cuihong
    #     '''
    #     self.Contact.click_grouplist(GROUP_MSG)
    #     sleep(2)
    #     fail1 = 0
    #     for i in range(0,2):
    #         text ="@"
    #         self.Chat.input_main_chat_inputbox(text)
    #         sleep(1)
    #         self.Chat.select_main_groupmemer(-1)
    #         sleep(2)
    #         self.Chat.shortcuts_main_chat_send()
    #         sleep(2)
    #         text1 = self.Chat.main_messagelist_first_newmessage()
    #         text2 = self.Chat.main_messagelist_message()
    #         try:
    #             self.driver.assert_equal(text1,text2)
    #             sleep(2)
    #         except:
    #             fail1 = fail1+1
    #             self.driver.get_screenshot("chat_testsend@fail%s: "%fail1)
    #     if fail1 !=0:
    #         raise Exception("发送@消息失败%s"%fail1)
    #
    # def test_chat20(self):
    #     '''
    #     前提：会话中有好友发来的消息
    #     功能：右击头像@好友
    #     编者：cuihong
    #     :return:
    #     '''
    #     self.Contact.click_grouplist(GROUP_MSG)
    #     sleep(1)
    #     for i in range(0,2):
    #         self.Chat.context_main_lastimg(-1)
    #         sleep(1)
    #         self.Chat.click_main_pop()
    #         sleep(1)
    #         self.Chat.shortcuts_main_chat_send()
    #         sleep(2)
    #
    def test_chat21(self):
        '''二人聊天中发送文件---发送非图片文件'''
        self.Login.login(account, password)
        self.Contact.click_friendlist_sendmsg(FRIEND)#进入好友聊天
        sleep(2)
        fail1=0
        # self.driver.js(FileJS)
        for i in range(0,FRIEND_FILE_NUM):#文件数量
            self.Chat.click_main_chat_filebutton()
            sleep(3)
            os.system("D:\\testexe\\uploadFile01.exe")
            sleep(2)
            self.Chat.shortcuts_main_chat_send()
            sleep(3)
            text1 = self.Chat.main_messagelist_first_newmessage()
            text2 = "[文件] " + self.Chat.main_display_area_lastfile_name()
            try:
                self.driver.assert_equal(text1,text2)
                sleep(2)
            except:
                fail1 = fail1 + 1
                self.driver.get_screenshot("test_chat21_sendfilefail%s.jpg" % fail1)
                sleep(2)
        if fail1!=0:
            raise Exception("发送失败%s；"%fail1)
    #
    # def test_chat22(self):
    #     '''
    #     功能：二人聊天发送文件--图片文件
    #     编者：cuihong
    #     :return: null
    #     '''
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     fail1 = 0
    #     self.driver.js(FileJS)
    #     for i in range(0,FRIEND_FILE_NUM):
    #         self.Chat.click_main_chat_filebutton()
    #         sleep(3)
    #         os.system("D:\\Actoma_autotest\\single_uppicture.exe")
    #         sleep(2)
    #         self.Chat.shortcuts_main_chat_send()
    #         sleep(3)
    #         text1 = self.Chat.main_messagelist_first_newmessage()
    #         try:
    #             self.driver.assert_equal(text1,PICTURE)
    #             sleep(2)
    #         except:
    #             fail1 = fail1+1
    #             self.driver.get_screenshot("test_chat22_sendfilefail%s.jpg" %fail1)
    #             sleep(2)
    #     if fail1 !=0:
    #         raise Exception("发送失败%s；" %fail1)
    #
    # def test_chat23(self):
    #     '''二人会话批量选择10个文件，点击发送'''
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     self.driver.js(FileJS)
    #     sleep(1)
    #     self.Chat.click_main_chat_filebutton()
    #     sleep(3)
    #     os.system("D:\\Actoma_autotest\\batches_upfile.exe")
    #     sleep(3)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #     file_title = FILE + " "+ self.Chat.main_display_area_lastfile_name()
    #     sleep(4)
    #     self.driver.assert_equal(file_title,self.Chat.main_messagelist_first_newmessage())
    #
    # def test_chat24(self):
    #     '''发送超过文件，toast提示：不能插入超过10个文件'''
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     self.driver.js(FileJS)
    #     sleep(1)
    #     self.Chat.click_main_chat_filebutton()
    #     os.system("D:\\Actoma_autotest\\batches_upfile.exe")
    #     sleep(3)
    #     self.Chat.click_main_chat_filebutton()
    #     os.system("D:\\Actoma_autotest\\single_upfile.exe")
    #     sleep(1)
    #     self.Chat.wait_toastMessage_hint_isdisplay(UPLIMIT)
    #     sleep(3)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #
    # def test_chat25(self):
    #     '''文件草稿'''
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     self.driver.js(FileJS)
    #     sleep(1)
    #     self.Chat.click_main_chat_filebutton()
    #     os.system("D:\\Actoma_autotest\\single_upfile.exe")
    #     sleep(2)
    #     self.Chat.click_messagelist_to_other_list()
    #     sleep(2)
    #     self.driver.assert_equal(self.Chat.main_messagelist_draft(),DRAFT+" "+FILE)
    #
    # def test_chat26(self):
    #     '''
    #     前提：会话中必须有未下载的文件消息
    #     功能：二人文件下载,下载最新的那条未下载的文件
    #     编者：cuihong
    #     :return:
    #     '''
    #     self.Contact.click_friendlist_sendmsg(FRIEND)
    #     sleep(2)
    #     self.Chat.click_lastestfile_download()
    #     sleep(5)
    #     text1 = self.Chat.main_messagelist_first_newmessage()
    #     text2= "[文件] "+ self.Chat.main_display_area_lastfile_name()
    #     self.driver.assert_equal(text1,text2)
    #
    # def test_chat28(self):
    #     '''群组会话通过文件入口发送一个文件'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     fail1 = 0
    #     self.driver.js(FileJS)
    #     self.Chat.click_main_chat_filebutton()
    #     sleep(1)
    #     os.system("D:\\Actoma_autotest\\single_upfile.exe")
    #     sleep(1)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #     file_title = FILE + " " + self.Chat.main_display_area_lastfile_name()
    #     sleep(4)
    #     try:
    #         self.driver.assert_equal(file_title, self.Chat.main_messagelist_first_newmessage())
    #     except:
    #         fail1 = fail1 + 1
    #         self.driver.get_screenshot("test_chat28_sendfilefail%s.jpg" % fail1)
    #         sleep(2)
    #     if fail1 != 0:
    #         raise Exception("群组文件发送失败%s；" % fail1)
    #
    # def test_chat29(self):
    #     '''群组会话通过文件入口发送图片'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     self.driver.js(FileJS)
    #     self.Chat.click_main_chat_filebutton()
    #     sleep(1)
    #     os.system("D:\\Actoma_autotest\\single_uppicture.exe")
    #     sleep(1)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(2)
    #     text1 = self.Chat.main_messagelist_first_newmessage()
    #     sleep(1)
    #     self.driver.assert_equal(text1, PICTURE)
    #
    # def test_chat30(self):
    #     '''群组会话发送多个文件'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     fail1 = 0
    #     self.driver.js(FileJS)
    #     for i in range(0, FRIEND_FILE_NUM):
    #         self.Chat.click_main_chat_filebutton()
    #         sleep(1)
    #         os.system("D:\\Actoma_autotest\\single_upfile.exe")
    #         sleep(1)
    #         self.Chat.shortcuts_main_chat_send()
    #         sleep(3)
    #         file_title = FILE + " " + self.Chat.main_display_area_lastfile_name()
    #         sleep(4)
    #         try:
    #             self.driver.assert_equal(file_title, self.Chat.main_messagelist_first_newmessage())
    #         except:
    #             fail1 = fail1+1
    #             self.driver.get_screenshot("test_chat28_sendfilefail%s.jpg" %fail1)
    #             sleep(2)
    #     if fail1 != 0:
    #         raise Exception("群组文件发送失败%s；" % fail1)
    #
    # def test_chat31(self):
    #     '''群组会话编辑框铺入超过10个文件，toast提示：不能插入超过10个文件'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     self.driver.js(FileJS)
    #     sleep(1)
    #     self.Chat.click_main_chat_filebutton()
    #     os.system("D:\\Actoma_autotest\\batches_upfile.exe")
    #     sleep(3)
    #     self.Chat.click_main_chat_filebutton()
    #     os.system("D:\\Actoma_autotest\\single_upfile.exe")
    #     sleep(1)
    #     self.Chat.wait_toastMessage_hint_isdisplay(UPLIMIT)
    #     sleep(3)
    #     self.Chat.shortcuts_main_chat_send()
    #     sleep(3)
    #
    # def test_chat32(self):
    #     '''群组会话的编辑框放入一个文件，切换会话，查看草稿显示'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     self.driver.js(FileJS)
    #     sleep(1)
    #     self.Chat.click_main_chat_filebutton()
    #     os.system("D:\\Actoma_autotest\\single_upfile.exe")
    #     sleep(2)
    #     self.Chat.click_messagelist_to_other_list()
    #     sleep(2)
    #     self.driver.assert_equal(self.Chat.main_messagelist_draft(), DRAFT + " " + FILE)
    #
    # def test_chat33(self):
    #     '''群组会话下载最后一条未下载文件'''
    #     self.Contact.click_grouplist(GROUP_PIC)
    #     sleep(2)
    #     self.Chat.click_lastestfile_download()
    #     sleep(5)
    #     text1 = self.Chat.main_messagelist_first_newmessage()
    #     text2 = "小锦rgh : [文件] " + self.Chat.main_display_area_lastfile_name()
    #     self.driver.assert_equal(text1, text2)


    def test_chat34(self):
        '''2人聊天选择一个好友，测试文件发送-----以常规点击文件入口的方式'''
        self.Login.login(account, password)
        a = random.randint(112,10000)#替换为文件au3
        text = TEST + str(a)
        self.Contact.click_friendlist_sendmsg(FRIEND)#FRIEND好友id 进入与好友的聊天页面
        sleep(2)
        self.Chat.input_main_chat_inputbox(text)#输入文本
        sleep(2)
        self.Chat.shortcuts_main_chat_send()#发送
        sleep(1)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)#断言

    def test_chat35(self):
        '''文件传输助手，聊天列表点击置顶'''
        self.Login.login(account, password)#登录模组
        # #     sleep(5)
        #在联系人好友列表中选择文件传输助手并点击进入会话
        self.Contact.click_contactlist_antonglist(Text_File_transfer_assistant)
        self.Contact.click_main_friend_detal_dialog_enter()
        #在消息列表中右击后选择置顶聊天
        self.Chat.context_click_main_messagelist_groupname(Text_File_transfer_assistant, self.driver.driver,
                                                           self.Chat.CONTEXT_CLICK_OPTION_TOPPING)
        #判断是否置顶
        sleep(3)
        self.driver.assert_true(self.Chat.main_messagelist_groupname_issticky(Text_File_transfer_assistant))


    def test_chat36(self):
        '''文件传输助手，聊天列表中群取消置顶'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(Text_File_transfer_assistant)
        self.Contact.click_main_friend_detal_dialog_enter()
        # 在消息列表中右击后选择置顶聊天
        self.Chat.context_click_main_messagelist_groupname(Text_File_transfer_assistant, self.driver.driver,
                                                           self.Chat.CONTEXT_CLICK_OPTION_NOTTOPPING)
        # 判断是否置顶
        sleep(3)
        self.driver.assert_false(self.Chat.main_messagelist_groupname_issticky(Text_File_transfer_assistant))

    def test_chat37(self):
        '''文件传输助手，删除会话'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(Text_File_transfer_assistant)
        self.Contact.click_main_friend_detal_dialog_enter()
        # 在消息列表中右击后选择
        self.Chat.context_click_main_messagelist_groupname(Text_File_transfer_assistant, self.driver.driver,
                                                           self.Chat.CONTEXT_CLICK_OPTION_DELDETE)
        # 判断是否删除
        sleep(3)
        self.driver.assert_false(self.Chat.main_messagelist_isaccountname(Text_File_transfer_assistant))

    def test_caht38(self):
        '''文件传输助手，清空聊天记录'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(Text_File_transfer_assistant)
        self.Contact.click_main_friend_detal_dialog_enter()
        # 在消息列表中右击后选择
        self.Chat.context_click_main_messagelist_groupname(Text_File_transfer_assistant, self.driver.driver,
                                                              self.Chat.CONTEXT_CLICK_OPTION_CLEAR)
        self.Chat.click_determine()
        # 判断在消息列表中该会话的摘要为空
        sleep(3)
        self.driver.assert_false(self.Chat.main_messagelist_groupname_isabstract(Text_File_transfer_assistant))

    def test_chat38(self):
        '''文件传输助手发送文本消息'''
        a = random.randint(100,1000)
        text = TEST + str(a)

        self.Contact.click_contactlist_antonglist(Text_File_transfer_assistant)
        self.Contact.click_main_friend_detal_dialog_enter()
        self.Chat.input_main_chat_inputbox(text)#输入文本
        sleep(3)
        self.Chat.click_main_chat_sendbutton()#发送
        sleep(3)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)

    Emoji = "[emoji_001]"
    # def test_chat39(self):
    #     '''文件传输助手发送表情消息'''
    #     self.Login.login(account, password)  # 登录模组
    #     a = random.randint(100,1000)
    #     text = TEST + str(a)+self.Emoji
    #
    #     self.Contact.click_contactlist_antonglist(Text_File_transfer_assistant)
    #     self.Contact.click_main_friend_detal_dialog_enter()
    #     self.Chat.input_main_chat_inputbox(text)#输入文本
    #     sleep(3)
    #     self.Chat.click_main_chat_sendbutton()#发送
    #     sleep(3)
    #     print(self.Chat.main_messagelist_first_newmessage())
    #     self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),text)
    #消息列表中的表情为图片，目前没有想到解决方法---------hang in the air

    def test_chat40(self):
        '''一对一消息删除聊天记录'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        self.Chat.context_click_main_messagelist_groupname(FRIEND,self.driver.driver,
                                                           self.Chat.CONTEXT_CLICK_OPTION_DELDETE)
        #断言消息列表中是否存在该会话
        self.driver.assert_false(self.Chat.main_messagelist_isaccountname(FRIEND))

    def test_chat41(self):
        '''开启消息免打扰,在消息列表中右击'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        self.Chat.context_click_main_messagelist_groupname(FRIEND,self.driver.driver,
                                                           self.Chat.CONTEXT_CLICL_OPTION_NODISTURB)
        #检查该会话中是否有免打扰图标
        self.driver.assert_true(self.Chat.main_messagelist_conversation_nodisturb(FRIEND))

    def test_chat42(self):
        '''关闭消息免打扰，在消息列表中'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        self.Chat.context_click_main_messagelist_groupname(FRIEND,self.driver.driver,
                                                           self.Chat.CONTEXT_CLICK_OPTION_DISTURB)
        self.driver.assert_false(self.Chat.main_messagelist_conversation_nodisturb(FRIEND))

    def test_chat43(self):
        '''删除最后一条发送会话消息'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        a = random.randint(100, 1000)
        text1 = TEST + str(a)
        a = random.randint(1,100)
        text2 = TEST + str(a)


        self.Contact.click_friendlist_sendmsg(FRIEND)
        self.Chat.input_main_chat_inputbox(text1)  # 输入文本
        sleep(3)
        self.Chat.click_main_chat_sendbutton()  # 发送
        self.Contact.click_friendlist_sendmsg(FRIEND)
        self.Chat.input_main_chat_inputbox(text2)  # 输入文本
        sleep(3)
        self.Chat.click_main_chat_sendbutton()  # 发送
        sleep(2)
        #删除最后一条消息
        self.Chat.main_chat_senf_messageinfo_last_delete(self.driver.driver)
        #断言最后一条消息的内容
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(), text1)

    def test_chat44(self):
        '''删除最后一条接收会话消息'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        '''读取最后一条消息，执行删除操作后，判断最后一条消息不是之前的消息即可
            存在bug：最后两条消息的内容一致，会报错
        '''
        received_text = self.Chat.main_chat_receive_messageinfo_text()
        self.Chat.main_chat_receive_messageinfo_last_delete(self.driver.driver)

        self.driver.assert_not_equal(received_text,self.Chat.main_chat_receive_messageinfo_text())

    # def test_chat45(self):
    #     '''被撤回消息'''
    #     self.Login.login(account, password)  # 登录模组
    #     self.Contact.click_contactlist_antonglist(FRIEND)
    #     self.Contact.click_main_friend_details_sendmessage()
    #     sleep(2)
    #     messagetext = self.Chat.mian_chat_messagelist_last_text()
    #     print(messagetext)
    #     withdraw_message_text = FRIEND+' '+Text_Friend_retraction_message
    #     self.driver.assert_equal(messagetext,withdraw_message_text)

    def test_chat46(self):
        '''文件管理中的图片'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_FileManagement(self.driver.driver)
        sleep(3)
        self.Chat.click_chat_Filemanagement_TimeDivide_top1()
        sleep(3)
        self.Chat.click_chat_FileManagement_imglist_01()
        sleep(5)

    def test_chat47(self):
        '''文件管理中删除图片'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_FileManagement(self.driver.driver)
        sleep(3)
        self.Chat.click_chat_Filemanagement_TimeDivide_top1()
        sleep(3)
        self.Chat.context_click_chat_Filemanagement_imglist_01(self.driver.driver)
        sleep(3)

    # def test_chat48(self):
    #     '''文件管理中下载文件'''
    #     self.Login.login(account, password)  # 登录模组
    #     self.Contact.click_contactlist_antonglist(FRIEND)
    #     self.Contact.click_main_friend_details_sendmessage()
    #     sleep(2)
    #     self.Chat.click_chat_FileManagement(self.driver.driver)
    #     sleep(3)
    #     #点击文件选项
    #     self.Chat.click_chat_FileManagement_File()
    #     sleep(1)
    #     self.Chat.click_chat_FileManagement_File_TimeDivide_top1()
    #     sleep(1)
    #     self.Chat.context_click_chat_FileManagement_File_TimeDivide_top1_file1(self.driver.driver)
    #     sleep(2)
    #     self.Chat.click_download()
    #     sleep(3)
    #     #断言
    #     tomp = True
    #     try:
    #         self.driver.assert_true(self.Chat.is_FileManagement_file_top1_download())
    #     except:
    #         pass
    #         print("文件开始下载失败")
    #         tomp = False


    def test_chat49(self):
        '''在设置中点击置顶聊天'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_setting(self.driver.driver)
        sleep(3)
        self.Chat.click_setting_top_chat_button()
        #断言
        self.driver.assert_true(self.Chat.main_messagelist_groupname_issticky(FRIEND))

    def test_chat50(self):
        '''点击设置中取消置顶'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_setting(self.driver.driver)#使用webdriver来操作元素
        sleep(2)
        self.Chat.clicj_setting_nottop_chat_button()
        sleep(2)#此处加等待原因不明，不加等待会导致元素不可见异常
        #断言
        self.driver.assert_false(self.Chat.main_messagelist_groupname_issticky(FRIEND))

    def test_chat51(self):
        ''' 在设置中点击消息免打扰'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_setting(self.driver.driver)
        sleep(2)
        self.Chat.click_setting_dontDisturb_button()
        sleep(2)
        self.driver.assert_true(self.Chat.main_messagelist_conversation_nodisturb(FRIEND))

    def test_chat52(self):
        '''在设置中点击消息免打扰按钮关闭消息免打扰'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_setting(self.driver.driver)
        sleep(2)
        self.Chat.click_setting_NotDonnotDisturb_button()
        sleep(2)
        self.driver.assert_false(self.Chat.main_messagelist_conversation_nodisturb(FRIEND))

    text_add_Members_apge = "已选中 0 个联系人"

    def test_chat53(self):
        '''添加成员'''
        self.Login.login(account, password)  # 登录模组
        self.Contact.click_contactlist_antonglist(FRIEND)
        self.Contact.click_main_friend_details_sendmessage()
        sleep(2)
        self.Chat.click_chat_setting(self.driver.driver)
        sleep(2)
        self.Chat.click_setting_add_Members_buttom()
        sleep(2)
        self.driver.assert_equal(self.Chat.get_setting_add_Members(),self.text_add_Members_apge)

    #注释，该用例会影响其他操作
    # def test_chat54(self):
    #     '''清空聊天记录'''
    #     '''清空聊天记录，则会话摘要为空'''
    #     self.Login.login(account, password)  # 登录模组
    #     self.Contact.click_contactlist_antonglist(FRIEND)
    #     self.Contact.click_main_friend_details_sendmessage()
    #     sleep(2)
    #     self.Chat.click_chat_setting(self.driver.driver)
    #     sleep(2)
    #     self.Chat.click_setting_close_button()
    #     sleep(3)
    #     #点击确定
    #     self.Chat.click_determine()
    #     sleep(2)
    #     #断言，判断该会话摘要是否为空
    #     self.driver.assert_false(self.Chat.main_messagelist_groupname_isabstract(FRIEND))

    # def test_chat55(self):
    #     '''右击文件管理中的图片'''





    if __name__=="__main__":
     pytest.main("-v chat_test.py::TestChat").l;