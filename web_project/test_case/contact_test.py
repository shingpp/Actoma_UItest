from time import sleep
import pytest,sys,random,time

from web_project.public.myunit import MyTest
# from ..public.myunit import MyTest

myNickname = "xxj111"
myNickname = "test"
# friendAccount = "xuxiaojing5"                    #好友帐号，有昵称，无备注
# friendAccountNickname="xiaoxu"                    #好友的昵称
friendAccount = "5051183"                    #好友帐号，有昵称，无备注
friendAccountNickname="啊呀呀"                    #好友的昵称
# NotFriend = "5075754"
# NotFriendNickname = "小图"
NotFriend = "5188850"
aNotFriend="帐号：5188850"
friendRemark = "测试备注info1"                   #好友备注
clearFriendRemark = ""                            #清空好友备注
addFriendtext ="添加好友测试"                     #添加好友的好友请求
newFriendPagetext = "新好友"                      #新好友页面顶部内容
# ownAccount = "xxj111"                             #自己的账号
ownAccount = "5075754"                             #自己的账号
accountErr = "sdfsdfsdfsd1222"                   #不存在的账号
accountInformationNoExist = "没有搜索到帐号信息"  #帐号信息不存在
createGroup = "正在发起群聊…"                    #创建群组
# groupnameOld="xxj111、大太123、jjj001"                #群组名称
groupnameOld="小图、啊啊啊、啊呀呀"                #群组名称
groupnameNew = "群名称修改为自动化测试哈哈哈"        #修改后的群名称
groupnameChangeSuc = "修改成功"                       #修改群组名称成功
comeGroupOpentext = "群主已启用“群主确认进群”，群成员需群主确认才能进群"         #群主确认进群开启提醒
comeGroupClosetext = "群主已恢复默认进群方式"                                        #群主确认进群关闭提醒
exitAndDismissGroupBtn = "退出群组"                               #退出并解散群组按钮
exitAndDismissGrouptoast = "解散群组，所有成员将无法收发聊天消息"                      #退出并解散群组toast提示
exitAndDismissGrouptoastMsg = "正在解散群组…"                      #确认解散并退出群组后toast提示
exitAndDismissGroupSuc = "解散群组成功"                      #确认解散并退出群组后toast提示
groupAddressBooktext = "集团通讯录"                          #集团通讯录页面的顶部信息
groupAddressBooks = "Test_A"                                  #集团通讯录的根目录
groupAddressBook = "TestB"                                  #集团通讯录的根目录
groupAddressBookName = "autoTest"                           #集团通讯录中的人员
friendRequestToastMsg = "正在发送好友请求"                      #发送好友请求提示
newFriendVerifyName = "自动化"                            #集团通讯录发送好友请求后的账户验证信息
SENDTEXT ="安通+测试消息Send"
groupmanager_permissionTransferSuc = "转让成功"

PictureJS = "document.querySelector('#testPictureBtn').style.width = '19px'"

