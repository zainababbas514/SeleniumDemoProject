from selenium.webdriver.common.by import By
from pages.checkoutPage import CheckoutPage
from pages.base_page import BasePage

class ProductPage(BasePage):

    products = (By.XPATH,"//div[@class='card h-100']")
    product_name = (By.XPATH, "div/h4/a")
    add_to_card_btn = (By.XPATH, "div/button")
    checkout_btn = (By.CSS_SELECTOR,"a[class*='btn-primary']")

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(*self.products)

        for product in products:
            name = product.find_element(*self.product_name).text

            if product_name == name:
                product.find_element(*self.add_to_card_btn).click()
                return

        raise Exception(f"Product {product_name} does not exist")

    def click_checkout_btn(self):
        self.click(self.checkout_btn)
        return CheckoutPage(self.driver)

