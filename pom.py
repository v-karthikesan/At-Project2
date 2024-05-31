from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

#locators for fogot login page
txt_Name = "username"
txtPassword_Name = "password"
buttontxt_Xpath = "//button[@type='submit']"
hoverpim_xpath = "//span[normalize-space()='PIM']"
forgclick_xpath="//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
success_message_xpath="//h6[normalize-space()='Reset Password link sent successfully']"
#locator for admin menu element
hoveradmin_xpath="//span[normalize-space()='Admin']"
namematch_xpath="//nav[@aria-label='Topbar Menu']//ul//li"
#locator for dashboard path
dashboardmatch_xpath="//ul[@class='oxd-main-menu']//li"

class OrangeHRM:
    #definr the browser
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

#create function for click forgot password link
    def forgot_link(self, username):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, forgclick_xpath))).click()
        self.wait.until(EC.visibility_of_element_located((By.NAME, txt_Name))).send_keys(username)
        #click reset button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, buttontxt_Xpath))).click()
        #print the success message
        success_message_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, success_message_xpath)))
        success_message=success_message_element.text
        print(success_message)

     #create the function for login the application
    def valid_login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.NAME, txt_Name))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.NAME, txtPassword_Name))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, buttontxt_Xpath))).click()

#create function for get the menu items in the admin and print
    def get_adminmenu_items(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, hoveradmin_xpath))).click() #click admin tab
        #get the menu elements
        menu_elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, namematch_xpath)))
        menu_items = [element.text for element in menu_elements]
        print("Menu items:", menu_items)
        return menu_items


    #create the function for get the dashboard menu items and print
    def get_dashboradmenu_items(self):
        #locate the menu elements
        dashboard_menu_elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, dashboardmatch_xpath)))
        dashboard_menu_items = [element.text for element in dashboard_menu_elements]
        print("Menu items:", dashboard_menu_items)
        return dashboard_menu_items  #return the menu items

