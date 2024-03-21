import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from BaseClass import InitiateDriver
from LibraryFile import ConfigReader
from Pages import RegistrationPage
import pytest
from DataDriven import DataGenerater


    # Without using Excel Sheet
    #li =[['Rathore.alkesh6@gmail.com','EndgameAR@08'],['ralkesh98@gmail.com','EndgameAR@08']]
    #return li


@pytest.mark.parametrize('data',DataGenerater.DataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.StartBrowser()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails', 'login')).click()
    driver.implicitly_wait(3)
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_Email_Id(data(0))
    register.enter_Password(data(1))
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails', 'Submit')).click()

    time.sleep(2)