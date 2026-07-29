from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class ConfirmPage(BasePage):

    country_dropdown = (By.ID,"country")
    terms_conditions_checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchase_btn = (By.CSS_SELECTOR,"[type='submit']")
    success_text = (By.CLASS_NAME,"alert-success")

    def select_country(self, country):
        self.send_keys(self.country_dropdown, country)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, country)))
        self.click((By.LINK_TEXT, country))

    def click_terms_conditions_checkbox(self):
        self.click(self.terms_conditions_checkbox)

    def click_purchase_btn(self):
        self.click(self.purchase_btn)

    def get_success_message(self):
        return self.get_text(self.success_text)




