from selenium.webdriver.common.by import By


class SearchPlayer:
    txt_searchPlayer_xpath="//input[@type='search']"
    tbl_seachResults_xpath="/html/body/div/div/section[2]/div/div/div/div/div/div[2]/div/table/tbody"
    table_xpath="//*[@id='example1']"
    tableRows_xpath="//table[@id='example1']//tr"
    tableColumns_xpath="//table[@id='example1']//tr//td"

    def __init__(self,driver):
        self.driver=driver

    def clickteamPlayerMenu(self): #Define the method for Team Player Menu
        self.driver.find_element(By.XPATH,self.linkTeamPlayer_menu_xpath).click()

    def clickmanagePlayerMenuitem(self): # define the method for manage player menu item
        self.driver.find_element(By.XPATH,self.linkManagePlayer_menuitem_xpath).click()

    def setSearchPlayer(self,search):
        self.driver.find_element(By.XPATH, self.txt_searchPlayer_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_searchPlayer_xpath).send_keys(search)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchPlayerByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//*[@id='example1']//tr['+str(r)+']//td[6]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchPlayerByName(self,pname):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//*[@id='example1']//tr['+str(r)+']//td[3]").text
            if name == pname:
                flag = True
                break
        return flag

    def searchPlayerBySchool(self,pschool):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            school=table.find_element(By.XPATH,"//*[@id='example1']//tr['+str(r)+']//td[8]").text
            if school == pschool:
                flag = True
                break
        return flag


