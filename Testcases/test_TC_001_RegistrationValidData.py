import time
from selenium.webdriver import  Chrome
from selenium.webdriver.common.by import By
from BaseClass import InitiateDriver
from LibraryFile import ConfigReader
from Pages import RegistrationPage


def test_ValidateRegistration():
    driver = InitiateDriver.StartBrowser()
    #When We Use Static Data:
    #driver.implicitly_wait(5)
    #driver.find_element(By.XPATH,"//a[@id='login_Layer']").click()
    #driver.find_element(By.XPATH,"//div[@class='form-row']/input").send_keys("rathore.alkesh6@gmail.com")
    #driver.find_element(By.XPATH,"//input[@type='password']").send_keys("EndgameAR@08")
    #driver.implicitly_wait(5)
    #driver.find_element(By.XPATH,"//button[@type='submit']").click()

    #When We Use Dynamic Data:
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails','login')).click()
    #driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails','Email_ID')).send_keys("rathore.alkesh6@gmail.com")
    #driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails','Password')).send_keys("EndgameAR@08")

    driver.implicitly_wait(2)
    #using POM Pages
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_Email_Id("rathore.alkesh6@gmail.com")
    register.enter_Password("EndgameAR@08")
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails','Submit')).click()


    time.sleep(2)
