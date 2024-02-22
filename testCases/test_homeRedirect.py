from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_HomePage_Redirect:
    baseURL = ReadConfig.getApplicationURL()
    timeout = ReadConfig.getTimeOut()
    logger = LogGen.loggen()

    def test_homePageRedirect(self,setup):
        self.logger.info("***************** Test_001_HomePage_Redirect *****************")
        self.logger.info("***************** Verifying 'entrata' Home Logo redirects to Home Page *****************")
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)
        self.driver.get(self.baseURL)

        self.hp=HomePage(self.driver)
        self.hp.clickAcceptCookies()
        self.hp.clickSignInMain()
        self.hp.clickMainLogo()

        WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located((By.XPATH, self.hp.getHomeLogo()))
        )

        act_title=self.driver.title

        if(act_title=="Property Management Software | Entrata"):
            assert True
            self.driver.close()
            self.logger.info("*****************  Home Page Redirect Test Case Pass *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle_scr.png")
            self.driver.close()
            self.logger.error("*****************  Home Page Redirect Test Case Fail *****************")
            assert False

        self.logger.info("******* Ending Test_001_HomePage_Redirect **********")
