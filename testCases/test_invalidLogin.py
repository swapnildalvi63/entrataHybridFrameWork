from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.PropertyManagerLoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_Invalid_Login:
    baseURL = ReadConfig.getApplicationURL()
    timeout = ReadConfig.getTimeOut()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_invalid_login(self,setup):
        self.logger.info("***************** Test_003_Invalid_Login *****************")
        self.logger.info("***************** Verifying error messages for Property Manager Login Page *****************")
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)
        self.driver.get(self.baseURL)

        self.hp=HomePage(self.driver)
        self.hp.clickAcceptCookies()
        self.hp.clickSignInMain()

        self.lp=LoginPage(self.driver)
        self.lp.clickPropertyManagerLogin()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()

        error_message_element = WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, "//p[@id='statusMessage']"))
        )

        self.logger.info("********* Login validation *****************")

        if 'The username and password provided are not valid. Please try again.' in error_message_element.text:
            assert True
            self.logger.info("********* Invalid login Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_invalidLogin_scr.png")
            self.logger.error("********* Invalid login Test Failed  ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Test_003_Invalid_Login **********")
