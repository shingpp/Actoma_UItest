import os
import xlwt
from time import sleep
import sys,random

import os

import time

import pytest

sys.path.append("./models")
sys.path.append("./page_obj")

from selenium import webdriver

from web_project.public.myunit import MyTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from ..public.myunit import MyTest

# f = xlwt.Workbook()
# sheet = f.add_sheet('sheettest')
# sheet.write(0,0,'cehsi')
# f.save('D:\\testExcel.xls')

'''文件传输助手，聊天列表点击置顶'''
#在联系人好友列表中选择文件传输助手并点击进入会话
Test_File_transfer_assistant = "文件传输助手"
self.Contact.click_contactlist_antonglist(Test_File_transfer_assistant)
self.Contact.click_main_friend_detal_dialog_enter()
#在消息列表中右击后选择置顶聊天
self.Chat.click_main_messagelist_groupname(Test_File_transfer_assistant)
