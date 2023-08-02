import selenium
from selenium import webdriver

def driver():
    options = webdriver.ChromeOptions()


    return webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options
            )

