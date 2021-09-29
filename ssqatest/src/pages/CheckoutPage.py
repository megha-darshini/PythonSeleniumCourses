from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password
import time
class CheckoutPage(CheckoutPageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self,first_name=None):
        first_name = first_name if first_name else 'TestFname'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD,first_name)

    def input_billing_last_name(self,last_name=None):
        last_name = last_name if last_name else 'TestLname'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD,last_name)

    def input_billing_street_address(self, address1=None):
        address1 = address1 if address1 else 'TestAddress1'
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, address1)

    def input_billing_city(self, city=None):
        city = city if city else 'TestCity'
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zipcode(self, zipcode=None):
        zipcode = zipcode if zipcode else 'TestAddress1'
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zipcode)

    def input_billing_phone(self, phone=None):
        phone = phone if phone else 'TestAddress1'
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)

    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    def fillin_billing_info(self,first_name=None,last_name=None,address1=None,city=None,zipcode=None,phone=None,email=None):
        self.input_billing_first_name(first_name=first_name)
        self.input_billing_last_name(last_name=last_name)
        self.input_billing_street_address(address1=address1)
        self.input_billing_city(city=city)
        self.input_billing_zipcode(zipcode=560040)
        self.input_billing_phone(phone=12333)
        self.input_billing_email(email=email)

    def click_place_order(self):
        time.sleep(2)
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)

        #element = self.sl.wait_and_click(self.PLACE_ORDER_BTN)
        #self.driver.execute_script("arguments[0].click();", element)

        #element = self.sl.wait_and_click(self.PLACE_ORDER_BTN)
        #self.webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()