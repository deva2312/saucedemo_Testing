from behave import given, when, then
from selenium.common import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the Demo Login Page')
def step_given_on_demo_login_page(context):

    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account {user_type} into the Username field and the Password field')
def step_when_fill_account_information(context, user_type):
    if user_type == "StandardUser":
        username = "standard_user"
        password = "secret_sauce"
    elif user_type == "LockedOutUser":
        username = "locked_out_user"
        password = "secret_sauce"
    else:
        raise ValueError(f"Unknown user type: {user_type}")

    username_field = context.driver.find_element(By.ID, "user-name")
    password_field = context.driver.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

@when('I click the Login Button')
def step_when_click_login_button(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()


@then('I am redirected to the Demo Main')
def step_then_redirected_to_demo_main(context):
    hamburger_menu = context.driver.find_element(By.CLASS_NAME, "bm-burger-button")
    hamburger_menu.click()
    about_link = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "about_sidebar_link"))
    )
    about_link.click()


@then('I verify the App Logo exists')
def step_then_verify_app_logo_exists(context):
    try:
        logo = context.driver.find_element(By.CSS_SELECTOR, "div.MuiBox-root.css-6ohz81 img[alt='Saucelabs']")
        assert logo.is_displayed(), "App logo is not displayed!"
        print("App logo is displayed correctly.")
    except NoSuchElementException:
        print("App logo not found.")
        raise AssertionError("App logo is not present on the page.")


@then('I verify the Error Message contains the text "{expected_message}"')
def step_then_verify_error_message(context, expected_message):
    error_message_element = context.driver.find_element(By.CSS_SELECTOR, ".error-message-container")
    actual_message = error_message_element.text
    assert expected_message in actual_message, f"Expected error message '{expected_message}', but got '{actual_message}'"



