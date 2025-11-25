from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger("BasePage")

class BasePage:
    """
    Base page object that all page objects will inherit from.
    Contains common methods and utilities for page interactions.
    """
    
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)   # 👈 initialize logger
    
    def navigate_to(self, url: str):
        """Navigate to the specified URL"""
        logger.info(f"Navigating to {url}")
        self.page.goto(url)
    
    def click(self, locator: str, timeout: int = None):
        """Click on an element"""
        logger.debug(f"Clicking element with locator: {locator}")
        self.page.click(locator, timeout=timeout)
    
    def fill(self, locator: str, text: str, timeout: int = None):
        """Fill a text field"""
        logger.debug(f"Filling text '{text}' in element with locator: {locator}")
        self.page.fill(locator, text, timeout=timeout)
    
    def get_text(self, locator: str, timeout: int = None) -> str:
        """Get text from an element"""
        logger.debug(f"Getting text from element with locator: {locator}")
        return self.page.text_content(locator, timeout=timeout)
    
    def is_visible(self, locator: str, timeout: int = None) -> bool:
        """Check if an element is visible"""
        logger.debug(f"Checking visibility of element with locator: {locator}")
        return self.page.is_visible(locator, timeout=timeout)
    
    def wait_for_element(self, locator: str, timeout: int = None):
        """Wait for an element to be visible"""
        logger.debug(f"Waiting for element with locator: {locator}")
        self.page.wait_for_selector(locator, state="visible", timeout=timeout)
    
    def take_screenshot(self, path: str):
        """Take a screenshot"""
        logger.info(f"Taking screenshot and saving to {path}")
        self.page.screenshot(path=path)