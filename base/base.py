import datetime
import random
import string
import time
from time import time
import utilities.customlogger as cl
from traceback import print_stack
from selenium.webdriver.support.select import Select
# from appium.webdriver.common.touch_action import TouchAction
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
import json


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            print("Web Page Launched with URL : " + url)
        except:
            print("Web Page not Launched with URL : " + url)

    def wait_for_element(self, locatorvalue, locatortype):
        locatortype = locatortype.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotInteractableException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatortype == "id":
            element = wait.until(lambda x: x.find_element(By.ID, locatorvalue))
            return element
        elif locatortype == "class":
            element = wait.until(lambda x: x.find_element(By.CLASS_NAME, locatorvalue))
            return element
        elif locatortype == "placeholder":
            element = wait.until(lambda x: x.find_element(By.PLACEHOLDER, '%s' % (locatorvalue)))
            return element
        elif locatortype == "name":
            element = wait.until(lambda x: x.find_element(By.NAME, '%s' % (locatorvalue)))
            return element
        elif locatortype == "xpath":
            element = wait.until(lambda x: x.find_element(By.XPATH, '%s' % (locatorvalue)))
            return element
        elif locatortype == "css":
            element = wait.until(lambda x: x.find_element(By.CSS_SELECTOR, '%s' % (locatorvalue)))
            return element
        elif locatortype == "tag":
            element = wait.until(lambda x: x.find_element(By.TAG_NAME, '%s' % (locatorvalue)))
            return element
        elif locatortype == "link":
            element = wait.until(lambda x: x.find_element(By.LINK_TEXT, '%s' % (locatorvalue)))
            return element
        elif locatortype == "plink":
            element = wait.until(lambda x: x.find_element(By.PARTIAL_LINK_TEXT, '%s' % (locatorvalue)))
            return element
        else:
            self.log.info("locator value " + locatorvalue + "not found")
            print("locator value " + locatorvalue + "not found")

        return element

    def get_element(self, locatorvalue, locatortype="xpath"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.wait_for_element(locatorvalue, locatortype)
            self.log.info("element found with locatortype: " + locatortype + " with the locatorvalue :" + locatorvalue)
            print("element found with locatortype: " + locatortype + " with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "element not found with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print("element not found with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)

        return element

    def click_on_element(self, locatorvalue: object, locatortype: object = "xpath") -> object:
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.get_element(locatorvalue, locatortype)
            element.click()
            print("clicked on element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            self.log.info("clicked on element with locatortype: " + locatortype + " and with the locatorvalue :"
                          + locatorvalue)
        except:
            self.log.info("unable to click on element with locatortype: " + locatortype + " and with the locatorvalue :"
                          + locatorvalue)
            print(
                "unable to click on element with locatortype: " + locatortype + " and with the locatorvalue :"
                + locatorvalue)
            self.take_screenshot("Screenshots")
            assert False

    def send_text(self, text: object, locatorvalue: object, locatortype: object = "xpath") -> object:
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.get_element(locatorvalue, locatortype)
            element.send_keys(text)
            self.log.info(
                "send text  on element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print(
                "send text  on element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "unable to send text on element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print(
                "unable to send text on element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            self.take_screenshot("Screenshots")
            assert False

    def clear(self, locatorvalue, locatortype="xpath"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.get_element(locatorvalue, locatortype)
            element.click()
            element.clear()
            self.log.info("clear text on element with locatortype: " + locatortype + " and with the locatorvalue :"
                          + locatorvalue)
            print(
                "clear text on element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
        except:
            self.log.info("unable to clear text on element with locatortype: " + locatortype
                          + " and with the locatorvalue :" + locatorvalue)
            print(
                "unable to clear text on element with locatortype: " + locatortype + " and with the locatorvalue :"
                + locatorvalue)
            self.take_screenshot("Screenshots")
            assert False

    def is_displayed(self, locatorvalue: object, locatortype: object = "xpath") -> object:
        try:
            locatortype = locatortype.lower()
            element = self.get_element(locatorvalue, locatortype)
            value = element.is_displayed()
            self.log.info("element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                          + " is displayed ")
            print(
                "element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                + " is displayed ")
            return value
        except:
            self.log.info("element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                          + " is not displayed")
            print(
                "element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                + " is not displayed")
            self.take_screenshot("Screenshots")
            return False

    def get_text(self, locatorvalue, locatortype="xpath"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.get_element(locatorvalue, locatortype)
            e = element.text()
            self.log.info("element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                          + "is displayed ")
            print(
                "element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                + "is displayed ")
            return e
        except:
            self.log.info("element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                          + " is not displayed")
            print(
                "element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue
                + " is not displayed")
            self.take_screenshot("Screenshots")

    def screenshot(self, screenShotName):
        filename = screenShotName + "_" + (time.strftime("%d_%m_%y_%h_%m_%s")) + ".png"
        screenshotdirectory = "C:/Users/monika.trivedi_infob/workspace_python/demowebshop/reports/screenshot"
        screenshotpath = screenshotdirectory + filename
        try:
            self.driver.save_screenshot(screenshotpath)
            self.log.info("screenshot save to path : " + screenshotpath)
            print("screenshot save to path : " + screenshotpath)
        except:
            self.log.info("unable to save screenshot to the path : " + screenshotpath)
            print("unable to save screenshot to the path : " + screenshotpath)

    def take_screenshot(self, screenshot_name):
        # this is for allure
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

    def swipe(self, x_start, y_start, x_end, y_end):
        devicesize = self.driver.get_window_size()
        screenwidth = devicesize['width']
        screenheight = devicesize['height']
        # step 2 : find the x,y coordinate to swipe from bottom to top
        startx = screenwidth / 2
        endx = screenwidth / 2
        starty = screenheight * 8 / 9
        endy = screenheight / 9

        # step 3 : create touchaction class object
        # actions = TouchAction(self.driver)

        # step 4 : call long press method along with move_to method
        # actions.long_press(None, x_start, y_start).move_to(None, x_end, y_end).release().perform()

    def random_char(self, char_num):
        return ''.join(random.choice(string.digits) for _ in range(char_num))

    def convert_mm_ss_to_seconds_lrm(self, value):
        # Left to right mark
        new_val = value.split(":")
        remain_time = new_val[0].replace("\u200e", "")
        minutes = remain_time.replace("−", '')
        return int(minutes) * 60 + int(new_val[1])

    def read_json_file(self, file_path):
        # Read JSON Data
        myjsonfile = open(
            file_path, 'r')
        jsondata = myjsonfile.read()
        return json.loads(jsondata)

    def key_code(self, value):
        self.driver.press_keycode(value)

    def get_current_date_and_time(self):
        return str(datetime.datetime.time())

    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.wait_for_element(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                "Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print(
                "Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.info(
                "Unable to scroll to WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print(
                "Unable to scroll to WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()

    def get_Option_by_Text_Index(self, text, locatorvalue, locatortype="xpath"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.get_element(locatorvalue, locatortype)
            select = Select(element)
            # dd_v = select.options
            # for dd_values in dd_v:
            #     print(dd_values.text)
            select.select_by_index(text)
            self.log.info(
                "selected the element from dropdown locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print(
                "selected the element from dropdown locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "unable to select element from dropdown with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print(
                "unable to select element from dropdown with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            self.take_screenshot("Screenshots")
            assert False

    def get_Option_by_Text_value(self, text, locatorvalue, locatortype="xpath"):
        element = None

        try:
            select = Select(self.get_element(locatorvalue, locatortype.lower()))
            select.select_by_visible_text(text)
            self.log.info(
                "selected the element from dropdown locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print(
                "selected the element from dropdown locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "unable to select element from dropdown with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            print(
                "unable to select element from dropdown with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
            self.take_screenshot("Screenshots")
            assert False

    def generate_alphanumeric(self, text):
        return text + str(int(time() * 1000))

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def switch_tab(self):
        # obtain window handle of browser in focus
        p = self.driver.current_window_handle
        # obtain parent window handle
        parent = self.driver.window_handles[0]
        # obtain browser tab window
        chld = self.driver.window_handles[1]
        # switch to browser tab
        self.driver.switch_to.window(chld)
        print("Page title for browser tab:")
        print(self.driver.title)

    def alert_handle(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.dismiss()
        print("alert accepted")



        # switch to parent window
        # self.driver.switch_to.window(parent)
        # print("Page title for parent window:")
        # print(self.driver.title)
        # return self.driver.switch_to.window(parent)

    # def switch_page(self, element):
    #     action = ActionChains(self.driver)
    #     # clicks on located kink element with CONTROL button in pressed state using actionChains class. This opens the link in new tab
    #     action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
