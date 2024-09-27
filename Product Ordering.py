from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Login import step_when_fill_account_information,step_when_click_login_button
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@given('I am on the inventory page')
def step_given_on_inventory_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/")
    step_when_fill_account_information(context,"StandardUser")
    step_when_click_login_button(context)
    assert "inventory.html" in context.driver.current_url, "Not on the inventory page"


@when('user sorts products from high price to low price')
def step_when_user_sorts_high_to_low(context):
    sort_dropdown = Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("hilo")


@when('user adds highest priced product')
def step_when_user_adds_highest_priced_product(context):
    add_to_cart_button = context.driver.find_elements(By.CLASS_NAME, "btn_inventory")[
        0]
    add_to_cart_button.click()


@when('user clicks on cart')
def step_when_user_clicks_cart(context):
    cart_button = context.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    assert "cart.html" in context.driver.current_url, "Not on the cart page"


@when('user clicks on checkout')
def step_when_user_clicks_checkout(context):
    checkout_button = context.driver.find_element(By.ID, "checkout")
    checkout_button.click()
    assert "checkout-step-one.html" in context.driver.current_url, "Not on the checkout page"


@when('user enters first name {first_name}')
def step_when_user_enters_first_name(context, first_name):
    first_name_field = context.driver.find_element(By.ID, "first-name")
    first_name_field.send_keys(first_name)


@when('user enters last name {last_name}')
def step_when_user_enters_last_name(context, last_name):
    last_name_field = context.driver.find_element(By.ID, "last-name")
    last_name_field.send_keys(last_name)


@when('user enters zip code {zip_code}')
def step_when_user_enters_zip_code(context, zip_code):
    zip_code_field = context.driver.find_element(By.ID, "postal-code")
    zip_code_field.send_keys(zip_code)


@when('user clicks Continue button')
def step_when_user_clicks_continue_button(context):
    continue_button = context.driver.find_element(By.ID, "continue")
    continue_button.click()
    assert "checkout-step-two.html" in context.driver.current_url, "Not on the checkout overview page"


@then('I verify in Checkout overview page if the total amount for the added item is $49.99')
def step_then_verify_total_amount(context):
    item_total = context.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert item_total == "$49.99", f"Expected $49.99 but got {item_total}"


@when('user clicks Finish button')
def step_when_user_clicks_finish_button(context):
    finish_button = context.driver.find_element(By.ID, "finish")
    finish_button.click()
    assert "checkout-complete.html" in context.driver.current_url, "Not on the checkout complete page"


@then('Thank You header is shown in Checkout Complete page')
def step_then_verify_thank_you_header(context):
    thank_you_header = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert thank_you_header == "Thank you for your order!", "Thank You header not found"

