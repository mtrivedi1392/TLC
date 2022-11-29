import pytest
import time
from base.driver import WebDriverClass


@pytest.fixture(scope='function', autouse=True)
def beforeMethod(request):
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("Chrome")
    driver.get("https://shangrila.questexdata.com/")
    driver.maximize_window()
    time.sleep(4)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()