import time
import os
from selenium import webdriver
#import page object model file
from pom import OrangeHRM

# testcase01_forgot passord link sent
def test1_forgot_link(browser):
    login_page =OrangeHRM(browser)
    login_page.forgot_link("Admin")
    print("Reset Password link sent successfully")
#test case_for login the application
def test2_validlogin(browser):
    login_page =OrangeHRM(browser)
    login_page.valid_login("Admin","admin123")
    print("The user is logged in successfully")

# verify admin tab menu elements
def test3_admintabmenu(browser):
    #login the bowser
    login_page =OrangeHRM(browser)
    login_page.valid_login("Admin", "admin123")
    actual_items = login_page.get_adminmenu_items()
    expected_menu=['User Management', 'Job', 'Organization', 'Qualifications', 'Nationalities', 'Corporate Branding', 'Configuration']
   # compare the menu elements
    if actual_items==expected_menu:
        print("all menu present successfully")
    else:
        print("invalid all menu not present")

#test_case3 verify the dashboard menu elements
def test4_dashboardmenu(browser):
        #login the browser
    login_page =OrangeHRM(browser)
    login_page.valid_login("Admin", "admin123")
    actual_items=login_page.get_dashboradmenu_items()
    expected_menu=['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']
    #compare all the menu elements
    if actual_items==expected_menu:
        print("all menu present successfully")
    else:
        print("invalid all menu not present")
