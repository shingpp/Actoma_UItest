from time import sleep
import datetime
import sys,random
import pytest
sys.path.append("./models")
sys.path.append("./page_obj")
import os
import xlwt
import time
from selenium import webdriver
from web_project.public.myunit import MyTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

account = '5118465'
password = 'a123456'
FRIEND = '贺平平' #好友名称
FRIEND_FILE_NUM = 10  #单个文件测试次数
File_exe_path = "D:\\testexe" #测试录制文件Autolt3文件的存放目录
File_result_path = "D:\\testFiles\\testResult\\Result.xls"
File_result_name = "Result.xls"

class file_performance_test(MyTest):
    def test_01(self):
        '''文件上传测试'''
        # self.Contact.click_friendlist_sendmsg(FRIEND)  # 进入好友聊天
        # sleep(2)
        self.Login.login(account, password)
        sleep(5)
        self.Contact.click_friendlist_sendmsg(FRIEND)
        sleep(2)
        result = xlwt.Workbook()
        sheet = result.add_sheet(datetime.datetime.now().strftime('%Y-%m-%d'))
        exelist = os.listdir(File_exe_path)
        temp = 0
        for testexe in exelist:
            # self.driver.js(FileJS)
            temp += 1
            for i in range(0, FRIEND_FILE_NUM):  # 文件数量
                self.Chat.click_main_chat_filebutton()
                sleep(3)
                os.system(File_exe_path+'\\'+testexe)#引用制定录制的文件
                sleep(2)
                self.Chat.shortcuts_main_chat_send()
                time1 = time.time()
                # 需要添加一个扫描机制，不停扫描等待发送成功 ball-spin-fade-loader-1
                # 在进行该操作之前，需要把public文件夹下的wd_public.py文件中的隐式等待关闭
                WebDriverWait(self.driver.driver, 50, 0.005).until_not(
                    EC.presence_of_element_located((By.CLASS_NAME, 'ball-spin-fade-loader-1'))
                )

                time2 = time.time()
                time3 = time2 - time1
                print("时间：%s" % time3)
                if i == 0 :
                    sheet.write(temp,i,str(testexe))
                sheet.write(temp,i+1,str(time3))
        result.save(File_result_path)