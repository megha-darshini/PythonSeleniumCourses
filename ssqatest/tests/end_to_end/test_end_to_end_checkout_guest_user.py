from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
from ssqatest.src.helpers.datebase_helpers import get_order_from_db_by_order_no
import pytest

#pytest -m tcid33 -s --pdb --html=results/my_report.html --self-contained-html


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:


    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)


        # goto home page
        home_p.goto_home_page()
        #add 1 item to cart
        home_p.click_first_add_item_to_cart()
        #home_p.click_second_add_item_to_cart()
        #make sure cart is updated
        header.wait_until_cart_item_count(1)
        #gotp cart
        header.click_on_cart_on_right_header()
        #get names of all products in cart
        product_names = cart_p.get_all_products_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        #apply free cupon
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)
        #select free shipping
        #cart_p.select_shipping()
        #click proced to cehckout
        cart_p.click_proceed_btn()
        #fil the form
        checkout_p.fillin_billing_info()
        #click place order
        checkout_p.click_place_order()

        #verify order received
        order_received_p.verify_order_received_page()
        #verify order is received in db (sql/api)
        order_no = order_received_p.get_order_number()
        print("*************")
        print(order_no)
        print("*************")

        db_order = get_order_from_db_by_order_no(order_no)
        assert db_order,f"Order No: {order_no} not found in DB"

        print("*****")
        print("PASS")
        print("*****")

#export BROWSER='chrome'
#export DB_USER=root
#export DB_PASSWORD=root