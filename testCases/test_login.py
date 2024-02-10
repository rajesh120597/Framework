import time
from selenium.webdriver.support import expected_conditions as ec
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import Login
#from utilities.Read_excel_data import Read_data as re
from utilities.Read_excel_data import Read_data


class Test_001_Login():
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.skip
    def test_HomePage_Title(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePage_Title.png")
            assert False

    @pytest.mark.skip
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title = self.driver.title
        if title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            assert False

    @pytest.mark.parametrize("username,password,result", Read_data.get_test_data())
    def test_login_parameterize(self,username, password, result, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, timeout=10)
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.setUserName(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        if result == 'Pass':
            wait.until(ec.title_is("Dashboard / nopCommerce administration"))
            assert self.driver.title == "Dashboard / nopCommerce administration"
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login_parameterize"+username+password+".png")
            assert self.driver.title == "Your store. Login"
            print(self.lp.error_msg())
            assert "Login was unsuccessful. Please correct the errors and try again." in self.lp.error_msg()



