import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import pytest
from testCases.Confest import setup
from pageObjects.addPlayerPage import AddPlayer
import random


class Test_003_addPlayer():
    baseURL=ReadConfig.getAppicationURL()
    #baseURL="https://mayunganoamukasocceracademy.000webhostapp.com/admin/"
    username=ReadConfig.getUsername()
    #username="obekevicent@gmail.com"
    password=ReadConfig.getPassword()
    #password="1234"

    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addPlayer(self,setup):
        self.logger.info("*********** Test_003_AddPlayer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful ********")

        self.logger.info("******* Starting Add Player Test **********")
        self.addPlayer=AddPlayer(self.driver)
        self.addPlayer.clickteamPlayerMenu()
        self.addPlayer.clickmanagePlayerMenuitem()
        self.addPlayer.clickaddPlayerButton()

        self.logger.info("******* Starting to provide the Player Details")

        self.addPlayer.browsePlayerPhoto()

        self.addPlayer.setplayerFullname("OKello Ivan")
        time.sleep(2)

        self.addPlayer.setplayerGender("Male")
        time.sleep(2)

        self.addPlayer.setplayerDOB("01/01/2015")
        time.sleep(2)

        self.email=random_generator() + "@gmail.com"
        self.addPlayer.setplayerEmail(self.email)
        time.sleep(2)

        self.addPlayer.setplayerPassword("okelloIvan")
        time.sleep(2)

        self.addPlayer.setplayerSchool("Lira Central Primary School")
        time.sleep(2)

        self.addPlayer.setplayerNationality("Uganda")
        time.sleep(2)

        self.addPlayer.setplayerClass("Under 7-10")
        time.sleep(2)

        self.addPlayer.setplayerProgramme("Holiday Programme")
        time.sleep(2)

        self.addPlayer.setplayerSeason("2020/2021")
        time.sleep(2)

        self.logger.info("***** Starting Providing Parents' and Guardian's Details *****")
        self.logger.info("************Start Providing Father's Details **********")

        self.addPlayer.setfatherFullname("Okello Jasper")
        time.sleep(2)

        self.addPlayer.setfatherresidence("Teso Bar")
        time.sleep(2)

        self.addPlayer.setfatherMobile("0701123456")
        time.sleep(2)

        self.email1 = random_generator() + "@gmail.com"
        self.addPlayer.setfatherEmail(self.email1)
        time.sleep(2)

        self.logger.info("************Start Providing Mother's Details **********")

        self.addPlayer.setmotherFullname("Adong Esther")
        time.sleep(2)

        self.addPlayer.setmotherresidence("Teso Bar")
        time.sleep(2)

        self.addPlayer.setmotherMobile("0781123456")
        time.sleep(2)

        self.email2 = random_generator() + "@gmail.com"
        self.addPlayer.setmotherEmail(self.email2)
        time.sleep(2)

        self.logger.info("************Start Providing Guardian's Details **********")

        self.addPlayer.setguardianFullname("Otim Daniel")
        time.sleep(2)

        self.addPlayer.setguardianMobile("0782123456")
        time.sleep(2)

        self.addPlayer.clicksubmitButton()

        self.logger.info("******* Saving Player's Info ********")
        self.logger.info("******* Add Player Validation Started ********")

        """
        #self.msg=self.driver.find_element(By.XPATH,"//div[@class='box box-info']").text
        #self.msg=self.driver.find_element_by_tag_name("box-body").text
        self.msg=self.driver.find_element(By.TAG_NAME,"box- body")
        print(self.msg)
        
        if 'Player has been added successfully :' in self.msg:
            assert True == True
            self.logger.info("******** Add Player Test Passed *******")
        else:
            self.driver.save_screenshot("../Screenshot/" + "test_addPlayer.png")
            self.logger.error("********** Add Player Test Failed ************")
        """

        self.driver.close()

        self.logger.info("******* Ending Add Player Test *********")

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))




