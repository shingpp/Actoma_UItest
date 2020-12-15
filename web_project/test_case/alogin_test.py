#-*- coding: utf-8 -*-
from time import sleep
import pytest
import allure
# from ..public.myunit import MyTest
from web_project.public.myunit import MyTest

# '''输入pin码页面'''
pin = "111111"                                                            #6位pin码
pinNumberOver16 = "01234567890123456"                                   #大于16位的pin码
pinNumberLess6 = "12345"                                                  #小于6位的pin码
pinErr="12345678"                                                        #错误pin码
hint1 = "安全芯片PIN码错误，错误 "                                            #错误pin码的提示，“安全口令错误，错误X次后锁死”
hint2= " 次后锁死 ！"                                                    #错误pin码的提示
pinLengthJS = "return document.querySelector('input[type=password]').value.length"           #pin码输入框长度
pinOKBtn = "disabled"                                                    #pin码确定按钮置灰的属性值

# '''登录页面'''
# account = "5118465"
account = "7341293" #p10pro
accountErr = "123456"
accountLess6 = "12345"                                                    #账户输入少于6位
accountOver20 = "123456789012345678901"                                 #密码输入多余20位
passwordLess6 = "12345"                                                    #密码输入少于6位
passwordOver20 = "123456789012345678901"                                 #密码输入多余20位
# password = "a123123"                                                      #正确密码
password = "a111111"                                                       #正确密码
passwordErr = "12345678"
accountOrPasswordErrHint = "安通⁺帐号或密码错误，请重新输入"                    #账户或密码错误，页面弹出的错误提示
accountAndPasswordErrHint="帐号不存在"
LoginOKBtn = "disabled"                                                   #登录确定按钮置灰的属性值
loginLengthJS = "return document.querySelector('input[name = account]').value.length"          #账户输入框长度
AccountMaxLength = 20                                                      #账户输入的最大长度
passwordLengthJS = "return document.querySelector('input[name = verification]').value.length"  #密码输入框长度
passwordMaxLength = 20
showpassword_attribute = "ng-src"                                           #密码框中明文和密文的切换按钮的属性
showpassword_attribute_text = "./common/imgBlack/button/show-password.png"             ##密码框中明文和密文的切换按钮的属性值
hidepassword_attribute_text = "./common/img/button/hide-password.png"             ##密码框中明文和密文的切换按钮的属性值
changePasswordAccount = "5077704"
changePasswordContent = "帐号：5077704"
changePasswordPhone1 = "15229509882"
changePasswordPhone2 = "18392553197"
changePasswordPhone3 = "17765850223"
newpassword = "111111"
changePasswordSuc = "修改密码成功"


