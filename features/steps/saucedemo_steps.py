from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


@given('I am on the Demo Login Page')
def login_page(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when('I fill the account information for account "{user}" into the Username field and the Password field "{pwd}"')
def user_info(context, user, pwd):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@when('I click the Login Button')
def click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('I am redirected to the Demo Main Page')
def home_page(context):
    header_text = context.driver.find_element(By.XPATH, "//span[@class='title']").text
    assert header_text == 'Products'


@then('I verify the App Logo exists')
def verify_logo(context):
    logo = context.driver.find_element(By.XPATH, "//div[text()='Swag Labs']").is_displayed()
    assert logo is True
    context.driver.save_screenshot("/Users/ganeshkumar/PycharmProjects/saucedemo_behave_framework/screenshots/test_success_login.png")
    context.driver.close()


@when('I fill the account information for lock account "{user2}" into the Username field and the Password field "{pwd}"')
def lock_user(context, user2, pwd):
    username = context.driver.find_element(By.ID, "user-name")
    username.clear()
    username.send_keys(user2)
    password = context.driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys(pwd)


@then('I verify the Error Message contains the text "Sorry, this user has been banned.')
def verify_error_msg(context):
    try:
        error_msg = context.driver.find_element(By.XPATH, "//div[@class='error-message-container error']/h3[1]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if error_msg == 'Epic sadface: Sorry, this user has been locked out.':
        context.driver.save_screenshot("/Users/ganeshkumar/PycharmProjects/saucedemo_behave_framework/screenshots/test_fail_login.png")
        context.driver.close()
        assert True, "Test Passed"


@given('I am on the inventory page')
def inventory_page(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()


@when('user sorts products from low price to high price')
def sort_product(context):
    drop = Select(context.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
    drop.select_by_visible_text('Price (low to high)')

@when('user adds lowest priced product')
def add_lowprice_product(context):
    context.driver.find_element(By.XPATH, "//div[@class='inventory_list']/div[1]/descendant::button[1]").click()

@when('user clicks on cart')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']").click()

@when('user clicks on checkout')
def click_chkout(context):
    context.driver.find_element(By.XPATH, "//button[@id='checkout']").click()


@when('user enters first name "{fname}"')
def first_name(context,fname):
    context.driver.find_element(By.ID, "first-name").send_keys(fname)

@when('user enters last name "{lname}"')
def last_name(context,lname):
    context.driver.find_element(By.ID, "last-name").send_keys(lname)

@when('user enters zip code "{zip}"')
def zip_code(context,zip):
    context.driver.find_element(By.ID, "postal-code").send_keys(zip)

@when('user clicks Continue button')
def cont_btn(context):
    continue_button = context.driver.find_element(By.ID, "continue")
    context.driver.execute_script("arguments[0].scrollIntoView();", continue_button)
    continue_button.click()

@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def verify_total_value(context):
    total_value = context.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']").text
    assert total_value == 'Total: $8.63'

@when('user clicks Finish button')
def click_finish_btn(context):
    context.driver.find_element(By.ID, "finish").click()


@then('Thank You header is shown in Checkout Complete page')
def complete_header(context):
    try:
        complete_txt = context.driver.find_element(By.XPATH, "//h2[@class='complete-header']").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if complete_txt == "Thank you for your order!":
        context.driver.save_screenshot("/Users/ganeshkumar/PycharmProjects/saucedemo_behave_framework/screenshots/test_order_product.png")
        context.driver.close()
        assert True, "Test Passed"

