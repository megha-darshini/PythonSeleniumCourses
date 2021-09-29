from selenium.webdriver.common.by import By

class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR,'tr.cart_item td.product-name')
    COUPON_FILED = (By.ID,'coupon_code')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR,'button[name="apply_coupon"]')
    CART_PAGE_MSG = (By.CLASS_NAME,'woocommerce-message')
    FREE_SHIPPING = (By.ID,'shipping_method_0_free_shipping2')
    PROCEED_BTN = (By.CSS_SELECTOR,'a.checkout-button')
    CHECKOUT_MSG = (By.CSS_SELECTOR, 'h1.entry-title')