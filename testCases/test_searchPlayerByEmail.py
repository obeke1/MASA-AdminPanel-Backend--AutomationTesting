import time

import pytest

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from pageObjects.loginPage import LoginPage
from testCases.Confest import setup
from pageObjects.searchPlayerPage import SearchPlayer
from pageObjects.addPlayerPage import AddPlayer


class Test_004_searchPlayerByEmail():
    baseURL=ReadConfig.getAppicationURL()
    #baseURL="https://mayunganoamukasocceracademy.000webhostapp.com/admin/"
    username=ReadConfig.getUsername()
    #username="obekevicent@gmail.com"
    password=ReadConfig.getPassword()
    #password="1234"

    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_searchPlayer(self,setup):
        self.logger.info("*********** Test_004_searchPlayer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful ********")

        self.logger.info("******* Starting Search Player By Email **********")
        self.addPlayer=AddPlayer(self.driver)
        self.addPlayer.clickteamPlayerMenu()
        self.addPlayer.clickmanagePlayerMenuitem()
        time.sleep(3)

        self.logger.info("******** Search By Player's Email **********")
        self.searchPlayer=SearchPlayer(self.driver)
        self.searchPlayer.setSearchPlayer("obekegodfrey1@gmail.com")
        time.sleep(2)
        status=self.searchPlayer.searchPlayerByEmail("obekegodfrey1@gmail.com")
        assert True == status
        self.logger.info("******** test_searchPlayerByEmail Passed ***********")
        time.sleep(2)


        self.driver.close()