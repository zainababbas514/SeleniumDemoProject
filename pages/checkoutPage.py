from selenium.webdriver.common.by import By
from pages.confirm_page import ConfirmPage
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    checkout_btn = (By.XPATH,"//button[@class='btn btn-success']")

    def click_checkout_btn(self):
        self.click(self.checkout_btn)
        return ConfirmPage(self.driver)