class TestLogin(MyTest):
    '''安通+登录测试'''

    def test_login01(self):
        '''默认PIN码为空时，确定按钮置灰'''
        sleep(1)
        self.driver.assert_equal(self.Login.pinOKbutton_attribute(pinOKBtn),"true")

    def test_login02(self):
        '''输入PIN码6-16位后确定按钮高亮'''
        self.Login.inputpin("111111")
        sleep(2)
        self.driver.assert_equal(self.Login.pinOKbutton_attribute(pinOKBtn),None)
    #
    #
    def test_login03(self):
        '''输入PIN码大于16位后，无法继续输入'''
        self.Login.inputpin(pinNumberOver16)
        sleep(2)
        PinLength = self.driver.js(pinLengthJS)
        self.driver.assert_equal(PinLength,16)


    def test_login04(self):
        '''输入PIN码小于6位后确定按钮置灰'''
        self.Login.inputpin(pinNumberLess6)
        sleep(2)
        self.driver.assert_equal(self.Login.pinOKbutton_attribute(pinOKBtn),"true")


    def test_login05(self):
        '''输入PIN码后，点击清除按钮'''
        self.Login.inputpin(pin)
        sleep(1)
        self.Login.click_clearpinbutton()
        sleep(2)
        self.driver.assert_equal(self.Login.pinOKbutton_attribute(pinOKBtn),"true")


    def test_login06(self):
        '''输入错误PIN码，页面显示提示信息'''
        self.Login.inputpin(pinErr)
        sleep(2)
        self.Login.click_pinOKbutton()
        sleep(2)
        # self.driver.assert_in(hint1,self.Login.pinerror_hint())
        # self.driver.assert_in(hint2,self.Login.pinerror_hint())
        # sleep(1)

    #
    def test_login07(self):
        '''输入正确PIN码，进入到登录页面'''
        self.Login.pin()
        sleep(5)
        self.driver.assert_true(self.Login.loginbutton_isdisplay())
        sleep(1)


    def test_login08(self):
        '''登录页面，账户输入5位，密码输入6位，登录按钮置灰'''
        # self.Login.pin()
        # sleep(5)
        self.Login.input_login_account(accountLess6)
        sleep(2)
        self.Login.input_login_password(password)
        sleep(2)
        self.driver.assert_equal(self.Login.loginbutton_attribute(LoginOKBtn),"true")


    def test_login09(self):
        '''登录页面，账户输入21位，密码输入6位，登录按钮置灰'''
        # self.Login.pin()
        # sleep(5)
        self.Login.input_login_account(accountOver20)
        sleep(2)
        self.Login.input_login_password(password)
        sleep(2)
        AccountLength = self.driver.js(loginLengthJS)
        self.driver.assert_equal(AccountLength,AccountMaxLength)


    def test_login10(self):
        '''登录页面，账户输入6位，密码输入5位，登录按钮置灰'''
        # self.Login.pin()
        # sleep(5)
        self.Login.input_login_account(account)
        sleep(2)
        self.Login.input_login_password(passwordLess6)
        sleep(2)
        self.driver.assert_equal(self.Login.loginbutton_attribute(LoginOKBtn),"true")


    def test_login11(self):
         # 登录页面，账户输入6位，密码输入21位(密码最多只能输入20位)
        # self.Login.pin()
        # sleep(5)
        self.Login.input_login_account(account)
        sleep(2)
        self.Login.input_login_password(passwordOver20)
        sleep(3)
        # self.driver.assert_equal(po.loginbutton_attribute("disabled"),"true")
        PasswordLength = self.driver.js(passwordLengthJS)
        self.driver.assert_equal(PasswordLength,20)


    def test_login12(self):
        # '输入密码，点击显示密码，密码框中密码显示明文
        # self.Login.pin()
        # sleep(6)
        self.Login.input_login_password(password)
        sleep(2)
        self.Login.click_login_showpassword()
        sleep(2)
        # self.driver.assert_equal(self.Login.login_showpassword_attribute(showpassword_attribute), showpassword_attribute_text)


    def test_login13(self):
         # '输入密码，点击显示密码，密码框中密码显示明文，再次点击，显示密文
        # self.Login.pin()
        # sleep(5)
        self.Login.input_login_password(password)
        sleep(2)
        self.Login.click_login_showpassword()
        sleep(1)
        self.Login.click_login_showpassword()
        sleep(2)
        # self.driver.assert_equal(self.Login.login_showpassword_attribute(showpassword_attribute),hidepassword_attribute_text)


    def test_login14(self):
         # 输入正确账户，错误密码，点击登录，页面有提示信息
        self.Login.login(account,passwordErr)
        sleep(5)
        self.driver.assert_in(accountOrPasswordErrHint,self.Login.loginhint_text())


    def test_login15(self):
        # 输入错误账户，错误密码，点击登录，页面有提示信息
        self.Login.login(accountErr)
        sleep(2)
        self.driver.assert_in(accountAndPasswordErrHint,self.Login.loginhint_text())


    def test_login16(self):
        # 输入正确账户密码，点击登录登录成功,通过主页面的添加“+”按钮进行断言
        self.Login.login(password)
        sleep(5)
        self.driver.assert_true(self.Chat.main_add_attribute_isdisplay())


    # def test_login17(self):
    #     '''更多-重置密码（通过三个好友手机号）'''
    #     # self.Login.pin()
    #     # sleep(8)
    #     # self.Login.click_login_unfold()
    #     # sleep(1)
    #     self.Login.click_login_more()
    #     sleep(2)
    #     self.Login.click_login_more_resetpassword()
    #     sleep(2)
    #     self.Login.click_main_resetPWD_friend()
    #     sleep(1)
    #     self.Login.input__main_resetPWD_friend_numinputbox(changePasswordAccount)
    #     self.Login.click_main_resetPWD_mun_next()
    #     sleep(3)
    #     self.Login.input_main_resetPWD_friend_inputphone1(changePasswordPhone1)
    #     sleep(1)
    #     self.Login.input_main_resetPWD_friend_inputphone2(changePasswordPhone2)
    #     sleep(1)
    #     self.Login.input_main_resetPWD_friend_inputphone3(changePasswordPhone3)
    #     sleep(2)
    #     self.Login.click_main_resetPWD_friendnum_okButton()
    #     sleep(4)
    #     self.driver.assert_in(changePasswordContent,self.Login.main_resetPWD_account_text())
    #     self.Login.input_main_resetPWD_newpassword(newpassword)
    #     sleep(2)
    #     self.Login.click_main_resetPWD_mewPWD_okButton()
    #     self.Chat.wait_toastMessage_hint_isdisplay(changePasswordSuc)changePasswordSuc


if __name__ == "__main__":
    pytest.main("-v alogin_test.py::TestLogin")


