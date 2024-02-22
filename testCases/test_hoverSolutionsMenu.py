from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Hover_Solutions_Menu:
    baseURL = ReadConfig.getApplicationURL()
    timeout = ReadConfig.getTimeOut()
    logger = LogGen.loggen()

    def test_hover_solutions_menu(self,setup):
        self.logger.info("***************** Test_002_Hover_Solutions_Menu *****************")
        self.logger.info("***************** Hovering on Solutions Menu *****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)
        self.driver.get(self.baseURL)

        self.hp=HomePage(self.driver)
        self.hp.clickAcceptCookies()
        self.hp.hoverSolutionMenu()

        options = self.driver.find_elements(By.XPATH,self.hp.getSubOptionAllSolutions())
        self.logger.info("***************** Verifying options length after hovering on Solutions Menu *****************")
        assert len(options) == 7,self.driver.save_screenshot(".\\Screenshots\\"+"test_hoverSolutionsMenu_scr.png")
        self.driver.close()
        self.logger.info("******* Ending Test_002_Hover_Solutions_Menu **********")