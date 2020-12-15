# -*-coding:utf-8-*-
from web_project.pages.login_page import Login
# from ..pages.login_page import Login
from .base import Page
from time import sleep

class Search(Page):

    #封装搜索好友/群组
    def click_search_friend_or_group(self):
        self.Login = Login(self.driver)
        self.Login.login()
        sleep(2)
        self.main_search_click()
        sleep(1)
        self.main_search_friend()
        sleep(2)

    #封装搜索搜索联系人（仅支持姓名）
    def click_search_person(self):
        self.Login = Login(self.driver)
        self.Login.login()
        sleep(2)
        self.main_search_click()
        sleep(1)
        self.main_search_person()
        sleep(2)

    # 搜索输入框
    main_search_loc = "//li[@class='select2-search-field']/input"
    def main_search_click(self):
        self.driver.click(self.main_search_loc)
    def main_search_input(self,text):
        self.driver.input(self.main_search_loc,text)
    def main_search_input_text(self):
        return self.driver.get_attribute(self.main_search_loc,"placeholder")


    # 搜索输入框--集团通讯录
    main_search_person_input_loc = "//li[@class='select3-search-field']/input"
    def main_search_person_input_text(self):
        return self.driver.get_attribute(self.main_search_person_input_loc,"placeholder")
    def main_search_person_input_name(self,text):
        self.driver.input(self.main_search_person_input_loc,text)

    #搜索选择好友/群组
    main_search_friend_loc = "//ul[@class='search-choices']/li[1]/a"
    def main_search_friend(self):
        self.driver.click(self.main_search_friend_loc)

    #搜索选择集团通讯录
    main_search_person_loc = "//ul[@class='search-choices']/li[2]/a"
    def main_search_person(self):
        self.driver.click(self.main_search_person_loc)

    # 搜索结果中显示一行备注/昵称
    main_search_result_loc = "//div[@ng-show = 'searchResults[0].length>0 && searchResultLength == 5 && searchResultGroupLength == 5 && !searchLoading']/ul/li/div/div/p"
    def main_search_result_list(self,name):
        lists = self.driver.get_elements(self.main_search_result_loc)
        result = "false"
        for list in lists:
            if name in list.text:
                result = "true"
        return result

    # 搜索结果中显示备注/昵称，和账号
    # main_search_result_row_loc = (By.XPATH,"//div[@class = 'result-name ng-binding']")
    main_search_result_RemarkOrNickname_loc = "//div[@class = 'result-name ng-binding']/p"
    main_search_result_Personname_loc = "//div[@class = 'search-reault-inner']/div[4]/ul/li/div/div"
    main_search_result_account_loc = "//div[@class = 'result-name ng-binding']/p[2]"
    # 显示一行中的备注或昵称信息
    def main_search_result_RemarkOrNickname(self,name):
        lists = self.driver.get_elements(self.main_search_result_RemarkOrNickname_loc)
        result = "false"
        for list in lists:
            if name in list.text:
                result = "true"
        return result
    # 显示一行中的账号信息
    def main_search_result_account(self,account):
        lists = self.driver.get_elements(self.main_search_result_account_loc)
        result = "false"
        for list in lists:
            if account in list.text:
                result = "true"
        return result

    #点击搜索出的联系人
    def main_search_result_click_name(self,name):
        lists = self.driver.get_elements(self.main_search_result_RemarkOrNickname_loc)
        found = 0
        for list in lists:
            if name in list.text:
                list.click()
                found = 1
                break
        if found != 1:
            raise Exception("没有找到对象")
    #点击搜索出的集团通讯录联系人
    def main_search_result_click_person_name(self,name):
        lists = self.driver.get_elements(self.main_search_result_Personname_loc)
        found = 0
        for list in lists:
            if name in list.text:
                list.click()
                found = 1
                break
        if found != 1:
            raise Exception("没有找到对象")

    #点击搜索按钮
    main_search_input_click_button_loc = "//li[@class='select3-search-field']/button"
    def mian_search_input_click_button(self):
        self.driver.click(self.main_search_input_click_button_loc)

    # 搜索结果为空
    main_search_result_null_loc = "//div[@class = 'search-reault-inner']/div[2]/p"
    def main_search_result_null(self):
        return self.driver.get_text(self.main_search_result_null_loc)

