from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from BaseClass import InitiateDriver
from LibraryFile import ConfigReader


def test_TC_002_FindNewJob():
    driver = InitiateDriver.StartBrowser()

    #When we use Static Data:
    #driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter skill')]").send_keys("Automation Testing")
    #driver.find_element(By.XPATH,"//div[@class='qsbSubmit']").click()

    #When we use Dynamic Data:
    driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails','Search')).send_keys("Automation Testing")
    driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails','Click')).click()