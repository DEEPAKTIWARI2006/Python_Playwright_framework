from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config.settings import BASE_URL

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate_to(BASE_URL)

    def login(self, username: str, password: str):
        self.logger.info(f"Logging in with user: {username}")
        self.page.locator(LoginLocators.USERNAME_INPUT).fill(username)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
        self.page.locator(LoginLocators.LOGIN_BUTTON).click()

    def assert_login_success(self):
        # adjust this based on your app
        expect(self.page).to_have_title(lambda title: "Dashboard" in title)

    def assert_login_failed(self):
        expect(self.page.locator(LoginLocators.ERROR_MESSAGE)).to_be_visible()
