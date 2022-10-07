from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


class AddPlayer:
    #linkTeamPlayer_menu_xpath="//li[@class='treeview']//a[@href='#']" #team player menu link
    linkTeamPlayer_menu_xpath="/html/body/div[1]/aside/div/section/ul/li[3]/a"
    #linkManagePlayer_menuitem_xpath="//a[normalize-space()='Manage Players']" #manage player menu item  link
    linkManagePlayer_menuitem_xpath="/html[1]/body[1]/div[1]/aside[1]/div[1]/section[1]/ul[1]/li[3]/ul[1]/li[2]/a[1]"
    #btnAddPlayer_xpath="//a[normalize-space()='Add Player']" #add player button
    btnAddPlayer_xpath="/html/body/div/div/section[1]/div[2]/a"
    #Player's Details
    #picLocation="C:\\Users\CMI\Downloads\jerseys\Screenshot_20220708_160824.jpg"
    btnAddPhoto_name="logo"
    txtplayerFullname_name="fullname"
    radioMaleGender_xpath="//input[@value='Male']"
    radioFemaleGender_xpath="//input[@value='Female']"
    dateplayerDOB_name = "dob"
    txtplayerEmail_name="email"
    txtplayerPassword_name="password"
    txtplayerSchool_name="school"
    dropdownplayerNationality_xpath="/html/body/div[1]/div/section[2]/div/div/form/div/div/div[8]/div/span"
    dropdownplayerNationality_xpath2="//input[@role='textbox']"
    dropdownplayerClass_xpath="/html/body/div[1]/div/section[2]/div/div/form/div/div/div[9]/div/span"
    dropdownplayerClass_xpath2="//input[@role='textbox']"
    dropdownplayerProgramme_xpath="/html/body/div[1]/div/section[2]/div/div/form/div/div/div[10]/div/span"
    dropdownplayerProgramme_xpath2="//input[@role='textbox']"
    txtplayerSeason_name="session"
    #Parents and Guardian
    #Father's Details
    txtfatherName_name="fathername"
    txtareafatherresidence_xpath="//body/div[@class='wrapper']/div[@class='content-wrapper']/section[@class='content']/div[@class='row']/div[@class='col-md-12']/form[@class='form-horizontal']/div[@class='box box-info']/div[@class='box-body']/div[13]/div[1]/div[1]/div[3]/div[2]"
    txtfatherMobile_name="fathermobile"
    txtfatherEmail_name="fatheremail"
    #Mother's Details
    txtmotherName_name="mothername"
    txtareamotherResidence_xpath="//body/div[@class='wrapper']/div[@class='content-wrapper']/section[@class='content']/div[@class='row']/div[@class='col-md-12']/form[@class='form-horizontal']/div[@class='box box-info']/div[@class='box-body']/div[17]/div[1]/div[1]/div[3]/div[2]"
    txtmotherMobile_name="mothermobile"
    txtmotherEmail_name="motheremail"
    #Guardian's Details
    txtguardianName_name="guardianname"
    txtguardianMobile_name="guardianmobile"
    #submit button
    btnSubmit_xpath="//button[@name='form1']"
    msgInfo_xpath="//div[@class='box box-info']"

    def __init__(self,driver): #define the constructor method
        self.driver=driver

    def clickteamPlayerMenu(self): #Define the method for Team Player Menu
        self.driver.find_element(By.XPATH,self.linkTeamPlayer_menu_xpath).click()

    def clickmanagePlayerMenuitem(self): # define the method for manage player menu item
        self.driver.find_element(By.XPATH,self.linkManagePlayer_menuitem_xpath).click()

    def clickaddPlayerButton(self): #Define the method for add player button
        self.driver.find_element(By.XPATH,self.btnAddPlayer_xpath).click()

    def browsePlayerPhoto(self):  #Define the method for browse the player photo
        self.driver.find_element(By.NAME,self.btnAddPhoto_name).send_keys("C:\\Users\CMI\Downloads\jerseys\Screenshot_20220708_160824.jpg")

    def setplayerFullname(self,pfullname): #define the method for player's fullname
        self.driver.find_element(By.NAME,self.txtplayerFullname_name).clear()
        self.driver.find_element(By.NAME,self.txtplayerFullname_name).send_keys(pfullname)

    def setplayerGender(self,gender): #define the method for player's gender
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.radioMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH,self.radioFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.radioMaleGender_xpath).click()

    def setplayerDOB(self,dob): #Define the method for player's Date of Birth
        self.driver.find_element(By.NAME,self.dateplayerDOB_name).send_keys(dob)

    def setplayerEmail(self,email): #define the method for Player's email
        self.driver.find_element(By.NAME,self.txtplayerEmail_name).clear()
        self.driver.find_element(By.NAME,self.txtplayerEmail_name).send_keys(email)

    def setplayerPassword(self,password): #Define the method for Player's password
        self.driver.find_element(By.NAME,self.txtplayerPassword_name).clear()
        self.driver.find_element(By.NAME,self.txtplayerPassword_name).send_keys(password)

    def setplayerSchool(self,school): #Define the method for player's Current school
        self.driver.find_element(By.NAME,self.txtplayerSchool_name).clear()
        self.driver.find_element(By.NAME,self.txtplayerSchool_name).send_keys(school)

    def setplayerNationality(self,nationality): #Define the method for player's nationality
        self.driver.find_element(By.XPATH,self.dropdownplayerNationality_xpath).click()
        self.driver.find_element(By.XPATH,self.dropdownplayerNationality_xpath2).clear()
        self.driver.find_element(By.XPATH,self.dropdownplayerNationality_xpath2).send_keys(nationality)

    def setplayerClass(self,pclass): #Define the method for player's Class
        self.driver.find_element(By.XPATH,self.dropdownplayerClass_xpath).click()
        self.driver.find_element(By.XPATH,self.dropdownplayerClass_xpath2).clear()
        self.driver.find_element(By.XPATH,self.dropdownplayerClass_xpath2).send_keys(pclass)

    def setplayerProgramme(self,programme): #Define the method for the player's programme
        self.driver.find_element(By.XPATH,self.dropdownplayerProgramme_xpath).click()
        self.driver.find_element(By.XPATH,self.dropdownplayerProgramme_xpath2).clear()
        self.driver.find_element(By.XPATH,self.dropdownplayerProgramme_xpath2).send_keys(programme)

    def setplayerSeason(self,season): #Define the method for the player's season
        self.driver.find_element(By.NAME,self.txtplayerSeason_name).send_keys(season)

    def setfatherFullname(self,fname): #Define the method for father's Fullname
        self.driver.find_element(By.NAME,self.txtfatherName_name).clear()
        self.driver.find_element(By.NAME,self.txtfatherName_name).send_keys(fname)

    def setfatherresidence(self,fresidence): #Definbe the method for father's residence
        self.driver.find_element(By.XPATH,self.txtareafatherresidence_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtareafatherresidence_xpath).send_keys(fresidence)

    def setfatherMobile(self,fmobile): #Define the method for father's mobile
        self.driver.find_element(By.NAME,self.txtfatherMobile_name).clear()
        self.driver.find_element(By.NAME,self.txtfatherMobile_name).send_keys(fmobile)

    def setfatherEmail(self,femail): #Define the method for the father's email
        self.driver.find_element(By.NAME,self.txtfatherEmail_name).clear()
        self.driver.find_element(By.NAME,self.txtfatherEmail_name).send_keys(femail)

    def setmotherFullname(self,mname): #Define the method for mother's Fullname
        self.driver.find_element(By.NAME,self.txtmotherName_name).clear()
        self.driver.find_element(By.NAME,self.txtmotherName_name).send_keys(mname)

    def setmotherresidence(self,mresidence): #Definbe the method for mother's residence
        self.driver.find_element(By.XPATH,self.txtareamotherResidence_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtareamotherResidence_xpath).send_keys(mresidence)

    def setmotherMobile(self,mmobile): #Define the method for mother's mobile
        self.driver.find_element(By.NAME,self.txtmotherMobile_name).clear()
        self.driver.find_element(By.NAME,self.txtmotherMobile_name).send_keys(mmobile)

    def setmotherEmail(self,memail): #Define the method for the mother's email
        self.driver.find_element(By.NAME,self.txtmotherEmail_name).clear()
        self.driver.find_element(By.NAME,self.txtmotherEmail_name).send_keys(memail)

    def setguardianFullname(self,gname): #Define the method for guardian's Fullname
        self.driver.find_element(By.NAME,self.txtguardianName_name).clear()
        self.driver.find_element(By.NAME,self.txtguardianName_name).send_keys(gname)

    def setguardianMobile(self,gmobile): #Define the method for guardian's mobile
        self.driver.find_element(By.NAME,self.txtguardianMobile_name).clear()
        self.driver.find_element(By.NAME,self.txtguardianMobile_name).send_keys(gmobile)

    def clicksubmitButton(self): #Define the method for the submit/save button
        self.driver.find_element(By.XPATH,self.btnSubmit_xpath).click()

    def getmsgInfo(self):
        self.driver.find_element(By.XPATH,self.msgInfo_xpath)

