from behave import given, when, then
from pages.login_page import LoginPage
from config.settings import BASE_URL
from playwright.sync_api import expect

@given("I navigate to the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open(BASE_URL)

@when("I enter valid username and password")
def step_enter_credentials(context):
    context.login_page.login("admin", "Admin@123")

@when("I click on login button")
def step_click_login(context):
    pass  # action performed in login()

@then("I should see dashboard page")
def step_verify_dashboard(context):
    expect(context.page.get_by_text("Dashboard")).to_be_visible()
