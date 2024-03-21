from selenium.webdriver.common.by import By
from LibraryFile import ConfigReader


class RegistrationClass:

    def __init__(self,Obj):
        global  driver
        driver = Obj

    def enter_Email_Id(self,Email_ID):
        driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails', 'Email_ID')).send_keys(
            "rathore.alkesh6@gmail.com")

    def enter_Password(self,Password):
        driver.find_element(By.XPATH, ConfigReader.fetchElementLocators('LoginDetails', 'Password')).send_keys(
            "EndgameAR@08")
