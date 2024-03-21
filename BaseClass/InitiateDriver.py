from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from LibraryFile import ConfigReader

def StartBrowser():
    global driver
    #Normal Method to open URL:(Static Method)
    #path = "C:\\Users\\abc\\Videos\\AnyDesk\\chromedriver.exe"
    #driver = Chrome()
    #driver.maximize_window()
    #driver.get("https://www.naukri.com/")
    #return driver

    #when we use Dynamic URL:

    if((ConfigReader.readConfigData('Details','Browser'))=="Chrome"):
      Path = "C:\\Users\\abc\\Videos\\AnyDesk\\chromedriver.exe"
      driver = Chrome()
    elif((ConfigReader.readConfigData('Details', 'Browser'))=="Firefox"):
      path ="C:\\Users\\abc\\Videos\\Captures\\geckodriver-v0.34.0-win-aarch64\\geckodriver.exe"
      driver = Firefox()

    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver


def CloseBrowser():
    driver.close()