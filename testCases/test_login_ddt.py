import pytest
from selenium import webdriver
import time
from Utilities import XLUtils
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.loginPage import LoginPage
from testCases.Confest import setup


class Test_002_DDT_Login:
    baseURL=ReadConfig.getAppicationURL()
    path="../testData/loginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Test_002_DDT_Login *****")
        self.logger.info("******* Verifying Login Test DDT ****")
        self.driver=setup

        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:", self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Admin Panel"
            if act_title  == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Passed ******")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****** Failed ******")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****** Failed ******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed ******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test Passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login DDT test Failed *******")
            self.driver.close()
            assert False

        self.logger.info("******** End of Login DDT Test *********")
        self.logger.info("******** Completed TC_loginDDT_002 ********")


