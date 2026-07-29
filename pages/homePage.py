from pages.productPage import ProductPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    shop_button = (By.CSS_SELECTOR," a[href*='shop']")

    def click_shop_button(self):
        self.click(self.shop_button)
        return ProductPage(self.driver)

