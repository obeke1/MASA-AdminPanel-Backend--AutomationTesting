import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name="email"
    textbox_password_name="password"
    button_login_name="form1"
    link_logout_linktext="Log out"
    image_userimage_xpath="//img[@alt='User Image']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME,self.button_login_name).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.image_userimage_xpath).click()
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()