class TestContact(MyTest):
    '''
    联系人页面测试，包含好友、群组和集团通讯录
    '''

    # @pytest.mark.skip
    def test_contact01(self):
        '''联系人--好友列表点击“安通+团队”'''
        # text = "团队"#后续版本中该值该为安通⁺团队
        text = "安通⁺团队"
        link = "芯片管家是什么？"
        self.Contact.enter_to_chat_page()
        sleep(2) 
        self.Contact.click_contactlist_antonglist(text)
        sleep(2)
        # js="var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)
        self.Contact.click_main_friend_detal_dialog_enter()
        sleep(2)
        self.driver.assert_in(text,self.Chat.main_chat_Actoma_title_text())
        sleep(8)
        # target = self.driver.find_element_by_xpath("//div[@class='msg-type-text msg-type-text-left not-handle-link ng-binding selectable-at']")
        # target = self.driver.find_element_by_class_name("msg-type-text-left']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
        # sleep(2)
        self.Chat.click_main_chat_Actoma_WhatIsActoma(link)
        sleep(2)
        # handles = self.driver.window_handles
        # mainhandle = self.driver.current_window_handle
        # self.driver.switch_to.window(handles[2])
        # sleep(1)
        # self.driver.assert_equal(self.Chat.newwindows_whatisActoma_title_text(),link)
        # sleep(2)

    # @pytest.mark.flaky(reruns=2)
    def test_contact02(self):
        '''添加好友，输入存在的账号查找，并发送好友请求'''
        addFriendtext ="添加好友测试"
        a = random.randint(1000,10000)
        addFriendtext = addFriendtext + str(a)

        self.Contact.enter_to_chat_page()
        sleep(2)
        self.Contact.add_or_search_friend(NotFriend)
        sleep(3)
        self.driver.assert_equal(self.Contact.main_friend_detal_dialog_head_text(),aNotFriend)
        # self.Contact.click_main_friend_detal_dialog_addfriend()
        # sleep(2)
        # self.Contact.click_main_friend_detal_dialog_addfriend_inputbox_deletebutton()
        # sleep(1)
        # self.Contact.input_main_friend_detal_dialog_addfriend_inputbox(addFriendtext)
        # sleep(1)
        # self.Contact.click_main_friend_detal_dialog_addfriend_sendbutton()
        # self.Chat.wait_toastMessage_hint_isdisplay("正在发送好友请求")
        # sleep(5)
        # #新好友中存在已加好友正在等待验证等一些信息
        # self.Contact.click_main_contactlist_newfriend()
        # sleep(3)
        # self.driver.assert_equal(self.Contact.main_contactlist_newfriend_title_text(),newFriendPagetext)
        # sleep(2)
        # self.driver.assert_equal(self.Contact.main_messagelist_newfriend_row_account_text(0),NotFriend)
        # sleep(1)
        # self.driver.assert_equal(self.Contact.main_messagelist_newfriend_row_verifyinfo_text(0),addFriendtext)

    def test_contact03(self):
        '''添加好友，输入自己的账号查找，页面出现提示'''
        self.Contact.enter_to_chat_page()
        sleep(2)
        self.Contact.add_or_search_friend(ownAccount)
        self.Chat.wait_toastMessage_hint_isdisplay("不支持搜索自己")

    def test_contact04(self):
        '''添加好友，输入不存在的帐号查找，页面出现提示'''
        self.Contact.enter_to_chat_page()
        sleep(2)
        self.Contact.add_or_search_friend(accountErr)
        self.Chat.wait_toastMessage_hint_isdisplay(accountInformationNoExist)

    def test_contact05(self):
        '''查看好友详情,无备注信息好友'''
        self.Contact.enter_to_chat_page()
        sleep(2)
        self.Contact.add_or_search_friend(friendAccount)
        sleep(3)
        self.driver.assert_equal("昵   称："+self.Contact.main_friend_detal_dialog_head_text(),self.Contact.main_friend_detal_dialog_nickname_text())

    def test_contact06(self):
        '''查看好友详情,没有备注信息好友，添加备注'''
        self.Contact.enter_to_chat_page()
        sleep(2)
        self.Contact.add_or_search_friend(friendAccount)
        sleep(3)
        self.Contact.click_main_friend_detal_dialog_comment_editbutton()
        sleep(2)
        self.Contact.input_main_friend_detal_dialog_comment_edit_inputbox(friendRemark)
        sleep(2)
        self.Contact.click_main_friend_detal_dialog_comment_edit_OKbutton()
        sleep(2)
        self.driver.assert_equal(self.Contact.main_friend_detal_dialog_comment_text(), self.Contact.main_friend_detal_dialog_head_text())

    def test_contact07(self):
        '''查看好友详情,有备注信息好友，清空备注'''
        self.Contact.enter_to_chat_page()
        sleep(2)
        self.Contact.add_or_search_friend(friendAccount)
        sleep(3)
        self.driver.assert_equal(self.Contact.main_friend_detal_dialog_comment_text(),self.Contact.main_friend_detal_dialog_head_text())
        sleep(1)
        self.Contact.click_main_friend_detal_dialog_comment_editbutton()
        sleep(2)
        self.Contact.input_main_friend_detal_dialog_comment_edit_inputbox(clearFriendRemark)
        sleep(2)
        self.Contact.click_main_friend_detal_dialog_comment_edit_OKbutton()
        sleep(4)
        self.driver.assert_equal("昵   称："+self.Contact.main_friend_detal_dialog_head_text(),self.Contact.main_friend_detal_dialog_nickname_text())

    def test_contact08(self):
        '''创建群组成功'''
        #勾选几个好友
        N= 2
        friend=[]

        self.Contact.create_group()
        sleep(2)
        #勾选第1,2个好友，并返回第1,2个好友的昵称
        for i in range(0,N):
            #勾选并返回名称
            friend.append(self.Contact.check_main_newgroup_checkbox_returnfriendname(i))
            sleep(2)
            self.driver.assert_equal(self.Contact.main_newgroup_friendname_text(-1),friend[i])
            self.driver.assert_equal(self.Contact.main_newgroup_sidetoptext(),"已选中%s个联系人"%str(i+1))
        self.Contact.click_main_newgroup_OKbutton()
        self.Chat.wait_toastMessage_hint_isdisplay(createGroup)
        sleep(10)
        #发起群聊成功后，验证聊天页面的标题信息正确
        self.driver.assert_equal(self.Chat.main_group_me_chat_head_text(),"%s、%s、%s(%s人)" %(myNickname,friend[0],friend[1],str(N+1)))

    def test_contact09(self):
        ''' 修改群名称'''

        self.Contact.click_grouplist(groupnameOld)
        sleep(3)
        self.Chat.click_main_groupchat_settingsbutton()
        sleep(2)
        self.Chat.click_main_groupsetting_GroupNameButton()
        sleep(2)
        self.Chat.main_groupSetting_GroupNameEditButton_inputbox(groupnameNew)
        sleep(2)
        self.Chat.main_groupSetting_GroupNameEdit_OKButton()
        self.Chat.wait_toastMessage_hint_isdisplay(groupnameChangeSuc)

    def test_contact10(self):
        "群主确认进群开启"
        self.Login.login()
        self.Chat.click_main_messagelist_groupname(groupnameNew)
        sleep(2)
        self.Chat.click_main_groupchat_settingsbutton()
        sleep(2)
        self.Chat.main_groupsetting_groupmanagerButton()
        sleep(2)
        self.Chat.main_groupsetting_groupmanager_onButton()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_messagelist_message(0),comeGroupOpentext)

    def test_contact11(self):
        "群主确认进群关闭"
        self.Login.login()
        self.Chat.click_main_messagelist_groupname(groupnameNew)
        sleep(2)
        self.Chat.click_main_groupchat_settingsbutton()
        sleep(2)
        self.Chat.main_groupsetting_groupmanagerButton()
        sleep(2)
        self.Chat.main_groupsetting_groupmanager_offButton()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_messagelist_message(0),comeGroupClosetext)

    def test_contact12(self):
        "群主管理权转让"
        self.Login.login()
        sleep(2)
        self.Chat.click_main_messagelist_groupname(groupnameNew)
        sleep(2)
        self.Chat.click_main_groupchat_settingsbutton()
        sleep(2)
        self.Chat.main_groupsetting_groupmanagerButton()
        sleep(2)
        self.Chat.main_groupsetting_groupmanager_permissionTransferButton()
        sleep(5)
        self.Chat.main_groupsetting_newgroupmanagerSelectionbutton(-1)
        sleep(3)
        groupSetting = self.Chat.main_groupsetting_newgroupmanagerSelection_text(-1)
        sleep(3)
        self.Chat.main_newgroupmanagerSelectionOkbutton()
        sleep(2)
        self.Chat.wait_toastMessage_hint_isdisplay(groupmanager_permissionTransferSuc)
        sleep(2)
        self.driver.assert_in(groupSetting,self.Chat.main_messagelist_message(0))
        # self.driver.assert_equal(self.Chat.main_messagelist_message(0),"徐娃哈哈 已成为新群主")

    def test_contact13(self):
        '''解散或退出群组'''
        self.Login.login()
        self.Chat.click_main_messagelist_groupname(groupnameNew)
        sleep(3)
        self.driver.assert_equal(self.Chat.main_group_me_chat_head_text(),"%s(3人)" %groupnameNew)
        self.Chat.click_main_groupchat_settingsbutton()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_groupchat_settings_quitgroupbutton_text(),exitAndDismissGroupBtn)
        self.Chat.click_main_groupchat_settings_quitgroupbutton()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_ungroup_hint_text(),exitAndDismissGrouptoast)
        self.Chat.click_main_ungroup_hint_okbutton()
        self.Chat.wait_toastMessage_hint_isdisplay(exitAndDismissGrouptoastMsg)
        self.Chat.wait_toastMessage_hint_isdisplay(exitAndDismissGroupSuc)

    def test_contact14(self):
        '''新建群组时，查询好友,查询到好友,支持模糊搜索'''
        self.Contact.create_group()
        sleep(2)
        self.Contact.input_main_newgroup_searchbox(friendAccountNickname)
        sleep(8)
        self.driver.assert_equal(self.Contact.main_newgroup_searchresult_text(friendAccountNickname),"true")

    def test_contact15(self):
        '''新建群组时，查询好友,查询不到好友'''

        self.Contact.create_group()
        sleep(2)
        self.Contact.input_main_newgroup_searchbox(accountErr)
        sleep(2)
        try:
            self.Contact.main_newgroup_friendname_text(0)
            self.driver.fail("查询到了好友")
        except:
            sleep(3)

    def test_contact16(self):
        '''进入集团通讯录页面发送好友请求'''
        self.Contact.Select_person(groupAddressBookName, groupAddressBooks, groupAddressBook)
        sleep(2)
        self.Contact.click_main_friend_detal_dialog_addfriend()
        sleep(2)
        self.Contact.click_main_friend_detal_dialog_addfriend_inputbox_deletebutton()
        sleep(1)
        self.Contact.input_main_friend_detal_dialog_addfriend_inputbox(addFriendtext)
        sleep(1)
        self.Contact.click_main_friend_detal_dialog_addfriend_sendbutton()
        self.Chat.wait_toastMessage_hint_isdisplay(friendRequestToastMsg)
        sleep(5)

        # 新好友中存在已加好友正在等待验证等一些信息
        self.Contact.click_main_contactlist_newfriend()
        sleep(3)
        self.driver.assert_equal(self.Contact.main_contactlist_newfriend_title_text(), newFriendPagetext)
        sleep(2)
        self.driver.assert_equal(self.Contact.main_messagelist_newfriend_row_account_text(0), newFriendVerifyName)
        sleep(1)
        self.driver.assert_equal(self.Contact.main_messagelist_newfriend_row_verifyinfo_text(0), addFriendtext)

    def test_contact17(self):
        '''进入集团通讯录页面发送加密消息'''
        a = random.randint(1000,10000)
        sendtext = SENDTEXT +str(a)

        self.Contact.Select_person(groupAddressBookName,groupAddressBooks,groupAddressBook)
        sleep(2)
        self.Contact.click_main_friend_detal_dialog_sendEnmessage()
        sleep(2)
        self.driver.assert_equal(self.Chat.main_chat_head_name_text(),groupAddressBookName)
        sleep(1)
        self.Chat.input_main_chat_inputbox(sendtext)
        sleep(3)
        # ma.click_main_chat_sendbutton()
        sleep(1)
        self.Chat.shortcuts_main_chat_send()
        self.driver.assert_equal(self.Chat.main_chat_send_messageinfo_text(),sendtext)
        sleep(3)
        self.driver.assert_equal(self.Chat.main_messagelist_first_newmessage(),sendtext)

if __name__ == "__main__":
    pytest.main("-v contact_test.py::TestContact::test_contact17")
