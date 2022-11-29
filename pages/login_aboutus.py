import time

from base import driver
from base.base import BaseClass


class Login(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    email = "email"  # name
    password = "password"   # name
    check = "lg_remember" # id
    submit = "//button[@class = 'btn btn-sm btn-default']" # xpath
    about_us = "//a[@href='http://www.shangri-la.com/corporate/about-us/']" # xpath
    accept = "ch2-btn ch2-allow-all-btn ch2-btn-primary" #class
    privacy_policy = "//a[@href='http://www.shangri-la.com/corporate/policies-pledges/']" # xpath
    terms = "//a[@href= 'https://shangrila.questexdata.com/benefits#terms']" # xpath
    faq = "//a[@href= 'https://shangrila.questexdata.com/faq']" # xpath


    # method

    def scroll(self):
        self.scrollTo(self.email, "name")

    def send_email(self):
        self.send_text("jtielmann@questex.com", self.email, "name")

    def send_password(self):
        self.send_text("questex", self.password, "name")

    def click_check(self):
        self.click_on_element(self.check, "id")

    def click_submit(self):
        self.click_on_element(self.submit, "xpath")

    def scroll_about(self):
        self.scrollTo(self.about_us, "xpath")

    def click_about_us(self):
        self.click_on_element(self.about_us, "xpath")

    def click_accept(self):
        self.click_on_element(self.accept, "class")

    def click_privacy_policy(self):
        self.click_on_element(self.privacy_policy, "xpath")

    def click_terms(self):
        self.click_on_element(self.terms, "xpath")

    def click_faq(self):
        self.click_on_element(self.faq, "xpath")

    # def text_thankyou(self):
    #     return self.get_element(self.thankyou, "xpath").text
    #
    # # assert "Thank You for your Message!" == text_thankyou()
    #
    # # def selectcountry(self):
    # #     self.get_Option_by_Text_Index(41, "xpath")
    # #
    # # def click_state(self):
    # #      self.click_on_element(self.statedrpdwn, "xpath")
    #
    # # def click_estishipping(self):
    # #     self.click_on_element(self.estiship, "name")
    # #
    # # def click_checkbox(self):
    # #     self.click_on_element(self.checkbox, "name")
    # #
    # # def click_checkout(self):
    # #     self.click_on_element(self.checkout, "id")
    # #
    # # def clik_signout(self):
    # #     self.click_on_element(self.signout, "class")
    # # #
    # # #     # def selectcountry(self):
    # # # #     self.get_Option_by_Text_Index(41, "xpath")
