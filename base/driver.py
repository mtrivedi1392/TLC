from selenium import webdriver
import utilities.customlogger as cl
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "Chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            self.log.info("Chrome browser is initialised")
        elif browserName == "Safari":
            driver = webdriver.Safari()
            self.log.info("Safari browser is initialised")
        elif browserName == "Firefox":
            driver = webdriver.Firefox(GeckoDriverManager.install())
            self.log.info("Firefox browser is initialised")

        return driver
