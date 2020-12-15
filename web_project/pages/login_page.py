# -*- coding: utf-8 -*-
from .base import Page
from time import sleep


class Login(Page):
    '''用户输入pin码页面和登录页面'''

    pin = "111111"
    account = '7338021'
    password = 'a111111'
    # account = "5192180"
    # password = "a111111"
    #account = "5005813"
    # account="5118465"
    #password ="111111a"
    # password="a123456"
    #封装输入PIN，点击OK
    def pin(self,pi=pin):
        self.inputpin(pi)
        sleep(1)
        self.click_pinOKbutton()

    #封装登录过程
    def login(self,name=account,pw=password):
    # def login(self, pw=password):
        # self.pin()
        # sleep(10)
        self.input_login_account(name)
        sleep(1)
        self.input_login_password(pw)
        sleep(1)
        self.click_loginbutton()
        sleep(5)

    #PIN验证页面
    #pin码输入框
    login_pininputbox_loc = "name=>pinCode"
    #输入PIN码
    def inputpin(self,pin):
        self.driver.clear(self.login_pininputbox_loc)
        self.driver.input(self.login_pininputbox_loc,pin)

    def pininputbox_attribute(self,attribute):
        return self.driver.get_attribute(self.login_pininputbox_loc,attribute)

    # pin码确定按钮
    login_pinOKbutton_loc = "class=>pin-confirm"
    #获取PIN码确定按钮属性
    def pinOKbutton_attribute(self,attribute):
        return self.driver.get_attribute(self.login_pinOKbutton_loc,attribute)

    #单击PIN码确定按钮
    def click_pinOKbutton(self):
        self.driver.click(self.login_pinOKbutton_loc)

    #pin码输入错误提示信息
    login_pinhint_loc = "class=>pinErr"
    def pinerror_hint(self):
        return self.driver.get_text(self.login_pinhint_loc)

    #清空PIN码框
    login_clearpinbutton_loc= "class=>pin-clear"
    def click_clearpinbutton(self):
        self.driver.click(self.login_clearpinbutton_loc)


