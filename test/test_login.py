import time
import unittest
import pytest
from pages.login_aboutus import Login
import utilities.customlogger as cl


# from pages.signin import Sign_in
# import allure

@pytest.mark.usefixtures("beforeMethod")
class Log_in(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
        # self.sign_in = Sign_in(self.driver)
        self.login = Login(self.driver)

    def test_login(self):
        # time.sleep(5)
        #self.login.switch_tab();
        #time.sleep(5)
        self.login.scroll()
        self.login.send_email()
        self.login.send_password()
        self.login.click_check()
        self.login.click_submit()
        self.login.scroll()
        #self.login.click_accept()
        self.login.scroll_about()
        self.login.click_about_us()
        self.login.click_privacy_policy()
        self.login.click_terms()
        self.login.click_faq()
        # assert "Thank You for your Message!" == self.contact.text_thankyou()
        # print("Assertion is done:", "Thank You for your Message!" == self.contact.text_thankyou())
        # cl.allureLogs("Assertion Done")