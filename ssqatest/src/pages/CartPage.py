from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass

    def get_all_products_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        return product_names

    def input_coupon(self,coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FILED,coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def get_displayed_msg(self):
        txt = self.sl.wait_and_get_text(self.CART_PAGE_MSG)
        return txt

    def apply_coupon(self,coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()
        success_msg = self.get_displayed_msg()
        assert success_msg == 'Coupon code applied successfully.', f"Unexpected message when coupon is applied"

    def select_shipping(self):

        self.sl.wait_and_click(self.FREE_SHIPPING)

    def get_checkout_page_display(self):
        txt = self.sl.wait_and_get_text(self.CHECKOUT_MSG)
        return txt

    def click_proceed_btn(self):
        self.sl.wait_and_click(self.PROCEED_BTN)
        #element = self.sl.wait_and_click(self.PROCEED_BTN)
        #self.driver.execute_script("arguments[0].click();", element)

        #element = self.sl.wait_and_click(self.PROCEED_BTN)
        #self.webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()
        success_msg = self.get_checkout_page_display()
        assert success_msg == 'Checkout', f"Unexpected message after proceeding to checkout"
