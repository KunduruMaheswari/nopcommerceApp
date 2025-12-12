import time
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    baseURL=ReadConfig.getURL()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("********Test_001_Login******")
        self.logger.info("********Test_HomePageTitle is started******")
        self.driver=setup
        self.driver.get(self.baseURL)
        page_title=self.driver.title
        if page_title == 'nopCommerce demo store. Login':
            self.driver.close()
            self.logger.info("********Test_HomePageTitle is passed******")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********Test_HomePageTitle is failed******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********test_login is started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        page_title1=self.driver.title
        if page_title1=='Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info("********test_login is passed******")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.driver.close()
            self.logger.error("********test_login is failed******")
            assert False
