from selenium.webdriver import ActionChains
class HomePage:
    #Locators
    button_signin_xpath="//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/div[1]/div[1]/div[1]/div[3]/a[2]"
    hlogo_entrata_xpath="//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/div[1]/div[1]/div[1]/a[1]/*[1]"
    link_home_logo_xpath="//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]"
    button_accept_cookies_id="rcc-confirm-button"
    menu_solution_xpath="//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]"
    alloptions_solutions_css_selector="//a[contains(text(),'All Solutions') and @class='fat-nav-links']/parent::div/child::a"

    #constructor : invokes on object creation
    def __init__(self,driver):
        self.driver=driver
    def clickSignInMain(self):
        self.driver.find_element("xpath",self.button_signin_xpath).click()
    def clickMainLogo(self):
        self.driver.find_element("xpath",self.hlogo_entrata_xpath).click()
    def getHomeLogo(self):
        return self.link_home_logo_xpath
    def clickAcceptCookies(self):
        self.driver.find_element("id",self.button_accept_cookies_id).click()

    def hoverSolutionMenu(self):
        action=ActionChains(self.driver)
        action.move_to_element(self.driver.find_element("xpath",self.menu_solution_xpath)).perform()

    def getSubOptionAllSolutions(self):
        return self.alloptions_solutions_css_selector