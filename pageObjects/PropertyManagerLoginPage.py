class LoginPage:
    btn_property_manager_xpath="//a[contains(text(),'Property Manager Login')]"
    txtbox_username_xpath="//input[@id='entrata-username']"
    txtbox_password_xpath="//input[@id='entrata-password']"
    btn_signin_xpath="//button[contains(text(),'Sign In')]"

    #constructor : invokes on object creation
    def __init__(self,driver):
        self.driver=driver

    def clickPropertyManagerLogin(self):
        self.driver.find_element("xpath", self.btn_property_manager_xpath).click()

    def setUserName(self, username):
        self.driver.find_element("xpath",self.txtbox_username_xpath).clear()
        self.driver.find_element("xpath",self.txtbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("xpath",self.txtbox_password_xpath).clear()
        self.driver.find_element("xpath",self.txtbox_password_xpath).send_keys(password)

    def clickSignIn(self):
        self.driver.find_element("xpath", self.btn_signin_xpath).click()

