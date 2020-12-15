# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

# from .androidAPP import AndroidAPPtest
# from ..pages.chat_page import Chat
# from ..pages.contact_page import Contact
# from ..pages.login_page import Login
# from ..pages.search_page import Search
# from ..pages.set_page import Set
# from .wd_public import WDPublic
from web_project.pages.chat_page import Chat
from web_project.pages.contact_page import Contact
from web_project.pages.login_page import Login
from web_project.pages.search_page import Search
from web_project.pages.set_page import Set
from web_project.public.wd_public import WDPublic
from selenium import webdriver
# from web_project.public.androidAPP import AndroidAPPtest


class MyTest(unittest.TestCase):
    def setUp(self):
        #此方法用于启动客户端
        print("初始化")
        path="path =>C:\\Program Files (x86)\\Actoma\\Actoma.exe"
        print(path)
        self.driver = WDPublic(path)          #启动客户端
        print("启动成功")
        # self.driver.wait(20)                           #等待20s，进行文件测试时需要关闭该等待
        self.Chat = Chat(self.driver)
        self.Contact = Contact(self.driver)
        self.Login = Login(self.driver)
        self.Search = Search(self.driver)
        self.Set = Set(self.driver)

    def tearDown(self):                                 #结束时关闭客户端
        self.driver.quit()

# class AndroidTest(unittest.TestCase):
#
#     def setUp(self):
#         #启动手机端安通+
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '5.0.2'
#         desired_caps['deviceName'] = '222ed639'
#         desired_caps['appPackage'] = 'com.xdja.actoma'
#         desired_caps['appActivity'] = 'com.xdja.presenter_mainframe.presenter.activity.SplashPresenter'
#         desired_caps['newCommandTimeout'] = '300'  # 超时时间
#         desired_caps['unicodeKeyboard'] = 'true'  # 是否支持中文
#
#         self.Androiddriver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         self.Androiddriver.implicitly_wait(30)
#
#         #启动PC安通+
#         path = 'path=>C:\Program Files (x86)\Actoma\Actoma.exe'
#         self.driver = WDPublic(path)
#
#         self.androidAT = AndroidAPPtest(self.Androiddriver)
#         self.Chat = Chat(self.driver)
#         self.Contact = Contact(self.driver)
#         self.Login = Login(self.driver)
#         self.Search = Search(self.driver)
#         self.Set = Set(self.driver)
#     def tearDown(self):
#         try:
#             self.Androiddriver.quit()
#         except Exception as msg:
#             print(msg)
#         finally:
#             self.driver.quit()
