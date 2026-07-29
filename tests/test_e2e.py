import pytest
from pages.homePage import HomePage
from test_data.test_e2e_data import test_place_order_data
from utilities.excel_reader import get_test_data
from utilities.logger import get_logger

# @pytest.mark.parametrize("product_name, country", test_place_order_data)
# def test_place_order(setup, product_name, country):
#
#     home_page = HomePage(setup)
#     logger = get_logger()
#
#     logger.info("Clicking the shop button")
#     shop_page = home_page.click_shop_button()
#
#     logger.info(f"Adding {product_name} to the cart")
#
#     shop_page.add_product_to_cart(product_name)
#     checkout_page = shop_page.click_checkout_btn()
#
#     confirm_page = checkout_page.click_checkout_btn()
#     confirm_page.select_country(country)
#     confirm_page.click_terms_conditions_checkbox()
#     confirm_page.click_purchase_btn()
#
#     success_message = confirm_page.get_success_message()
#     assert "Success! Thank you!" in success_message, "The order is not placed"
#

@pytest.mark.parametrize("data", get_test_data("TC001", "C:\\Users\\LENOVO\\Downloads\\testdata (1).xlsx", "PlaceOrder"))
def test_place_order(setup, data):

    home_page = HomePage(setup)
    logger = get_logger()

    logger.info("Clicking the shop button")
    shop_page = home_page.click_shop_button()

    logger.info(f"Adding {data["Product"]} to the cart")
    shop_page.add_product_to_cart(data["Product"])

    logger.info(f"Clicking checkout button")
    checkout_page = shop_page.click_checkout_btn()

    confirm_page = checkout_page.click_checkout_btn()
    confirm_page.select_country(data["Country"])
    confirm_page.click_terms_conditions_checkbox()
    confirm_page.click_purchase_btn()

    success_message = confirm_page.get_success_message()
    assert "Success! Thank you!" in success_message, "The order is not placed"




