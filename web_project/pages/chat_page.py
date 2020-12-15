# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from .base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import traceback
from selenium.webdriver.common.action_chains import ActionChains

class Chat(Page):
    '''
    聊天首页
    '''



    #头像区域显示当前账号
    main_currentUser_account_loc = "class=>name"
    def main_currentUser_account_text(self):
        return self.driver.get_text(self.main_currentUser_account_loc)

    #左侧边栏消息
    main_menu_message_loc = "class=>at-menu-message"
    def click_main_menu_message(self):
        self.driver.click(self.main_menu_message_loc)
    def main_menu_message_attribute(self,attribute):
        self.driver.get_attribute(self.main_menu_message_loc,attribute)

    #创建群聊成功后，群聊聊天对话中的title信息
    main_group_me_chat_head_loc="//p[@class='head-title conv-title']/span"
    main_group_me_chat_head_num_loc="//p[@class='head-title conv-title']/span[2]"
    def main_group_me_chat_head_text(self):
        return self.driver.get_text(self.main_group_me_chat_head_loc)+self.driver.get_text(self.main_group_me_chat_head_num_loc)

    #聊天对话中的头名称
    main_chat_head_name_loc= "class=>chat-head-name"
    def main_chat_head_name_text(self):
        return self.driver.get_text(self.main_chat_head_name_loc)

    #群组聊天对话中的设置按钮
    main_groupchat_settingsbutton_loc = "class=>group-setting-btn-list"
    def click_main_groupchat_settingsbutton(self):
        self.driver.click(self.main_groupchat_settingsbutton_loc)

    #群组设置中的群名称按钮
    main_groupsetting_GroupNameButton_loc = "//div[@ng-show='!isShowGroupName']/span[2]"
    def click_main_groupsetting_GroupNameButton(self):
        self.driver.click(self.main_groupsetting_GroupNameButton_loc)

    # 群组设置---编辑群名称
    main_groupSetting_GroupNameEditButton_loc = "//input[@ng-model='curGroup.group_name']"
    def main_groupSetting_GroupNameEditButton_inputbox(self,text):
        self.driver.clear(self.main_groupSetting_GroupNameEditButton_loc)
        sleep(1)
        self.driver.input(self.main_groupSetting_GroupNameEditButton_loc,text)
    def main_groupSetting_GroupNameEdit_OKButton(self):
        self.driver.input(self.main_groupSetting_GroupNameEditButton_loc,Keys.ENTER)

    # 群组设置--群管理
    main_groupsetting_groupmanagerButton_loc = "//div[@ng-if='curGroup.owner == currentUser.account && curGroup.member.length > 2']/div[2]"
    def main_groupsetting_groupmanagerButton(self):
        self.driver.click(self.main_groupsetting_groupmanagerButton_loc)

    # 群组设置--群管理---群主确认进群开启
    main_groupsetting_groupmanager_onButton_loc = "//div[@ng-show='curGroup.MFlag == 0']"
    def main_groupsetting_groupmanager_onButton(self):
        self.driver.click(self.main_groupsetting_groupmanager_onButton_loc)
    # 群组设置--群管理---群主确认进群关闭
    main_groupsetting_groupmanager_offButton_loc = "//div[@ng-show='curGroup.MFlag == 1']"
    def main_groupsetting_groupmanager_offButton(self):
        self.driver.click(self.main_groupsetting_groupmanager_offButton_loc)
    #群组设置--群管理---群主管理权转让
    main_groupsetting_groupmanager_permissionTransfer_loc = "//div[@ng-click='openGroupMembers()']"
    def main_groupsetting_groupmanager_permissionTransferButton(self):
        self.driver.click(self.main_groupsetting_groupmanager_permissionTransfer_loc)
    # 群主管理权转让--新群主
    main_groupsetting_newgroupmanagerSelection_loc = "class=>side-bottom-item"
    main_groupsetting_newgroupmanagerSelection_text_loc = "class=>select-member-name"
    def main_groupsetting_newgroupmanagerSelectionbutton(self,number):
        elements = self.driver.get_elements(self.main_groupsetting_newgroupmanagerSelection_loc)
        self.driver.click(elements[number])
    def main_groupsetting_newgroupmanagerSelection_text(self,number):
        elements = self.driver.get_elements(self.main_groupsetting_newgroupmanagerSelection_text_loc)
        # return elements[number].text
        # print(elements)
        A1 = self.driver.get_text(elements[number])
        # print(A1)
        return A1

    #  转让群主提示框
    main_newgroupmanagerSelection_hint_text_loc = "//button[@class='dialog-content-child ng-binding ng-scope']"
    main_newgroupmanagerSelectionOkbutton_loc = "//button[@class='btn-confirm btn-large ng-binding ng-scope']"
    main_newgroupmanagerSelectioncancelbutton_loc = "//button[@class='btn-cancel btn-large ng-binding ng-scope']"
    def main_newgroupmanagerSelection_hint_text(self):
        return self.driver.get_text(self.main_newgroupmanagerSelection_hint_text_loc)
    def main_newgroupmanagerSelectionOkbutton(self):
        self.driver.click(self.main_newgroupmanagerSelectionOkbutton_loc)
    def main_newgroupmanagerSelectioncancelbutton_loc(self):
        self.driver.click(self.main_newgroupmanagerSelectioncancelbutton_loc)

    #清空聊天记录
    main_clear_chat_record_loc = "class=>btn-confirm"
    def main_clear_chat_record(self):
        self.driver.click(self.main_clear_chat_record_loc)

    # 群组设置关闭按钮
    main_groupsetting_offButton_loc = "class=>head-btn"
    def main_groupsetting_offButton(self):
        self.driver.click(self.main_groupsetting_offButton_loc)

    #群组聊天对话中设置里面的退出并解散群
    main_groupchat_settings_quitgroupbutton_loc = "//button[@class='btn-cancel btn-large']"
    def click_main_groupchat_settings_quitgroupbutton(self):
        self.driver.click(self.main_groupchat_settings_quitgroupbutton_loc)
    def main_groupchat_settings_quitgroupbutton_text(self):
        return self.driver.get_text(self.main_groupchat_settings_quitgroupbutton_loc)

    #解散群组的提示信息
    main_ungroup_hint_text_loc= "class=>dialog-content-child"
    main_ungroup_hint_okbutton_loc= "//button[@class='btn-confirm btn-large ng-binding ng-scope']"
    main_ungroup_hint_cancelbutton_loc= "//button[@class='btn-cancel btn-large ng-binding ng-scope']"
    def main_ungroup_hint_text(self):
        return self.driver.get_text(self.main_ungroup_hint_text_loc)#定位到群组的清空会话按钮
    def click_main_ungroup_hint_okbutton(self):
        self.driver.click(self.main_ungroup_hint_okbutton_loc)
    def click_main_ungroup_hint_cancelbutton(self):
        self.driver.click(self.main_ungroup_hint_cancelbutton_loc)#定位到解散群组

    #聊天对话中的输入框
    main_chat_iframe_input_loc = "class=>ke-edit-iframe" #输入框的分页面
    main_chat_inputbox_loc = "class=>ke-content" #输入框的body
    def input_main_chat_inputbox(self,chattext):
        self.driver.switch_to_frame(self.main_chat_iframe_input_loc)
        sleep(1)
        self.driver.click(self.main_chat_inputbox_loc)#点击输入框
        self.driver.clear(self.main_chat_inputbox_loc)#清空输入框
        self.driver.input(self.main_chat_inputbox_loc,chattext)#输入Chattext
        sleep(1)
        self.driver.switch_to_frame_out()

    #shortcuts发送
    def shortcuts_main_chat_send(self):
        self.driver.switch_to_frame(self.main_chat_iframe_input_loc)
        sleep(1)
        self.driver.input(self.main_chat_inputbox_loc,Keys.ENTER)
        sleep(1)
        self.driver.switch_to_frame_out()
    def shortcuts_main_chat_sendctrl(self):
        self.driver.switch_to_frame(self.main_chat_iframe_input_loc)
        sleep(1)
        self.driver.input(self.main_chat_inputbox_loc,Keys.CONTROL+Keys.ENTER)
        sleep(1)
        self.driver.switch_to_frame_out()
    #聊天对话中的发送按钮
    main_chat_sendbutton_loc = "id=>sendMsgFg"
    def click_main_chat_sendbutton(self):
        self.driver.click(self.main_chat_sendbutton_loc)

    #聊天对话中的已发送消息
    main_chat_send_messageinfo_loc= "//div[@ng-if='message.showNumFlag==1 && message.isMine']"
    # main_chat_send_messageinfo_loc= "//div[@class='msg-type-text msg-type-text-right handle-link ng-binding ng-scope selectable-at']"
    # main_chat_send_messageinfo_loc= "//div[@class='msg-type-text msg-type-text-right handle-link ng-binding ng-scope selectable-at']"
    def main_chat_send_messageinfo_text(self):
        '''返回最后一条消息内容 -发送'''
        elements = self.driver.get_elements(self.main_chat_send_messageinfo_loc)
        return elements[-1].text

    #xpath定位删除按钮
    main_chat_messageinfo_delete_loc = "link_text=>删除"
    def main_chat_senf_messageinfo_last_delete(self,web_driver):
        '''删除最后一条会话消息'''
        elements = self.driver.get_elements(self.main_chat_send_messageinfo_loc)
        ActionChains(web_driver).context_click(elements[-1]).perform()
        element = self.driver.element_wait(self.main_chat_messageinfo_delete_loc)
        element.click()

    #当前会话中最后一条接收到的消息-xpath
    main_chat_receive_messageinfo_last_loc = "//div[@class='msg-type-text msg-type-text-left not-handle-link ng-binding ng-scope selectable-at']"
    def main_chat_receive_messageinfo_last_delete(self,web_driver):
        '''删除最后接受到的消息'''
        elements = self.driver.get_elements(self.main_chat_receive_messageinfo_last_loc)
        ActionChains(web_driver).context_click(elements[-1]).perform()
        element = self.driver.element_wait(self.main_chat_messageinfo_delete_loc)
        element.click()

    def main_chat_receive_messageinfo_text(self):
        '''返回最后一条消息内容 -接受'''
        elements = self.driver.get_elements(self.main_chat_receive_messageinfo_last_loc)
        return elements[-1].text

    def main_chat_send_messageinfo_len(self):
        '''该会话中的消息数量'''
        messagetexts = self.driver.get_elemnet(self.main_chat_send_messageinfo_loc)
        return len(messagetexts)

    mian_chat_messagelist_loc = "//message[@ng-repeat='message in messages track by $index']"
    def mian_chat_messagelist_last_text(self):
        '''读取最后一条消息体中文本内容'''
        messagelist = self.driver.get_elements(self.mian_chat_messagelist_loc)
        return messagelist[-1].text

    #聊天对话框中的发送图片按钮
    # main_chat_picturebutton_loc = "id=>testPictureBtn"
    main_chat_picturebutton_loc = "id=>imgFileStyle"
    def click_main_chat_picturebutton(self):
        self.driver.click(self.main_chat_picturebutton_loc)

    #聊天对话框中的发送文件按钮
    # main_chat_filebutton_loc = "id=>testFileBtn"
    main_chat_filebutton_loc = "id=>files-file"
    def click_main_chat_filebutton(self):
        self.driver.click(self.main_chat_filebutton_loc)

    #聊天对话中已发送消息的状态
    main_chat_send_messagestate_loc= "class=>msg-state-text"
    def main_chat_send_messagestate(self,i):
        messagestates = self.driver.get_elements(self.main_chat_send_messagestate_loc)
        return self.driver.get_text(messagestates[-1])

    #输入框点击发送按钮
    # main_chat_send_message_button_loc=(By.ID,"sendMsgFg")
    main_chat_send_message_button_loc = "//li[@class='tool-item tool-item-right']/a"
    def main_chat_send_message_button(self):
        self.driver.click(self.main_chat_send_message_button_loc)

    #消息列表选中对话的聊天中最新消息摘要
    # main_messagelist_first_newmessage_loc = (By.XPATH,"//p[@class='latest-msg active']/span[@ng-bind-html='conv.lastMsg|transforLastMsg|trustHtml']")
    # main_messagelist_first_newmessage_loc = (By.XPATH,"//p[@class='latest-msg active']/span[@ng-bind-html='conv.lastMsg|transforLastMsgA:false:conv.sessionId|trustHtml']")
    main_messagelist_first_newmessage_loc = "//p[@class='latest-msg active']/span"
    def main_messagelist_first_newmessage(self):
        return self.driver.get_text(self.main_messagelist_first_newmessage_loc)

    #消息列表中点击指定二人会话的帐户,并点击进入
    main_messagelist_accountname_loc= "//p[@ng-if='conv.sessionType == 1 || conv.sessionType == 3 || conv.sessionType == 4 ']"
    def click_main_messagelist_accountname(self,name):
        accounts = self.driver.get_elements(self.main_messagelist_accountname_loc)
        found=0
        for account in accounts:
            if account.text == name:
                account.click()
                found = 1
        if found!=1:
            raise Exception("没有找到对象")

    #消息列表中查找指定账户
    def main_messagelist_accountname(self,name):
        accounts = self.driver.get_elements(self.main_messagelist_accountname_loc)
        found=0
        for account in accounts:
            if account.text == name:
                found = 1
                return ("true")
        if found!=1:
            raise Exception("没有找到对象")
    def main_messagelist_isaccountname(self,name):
        '''查找消息列表中该会话是否存在'''
        accounts = self.driver.get_elements(self.main_messagelist_accountname_loc)
        found=0
        for account in accounts:
            if account.text == name:
                found = 1
                return True
        if found!=1:
            return False

    def main_messagelist_accountname_text(self,i):
        a = self.driver.get_elements(self.main_messagelist_accountname_loc)
        return self.driver.get_text(a[i])
    # def  click_main_messagelist_accountname(self):
    #     self.find_elements(*self.main_messagelist_accountname_loc)[-1].click()

    # 消息列表中点击指定群组会话的帐户
    main_messagelist_groupname_loc = "//p[@class='name ng-binding ng-scope']"
    def click_main_messagelist_groupname(self,name):
        groupnames = self.driver.get_elements(self.main_messagelist_groupname_loc)
        found = 0
        for groupname in groupnames:
            if groupname.text == name:
                groupname.click()
                found = 1
        if found!=1:
            raise Exception("没有找到对象")

    # 消息列表中点击右击指定会话，选择操作
    main_messagelist_groupname_01_loc = "//span[@class='ng-binding ng-scope']"
    # main_message_menu_value_sticky_loc = "link_text=>置顶会话"
    # def context_click_main_messagelist_groupname(self,name,driver_web):
    #     groupnames = self.driver.get_elements(self.main_messagelist_groupname_01_loc)
    #     found = 0
    #     for groupname in groupnames:
    #         if groupname.text == name:
    #             ActionChains(driver_web).click(groupname).context_click(groupname).perform()
    #             #此时已经弹出菜单，选择置顶
    #             sleep(3)
    #             #获取菜单元素
    #             caidn = self.driver.element_wait(self.main_message_menu_value_sticky_loc)
    #             caidn.click()
    #             sleep(3)
    #
    #             found = 1
    #     if found!=1:
    #         raise Exception("没有找到对象")

    #对当前元素做取消置顶操作
    main_message_menu_value_sticky_loc_no = "link_text=>"
    # 右击菜单选项
    CONTEXT_CLICK_OPTION_TOPPING = '置顶会话'
    CONTEXT_CLICK_OPTION_NOTTOPPING = '取消置顶'
    CONTEXT_CLICK_OPTION_DELDETE = '删除会话'
    CONTEXT_CLICK_OPTION_CLEAR = '清空聊天记录' #该选项只有文件传输助手拥有
    CONTEXT_CLICL_OPTION_NODISTURB = '消息免打扰'
    CONTEXT_CLICK_OPTION_DISTURB = '开启新消息提醒'
    def context_click_main_messagelist_groupname(self,name,driver_web,option):
        groupnames = self.driver.get_elements(self.main_messagelist_groupname_01_loc)
        found = 0
        for groupname in groupnames:
            if groupname.text == name:
                ActionChains(driver_web).click(groupname).context_click(groupname).perform()
                #此时已经弹出菜单，选择
                sleep(3)
                #获取菜单元素
                try:
                    caidn = self.driver.element_wait(self.main_message_menu_value_sticky_loc_no+option)
                    caidn.click()
                except:
                    raise Exception("The menu options element is not found")
                sleep(3)

                found = 1
                break
                #如果不跳出循环会导致StaleElementReferenceExceptions
        if found!=1:
            raise Exception("没有找到对象")

    # main_chat_message_assistant = "//span[text()='文件传输助手']/../../preceding-sibling::div[1]"
    # main_chat_message_assistant = "//span[text()='文件传输助手']/../../../child::div[1]"
    main_chat_message_assistant_start = "//span[text()=\'"
    main_chat_message_assistant_end = "\']/../../../child::div[1]"
    def main_messagelist_groupname_issticky(self,name):
        '''判断该会话是否置顶'''
        groupnames = self.driver.get_elements(self.main_messagelist_groupname_01_loc)
        found = 0
        for groupname in groupnames:
            if groupname.text == name:
                #判断当前元素是否置顶
                #li/dev/p/span，找爷爷节点
                #拼接字符串
                assistant_loc = self.main_chat_message_assistant_start + name + self.main_chat_message_assistant_end
                print(assistant_loc)
                tomp = self.driver.get_attribute(assistant_loc,"class")
                print("topm为:"+tomp)
                if "list-top ng-scope" in tomp:
                    print("置顶成功")
                    return True
                else:
                    return False
                found = 1
        if found == 0:
            raise Exception("没有找到对象")

    main_chat_message_abstract_start = "//span[text()=\'"
    main_chat_message_abstract_end = "\']/../../../child::div[3]/child::p[1]/child::span[1]"
    def main_messagelist_groupname_isabstract(self, name):
        '''判断该会话摘要是否存在'''
        groupnames = self.driver.get_elements(self.main_messagelist_groupname_01_loc)
        found = 1
        for groupname in groupnames:
            if groupname.text == name:
                # li/dev/p/span，找爷爷节点
                # 拼接字符串
                loc = self.main_chat_message_abstract_start + name + self.main_chat_message_abstract_end
                print(loc)
                try:
                    tomp = self.driver.get_element(loc)
                except:
                    found = 0
                    pass
                if found == 0:
                    print("会话摘要为空")
                    return False
                else:
                    return True
                found = 1


    # 消息列表中指定账户的列表摘要内容
    main_messagelist_row_loc = "class=>context-menu"
    main_messagelist_row_message_loc= "./div[3]/p/span"
    def main_messagelist_message(self,number=0):
        elements = self.driver.get_elements(self.main_messagelist_row_loc)
        return self.driver.get_text(self.driver.get_sub_element(elements[number],self.main_messagelist_row_message_loc))
    # def get_messagelist_onname_abstract(self,name):
    #     elements = self.driver.get_elements(self.mian_chat_messagelist_loc)
    #     for element in elements:
    #         if element.text

    #安通+团队聊天中 点击安通+是什么link
    main_chat_Actoma_WhatIsActoma_loc = "//ul[@class='media msg-content file-process-container ng-scope']/li[2]/div/p"
    def click_main_chat_Actoma_WhatIsActoma(self,text):
        messages = self.driver.get_elements(self.main_chat_Actoma_WhatIsActoma_loc)
        found = 0
        for message in messages:
            if message.text == text:
                message.click()
                found = 1
                break
        if found!=1:
            raise Exception("没有找到对象")

    #安通+团队聊天中 查找“安通+是什么”link
    # main_chat_Actoma_WhatIsActoma_loc = (By.XPATH,"//ul[@class='media msg-content file-process-container ng-scope']/li/div/p")
    # def main_chat_Actoma_WhatIsActoma(self,i):
    #     self.find_elements(*self.main_chat_Actoma_WhatIsActoma_loc)[i]

    #安通+团队聊天页面，定位“欢迎使用安通+”元素
    main_chat_Actoma_loc = "//div[@class='msg-type-text msg-type-text-left not-handle-link ng-binding selectable-at']"
    def main_chat_Actoma(self):
        self.driver.get_element(self.main_chat_Actoma_loc)

    #安通+对话中的title信息
    # main_chat_Actoma_title_loc = (By.XPATH,"//p[@class='head-title conv-title']/span/span/span")
    main_chat_Actoma_title_loc = "class=>chat-head-name"
    def main_chat_Actoma_title_text(self):
        return self.driver.get_element(self.main_chat_Actoma_title_loc).text

    #添加好友对话
    main_addfriend_inputbox_loc = "//input[@autofocus='autofocus']"
    def input_main_addfriend_inputbox(self,account):
        self.driver.input(self.main_addfriend_inputbox_loc,account)

    main_addfriend_OKbutton_loc = "//button[@class='btn-confirm btn-single ng-binding']"
    def click_main_addfriend_OKbutton(self):
        self.driver.click(self.main_addfriend_OKbutton_loc)

    #页面所有浮动提示
    #等待某个提示信息出现
    toast_text_loc = "//div[@id='toastMessage']/div/span"
    def wait_toastMessage_hint_isdisplay(self,msg):
        self.driver.toast_msg_text(self.toast_text_loc,msg)

    #关闭窗口
    main_close_windows_loc= "//li[@class='operation-button close-window']"
    def close_windows(self):
        self.driver.click(self.main_close_windows_loc)

    #芯片管家是什么？弹出的窗口中的文本信息
    newwindows_whatisActoma_loc= "//div[@class='mui-content at-article']/h3"
    def newwindows_whatisActoma_title_text(self):
        self.driver.switch_to_frame("class=>modal-box")
        sleep(1)
        return self.driver.get_element(self.newwindows_whatisActoma_loc).text
        sleep(1)
        self.driver.switch_to_frame_out()

    # 安通+主页面的“添加”按钮
    # add_loc = (By.XPATH,"//i[@class ='menu-extra-options-icon']")
    add_loc = "class=>menu-extra-options-icon"
    def main_add_attribute(self,attribute):
        return self.driver.get_attribute(self.add_loc,attribute)
    def main_add_attribute_isdisplay(self):
        return self.driver.get_display(self.add_loc)

    #右击已发送的文本消息，右键--ch
    def context_click_main_message(self,i):
        elements = self.driver.get_elements(self.main_chat_send_messageinfo_loc)
        self.driver.right_click(elements[i])

    #右键已发送的图片消息--ch
    main_send_tpmessage_loc = "//div[@class = 'msg-type-img msg-type-img-right ng-scope']/img"
    # main_send_tpmessage_state = "//div[@class = 'chat-room-wrapper']/message[-1]/div/div/div/div[2]/div[2]/span"
    def context_click_main_tpmessage(self,i):
        elements = self.driver.get_elements(self.main_send_tpmessage_loc)
        self.driver.right_click(elements[i])
        # element = self.driver.get_element(self.main_send_tpmessage_state)
        # print("发送状态打印---" + element)
        # if element == "已发送" or "已送达" or "已阅读":
        #     self.driver.right_click(elements[i])
        # else:
        #     raise Exception("还处于发送中状态")

    # 点击撤回 文本 --ch
    main_callback_loc = "//ul[@class = 'dropdown-menu dropdown-menutx']/li[4]/a"
    def Click_main_callback(self):
        self.driver.click(self.main_callback_loc)
	# 点击撤回图片
    main_callbacktp_loc = "//ul[@class = 'dropdown-menu dropdown-menutx']/li[2]/a"
    def Click_main_callbacktp(self):
        self.driver.click(self.main_callbacktp_loc)

       #聊天会话中已经定位到某条文本消息
    # main_chat_send_messagelist_loc = (By.CLASS_NAME,"msg-type-text msg-type-text-right handle-link ng-binding ng-scope selectable-at")
    # def main_chat_send_messagelist(self,i):
    #     return self.find_elements(*self.main_chat_send_messagestate_loc)[i]

    #聊天对话框中的截图按钮
    click_main_screenshots_button_loc = "//ul[@class='tool-bar']/li[2]/div/i"
    def click_main_screenshots_button(self):
        self.driver.click(self.click_main_screenshots_button_loc)

    #双击进行快速截图
    # double_click_main_screenshots_loc = (By.CLASS_NAME, "Chrome_WidgetWin_0")
    def double_click_main_screenshots(self):
        # double_click = self.find_element(*self.double_click_main_screenshots_loc)
        # ActionChains(self.driver).context_click(double_click).perform()
        action = ActionChains(self.driver)
        #鼠标在当前停留的位置做双击操作
        # action.double_click().perform()
        action.move_by_offset(10, 50).perform()

    # 编辑框中@后弹框列表中最后一个成员@ ---cuihong
    #点位弹框的位置前：将AT-APP/common/lib/jquery/jquery.atwho.js 文件中注释掉  //return _this.hide();
    select_main_groupmumber_loc = "//ul[@class = 'atwho-view-ul']/li"
    # select_main_groupmumber_loc = (By.XPATH,"//li[@datan = '[object Object]']")
    def select_main_groupmemer(self,i):
        elements = self.driver.get_elements(self.select_main_groupmumber_loc)
        self.driver.click(elements[i])

    #右击群会话中，最后一条接收到的消息的发送者头像
    context_main_lastimg_loc = "//div[@class = 'chat-item ng-scope not-me']/div/img"
    def context_main_lastimg(self,i):
        elements = self.driver.get_elements(self.context_main_lastimg_loc)
        self.driver.right_click(elements[i])

    #点击@好友弹框
    click_main_pop_loc = "//ul[@class = 'dropdown-menu dropdown-menutx']/li/a"
    def click_main_pop(self):
        self.driver.click(self.click_main_pop_loc)

    #聊天会话中收到的最新的一个未下载文件的下载按钮
    # click_main_lastestfile_download_loc = "//div[@class='receive-file-describe ng-scope']/span[2]"
    # def click_lastestfile_download(self):
    #     self.driver.click(self.click_main_lastestfile_download_loc)
    #聊天会话中最后未下载文件的下载按钮
    click_main_lastestfile_download_loc = "//div[@class='receive-file-describe ng-scope']/span[2]"
    def click_lastestfile_download(self):
        elements = self.driver.get_elements(self.click_main_lastestfile_download_loc)
        self.driver.click(elements[-1])

    # 获取消息显示区最后一个文件的名称
    context_diaplsy_area_lastfile_name = "class=>receive-file-name"
    def main_display_area_lastfile_name(self):
        elements = self.driver.get_elements(self.context_diaplsy_area_lastfile_name)
        return elements[-1].text

    #获取消息显示区最后一个消息的发送状态
    context_diaplsy_area_lastfile_send_state = "class=>msg-state-text"
    def main_display_area_lastfile_send_state(self):
        elements = self.driver.get_elements(self.context_diaplsy_area_lastfile_send_state)
        return elements[-1].text

    # 会话列表切换至安通+团队
    click_messagelist_to_other_list_loc = "id=>session-10000"
    def click_messagelist_to_other_list(self):
        self.driver.click(self.click_messagelist_to_other_list_loc)

    determine_loc = "//button[text()='确定']"
    def click_determine(self):
        '''全局查找确定按钮点击'''
        self.driver.click(self.determine_loc)

    # 会话列表草稿显示
    messagelist_draft_loc = "css=>span.highlight"
    messagelist_draft_file_loc = "css=>span.ng-binding.ng-scope"
    def main_messagelist_draft(self):
        element = self.driver.get_text(self.messagelist_draft_loc)
        elements = self.driver.get_elements(self.messagelist_draft_file_loc)
        elementa = self.driver.get_text(elements[1])
        return element+" "+elementa

    main_messagelist_conversation_nodisturb_loc_start = "//span[.=\'"
    main_messagelist_conversation_nodisturb_loc_end = "\']/../../../span[2]"
    def main_messagelist_conversation_nodisturb(self,name):
        '''检查指定会话是否开启免打扰
        开启免打扰为true,关闭为false
        '''
        found = 1
        loc = self.main_messagelist_conversation_nodisturb_loc_start+name+self.main_messagelist_conversation_nodisturb_loc_end
        try:
            tomp = self.driver.get_element(loc)
            print(tomp)
        except:
            pass
            found = 0
        if found == 1:
            return True
        else:
            return False

    # main_chat_FileManagement_loc = "//div[@class='content-pannel-head ng-scope']/div[2]"
    main_chat_FileManagement_loc = "//div[@ng-click='showFileManage();getFileMsgList();']"
    def click_chat_FileManagement(self,web_driver):
        '''点击当前会话中的文件管理'''
        ActionChains(web_driver).click(web_driver.find_element_by_xpath(self.main_chat_FileManagement_loc)).perform()
        print("点击文件管理")

    file_management_time_divide_loc ="//div[@class='group-setting-body-content file-manager-content ng-scope']/div[2]"
    def click_chat_Filemanagement_TimeDivide_top1(self):
        '''点击文件管理中时间分组的最上面的一个'''
        self.driver.click(self.file_management_time_divide_loc)

    file_management_imglist_01_loc = "//ul[@class='img-list ng-scope']/li[1]/div[1]"
    def click_chat_FileManagement_imglist_01(self):
        '''点击查看'''
        self.driver.click(self.file_management_imglist_01_loc)

    def context_click_chat_Filemanagement_imglist_01(self,web_driver):
        '''右击图片删除'''
        ActionChains(web_driver).context_click(self.driver.get_element(self.file_management_imglist_01_loc)).perform()
        self.driver.click(self.main_chat_messageinfo_delete_loc)

    def is_context_click_chat_Filemanagement_imglist(self,web_driver):
        '''判断右击菜单中的数据'''

    FileManagement_file_button_loc = "//span[@id='file-title-doc']"
    def click_chat_FileManagement_File(self):
        '''点击文件管理中的文件选项'''
        self.driver.click(self.FileManagement_file_button_loc)

    FileManagement_file_time_divide_top1_loc = "//div[@id='ul-file0']"
    def click_chat_FileManagement_File_TimeDivide_top1(self):
        '''点击文件列表中第一个分组'''
        self.driver.click(self.FileManagement_file_time_divide_top1_loc)

    FileManagement_file_top1_divide_file1_loc = "//div[@id='ul-file0']/ul/li[1]"
    def context_click_chat_FileManagement_File_TimeDivide_top1_file1(self,web_driver):
        '''右击文件列表下的第一个文件'''
        ActionChains(web_driver).context_click(self.driver.get_element(self.FileManagement_file_top1_divide_file1_loc)).perform()

    main_chat_download_loc = "link_text=>下载"
    def click_download(self):
        '''全局定位下载'''
        '''这里提一句为什么要获取一个列表，首先不能判断当前会话中存在几个未下载的文件，不能保证是下载文件列表中第一个文件'''
        elements = self.driver.get_elements(self.main_chat_download_loc)
        elements[-1].click()

    download_ng_if = "message.file_state == 201 || message.file_state == 202"
    FileManagement_file_top1_download_progress_loc = "//div[@id='ul-file0']/ul/li[1]/div/div[2]/div[2]"
    def is_FileManagement_file_top1_download(self):
        '''判断是否开始下载，以出现下载就读条为准'''
        element_class = self.driver.get_attribute(self.FileManagement_file_top1_download_progress_loc,"ng-if")
        if element_class in self.download_ng_if:
            return True
        else:
            return False

    main_chat_pause_loc = "link_text=>暂停"
    def click_pause(self):
        '''全局定位暂停'''
        self.driver.element_wait(self.main_chat_pause_loc).click()

    def is_FileManagement_file_top1_pause(self,web_driver):
        '''判断是否已经暂停
        首先右击看弹出菜单内容
        '''
        self.context_click_chat_FileManagement_File_TimeDivide_top1_file1(web_driver)
        '''检查元素'''

    mian_chat_setting_loc = "//div[@ng-click='showGroupSet()']"
    # mian_chat_setting_loc = "//div[@class='content-pannel-head ng-scope']/div[1]"
    # mian_chat_setting_loc = "//em[@title='设置']/.."
    def click_chat_setting(self,web_driver):
        '''点击一对一聊天中的设置'''
        # self.driver.get_element(self.mian_chat_setting_loc).click()
        ActionChains(web_driver).click(web_driver.find_element_by_xpath(self.mian_chat_setting_loc)).perform()

    main_setting_topchat_loc = "//div[@ng-show='activeSession.top == 0']"
    def click_setting_top_chat_button(self):
        '''点击聊天设置中的置顶聊天'''
        self.driver.click(self.main_setting_topchat_loc)

    main_setting_nottopchat_loc = "//div[@ng-show='activeSession.top == 1']"
    def clicj_setting_nottop_chat_button(self):
        '''点击关闭设置中的在置顶聊天'''
        self.driver.click(self.main_setting_nottopchat_loc)

    main_setting_DonotDisturb_loc = "//div[@ng-click='noDisturb(activeSession)'][1]"
    def click_setting_dontDisturb_button(self):
        '''点击设置中的消息免打扰按钮'''
        self.driver.click(self.main_setting_DonotDisturb_loc)

    main_setting_NotDonotDisturb_loc = "//div[@ng-click='noDisturb(activeSession)'][2]"
    def click_setting_NotDonnotDisturb_button(self):
        '''点击设置中的消息免打扰按钮关闭消息免打扰'''
        self.driver.click(self.main_setting_NotDonotDisturb_loc)

    main_setting_add_Members_loc = "//div[@class='member-name ng-binding'][1]"
    def click_setting_add_Members_buttom(self):
        '''点击设置中的添加成员'''
        self.driver.click(self.main_setting_add_Members_loc)

    main_setting_is_add_Members_page_loc = "//span[@ng-if='!chooseAccountLength']"
    def get_setting_add_Members(self):
        '''返回设置中的添加成员按钮点击后的页面是否出现'''
        return self.driver.get_text(self.main_setting_is_add_Members_page_loc)

    main_setting_close_loc = "//button[@class='btn-confirm btn-large ng-binding']"
    def click_setting_close_button(self):
        '''点击设置中的清除聊天会话'''
        self.driver.click(self.main_setting_close_loc)










