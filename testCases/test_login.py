from selenium import webdriver
from pageObjects.loginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import pytest
from testCases.Confest import setup


class Test_001_Login():
    baseURL=ReadConfig.getAppicationURL()
    #baseURL="https://mayunganoamukasocceracademy.000webhostapp.com/admin/"
    username=ReadConfig.getUsername()
    #username="obekevicent@gmail.com"
    password=ReadConfig.getPassword()
    #password="1234"

    logger=LogGen.loggen()
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*********** Start Test_001_Login ******** ")
        self.logger.info("*********** Verifying the Home Page Title **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.act_title =self.driver.title
        if self.act_title == "Login":
            assert  True
            self.driver.close()
            self.logger.info("********** Home Page Title Test is Passed ************")
        else:
            self.driver.save_screenshot("../Screenshot/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page Title Test is Failed ************")
            assert False

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*********** Verifying the Login Test **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.act_title1 = self.driver.title
        if self.act_title1 == "Admin Panel":
            assert True
            self.driver.close()
            self.logger.info("********** Login Test is Passed ************")
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("********** Login Test is Failed ************")
            assert False