#登录页面
    #登录按钮
    loginbutton_loc = "class=>loginButton"
    def click_loginbutton(self):
        self.driver.click(self.loginbutton_loc)
    def loginbutton_attribute(self,attribute):
        return self.driver.get_attribute(self.loginbutton_loc,attribute)
    def loginbutton_isdisplay(self):
        return self.driver.get_display(self.loginbutton_loc)
    #登录账户
    login_account_loc = "name=>account"
    def input_login_account(self,account):
        self.driver.clear(self.login_account_loc)
        self.driver.input(self.login_account_loc,account)

    #登录密码
    login_password_loc = "name=>verification"
    def input_login_password(self,password):
        self.driver.clear(self.login_password_loc)
        self.driver.input(self.login_password_loc,password)
    def login_password_attribute(self,attribute):
        self.driver.get_attribute(self.login_password_loc,attribute)

    #登录错误的提示信息
    login_loginhint_loc = "class=>error-msg"
    def loginhint_text(self):
        return self.driver.get_text(self.login_loginhint_loc)

    #正在登录中，请稍后
    login_loading_loc = "class=>loading-text"
    def login_loading(self):
        return self.driver.get_text(self.login_loading_loc)

    #显示密码按钮
    login_showpassword_loc= "//img[@ng-click='showPassword = !showPassword']"
    def click_login_showpassword(self):
        self.driver.click(self.login_showpassword_loc)
    def login_showpassword_attribute(self,attribute):
        return self.driver.get_attribute(self.login_showpassword_loc,attribute)

    # 登录页面的下拉按钮
    login_unfold_loc = "class=>login-unfold-bottom"
    def click_login_unfold(self):
        self.driver.click(self.login_unfold_loc)
    #登录页面更多
    login_more_loc= "//div[@ng-click='more()']"
    def click_login_more(self):
        self.driver.click(self.login_more_loc)
    #登录页面更多-重置密码
    # login_more_resetpassword_loc=(By.CLASS_NAME,"more-resetPWD")
    login_more_resetpassword_loc = "//form[@class='ng-pristine ng-valid']/div[2]/button[2]"
    def click_login_more_resetpassword(self):
        self.driver.click(self.login_more_resetpassword_loc)

    #登录页面更多-返回
    login_more_back_loc= "//button[@ng-click='gotoStep('')']"
    def click_login_more_back(self):
        self.driver.click(self.login_more_back_loc)

    #登录页面更多-返回后，modal-content不存在
    login_more_more_modal_dialog_loc = "class=>more-modal-dialog"
    def login_more_more_modal_dialog_isdisplay(self):
        self.driver.get_display(self.login_more_more_modal_dialog_loc)

    #重置密码--通过账号绑定的手机号验证
    main_resetPWD_phone_loc= "//button[@class='loginButton big btn1']"
    def click_main_resetPWD_phone(self):
        self.driver.click(self.main_resetPWD_phone_loc)

    #重置密码--通过账号绑定的手机号验证--手机号输入框
    main_resetPWD_phone_phoneinputbox_loc= "name=>mobile"
    def input_main_resetPWD_phone_phoneinputbox(self,text):
        self.driver.input(self.main_resetPWD_phone_phoneinputbox_loc,text)

    #重置密码--通过账号绑定的手机号验证-- 获取短信码
    main_resetPWD_phone_getcode_loc= "//button[@ng-click='getResetAuthCode()']"
    def main_resetPWD_phone_getcode_isEnabled(self):
        self.driver.get_enable(self.main_resetPWD_phone_getcode_loc)
    def click_main_resetPWD_phone_getcode(self):
        self.driver.click(self.main_resetPWD_phone_getcode_loc)

    #重置密码--输入验证码
    main_resetPWD_phone_inputcode_loc= "//input[@class='login-input bound-number-right ng-pristine ng-invalid ng-invalid-required ng-touched']"
    def input_main_resetPWD_phone_inputcode(self,text):
        self.driver.input(self.main_resetPWD_phone_inputcode_loc)

    #重置密码--下一步
    main_resetPWD_phone_next_loc= "//button[@class='big']"
    def click_main_resetPWD_phone_next(self):
        self.driver.click(self.main_resetPWD_phone_next_loc)

    #重置密码--显示帐户
    main_resetPWD_account_loc= "//p[@class='account-title ng-binding']"
    def main_resetPWD_account_text(self):
        return self.driver.get_text(self.main_resetPWD_account_loc)

    #重置密码--新密码输入框
    main_resetPWD_newpassword_loc="name=>newPWD"
    def input_main_resetPWD_newpassword(self,text):
        self.driver.input(self.main_resetPWD_newpassword_loc,text)

    # 重置密码--通过好友绑定的手机号验证
    main_resetPWD_friend_loc = "//div[@class='loginButton big btn2']"
    def click_main_resetPWD_friend(self):
        self.driver.click(self.main_resetPWD_friend_loc)

    # 重置密码--通过好友手机号验证--输入安通+账号
    main_resetPWD_friend_numinputbox_loc = "name=>ATaccount"
    def input__main_resetPWD_friend_numinputbox(self, account):
        self.driver.input(self.main_resetPWD_friend_numinputbox_loc,account)

    # 重置密码---好友手机号--下一步
    main_resetPWD_num_next_loc = "class=>ATaccount-confirm"
    def click_main_resetPWD_mun_next(self):
        self.driver.click(self.main_resetPWD_num_next_loc)

    # 重置密码--输入三个好友手机号
    main_resetPWD_friend_inputphone_loc1 = "//form[@name='friendsResetform']/div[2]/input[1]"
    def input_main_resetPWD_friend_inputphone1(self, phone):
        self.driver.input(self.main_resetPWD_friend_inputphone_loc1,phone)
    main_resetPWD_friend_inputphone_loc2 = "//form[@name='friendsResetform']/div[2]/input[2]"
    def input_main_resetPWD_friend_inputphone2(self, phone):
        self.driver.input(self.main_resetPWD_friend_inputphone_loc2,phone)
    main_resetPWD_friend_inputphone_loc3 = "//form[@name='friendsResetform']/div[2]/input[3]"
    def input_main_resetPWD_friend_inputphone3(self, phone):
        self.driver.input(self.main_resetPWD_friend_inputphone_loc3,phone)

    # 重置密码--输入三个好友手机号--确定
    main_resetPWD_friendnum_next_loc = "//button[@class='loginButton big last-step-button login-button-step13']"
    def click_main_resetPWD_friendnum_okButton(self):
        self.driver.click(self.main_resetPWD_friendnum_next_loc)

    # 重置密码---输入新密码--确定
    main_resetPWD_mewPWD_okButton_loc = "class=>newPWD-confirm"
    def click_main_resetPWD_mewPWD_okButton(self):
        self.driver.click(self.main_resetPWD_mewPWD_okButton_loc)



