from ssqatest.src.pages.locators.MyAccountSingedInLocators import MyAccountSingedInLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSingedInLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)