# -*- coding: utf-8 -*-
from .base import Page
from time import sleep
# from ..pages.login_page import Login
from web_project.pages.login_page import Login

class Set(Page):

    def enter_to_settind_page(self):
        self.Login = Login(self.driver)
        self.Login.login()
        sleep(5)
        self.click_main_menu_settings()

    # 右侧边栏设置
    # main_menu_settings_loc=(By.XPATH,"//ul[@class='main-menus']/li[5]")
    main_menu_settings_loc= "class=>at-menu-setting"
    def click_main_menu_settings(self):
        self.driver.click(self.main_menu_settings_loc)

    #左侧边栏设置-退出登录
    main_menu_settings_logout_loc= "//div[@class='main-setup-right-detail']/button[@ng-click='logout()']"
    def click_main_menu_settings_logout(self):
        self.driver.click(self.main_menu_settings_logout_loc)

    #退出登录弹出的提示信息
    main_logout_hint_text_loc = "class=>dialog-content-child"
    def main_logout_hint_text(self):
        return self.driver.get_text(self.main_logout_hint_text_loc)

    #退出登录弹出的提示信息的确定按钮
    main_logout_hint_okbutton_loc= "class=>btn-confirm"
    def click_logout_hint_okbutton(self):
        self.driver.click(self.main_logout_hint_okbutton_loc)

    #设置-快捷按键
    main_menu_setting_shortcut_loc = "//ul[@class='main-setup-left']/li[3]"
    def click_main_menu_setting_shortcut(self):
        self.driver.click(self.main_menu_setting_shortcut_loc)

    #下拉按钮
    # main_menu_setting_shortcut_select = "//select[@ng-change='setSendMsg()']"
    main_menu_setting_shortcut_select = "//div[@ng-blur='hideSelectOptions()']"
    def click_main_menu_setting_shortcut_select(self):
        self.driver.click(self.main_menu_setting_shortcut_select)

    # 选择Enter
    # main_menu_setting_shortcut_enter = "//select[@ng-change='setSendMsg()']/option[1]"
    main_menu_setting_shortcut_enter = "//div[@ng-show='showSelect']/div[1]"#淦，这个enter和ctrl+enter按钮在设置中有两个，经常会定位错误
    def click_main_menu_setting_shortcut_enter(self):
        self.driver.click(self.main_menu_setting_shortcut_enter)

    #选择Ctrl+Enter
    # main_menu_setting_shortcut_ctrlenter = "//select[@ng-change='setSendMsg()']/option[2]"
    main_menu_setting_shortcut_ctrlenter = "//div[@ng-blur='hideSelectOptions()']/div[2]"
    def click_main_menu_setting_shortcut_ctrlenter(self):
        self.driver.click(self.main_menu_setting_shortcut_ctrlenter)

    #关闭设置页面
    main_menu_setting_paper = "class=>dialog-close"
    def click_main_menu_setting_paper(self):
        self.driver.click(self.main_menu_setting_paper)