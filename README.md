# MASA-AdminPanel-Backend--AutomationTesting
Mayungano Amuka Soccer Academy(MASA)AdminPanel(Backend)"https://mayunganoamukasocceracademy.000webhostapp.com/admin" -is an online Soccer academy website for administrator for MAsa to perform
different tasks. 

For this project, i used windows(operating system), python(programming language), selenium(automation), pytest(python testing framework), pytest-html(pytest HTML Reports)

The following were  the steps for the MASA-AdminPanel(Backend)-Automation Testing;

Step1: Install and configure Python on windows.

Step2: Identify any Python Intergarted Development Environment and code editors(Pycharm)integrate and install it on operating system(Windows).

step3: Create new project and install/configure in the project-->Settings-->Python Interpreter--> + -->search the required packages/plugins-->Install Plugins;

       -Selenium: Selenium libraries for identifying several elements on the webpage.
       
       -Pytest: Python UnitTest framework.
       
       -Pytest-HTML: for generating Pytest HTML Reports.
       
       -Pytest-xdist: for running tests parallel on the same or differnet web browsers.
       
       -Openpyxl: for microsoft Excel support.
       
 Step4: Create/Design Folder Structure 
      Project Name(MASA-AdminPanel-Backend--AutomationTesting)
      
           Configurations(Package)
           
           Logs(Folder)
           
           PageObjects(Package)
           
           Reports(Folder)
           
           Screenshots(Folder)
           
           testCases(Package)
           
           testData(Folder)
           
           Utilities(Package)
           
Step5: Automating Login Test Case

     5.1: Creating the loginPage.py under "pageObjects" Package to identify webpage elements for the login page.
     
     5.2: create test_login.py under "testCases" Package as a test case for login page.
     
     5.3: create confest.py under "testCases" Package.
     
     5.4: Capture screenshot on failure and create a screenshot as "../Screenshot/" + "testcase Name.png" under "screenshot" folder
     
     5.5: Run the login test case(test_login.py):cd \"file location"\pytest -v -s test_login.py in windows powershell/command prompt or Pycharm terminal.
     
Step6: Read common values from ini file

     6.1: Add "config.ini" file in "Configurations" folder.
     
     6.2: Create "readProperties.py" utility file under utilities package to read common data.
     
     6.3: Replace hard coded values in test_login case.
     
     6.4: Run step 5.5.
     
Step7: Adding logs to testcase

     7.1: create customLogger.py under "Utilities" package
     
     7.2: Add logs to login testCase
     
Step8: Generate pytest HTML Reports

     8.1: To generate HTML report run below command:
     
        Run step 5.5\--html=..\Reports\report.html
        
Step9: Automating Data Driven Test Case

     9.1: Prepare testData in Excel sheet(loginData.xlsx), place the excel file inside the testData folder
     
     9.2: Create "XLUtils.py" utility class under "Utilities" package
     
     9.3: Create test_login_ddt.py under "testCases" pacakage
     
     9.2: Run step 8.1
     
Step10: Adding new test cases under "testCases" package

     10.1: test_addPlayer.py to add new player
     
     10.2: test_searchPlayerByEmail to search a player by Email
     
     10.3: test_searchPlayerByName to search a player by Name
     
     10.4: test_searchPlayerBySchool to search a player by Current School
     
Step11: Create Group tests

    11.1: Group markers(Add markers to every test method) as follows;
    
         11.1.1: @pytest.mark.sanity
         
         11.1.2: @Pytest.mark.regression
         
    11.2: Add/Register marker entries in pytest.in file under "testCases" package.
    
    11.3: Select groups at run time
        
        -m "sanity"
        
        -m "regression"
        
    11.4: Run command: pytest -v -s -m "sanity"
    
         
        
     
     
      
     
 
       
