import os
import pytest
from playwright.sync_api import sync_playwright
from config.settings import BROWSER_CONFIG
from utils.logger import get_logger

logger = get_logger("BrowserFixture")

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser_type = BROWSER_CONFIG["browser"]
    headless = BROWSER_CONFIG["headless"]
    slow_mo = BROWSER_CONFIG["slow_mo"]

    browser = getattr(playwright_instance, browser_type).launch(
        headless=headless,
        slow_mo=slow_mo
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser, request, tmp_path_factory):
    video_setting = BROWSER_CONFIG.get("video", "on")
    trace_setting = BROWSER_CONFIG.get("trace", "on")

    test_name = request.node.name.replace("/", "_").replace(" ", "_")
    video_dir = tmp_path_factory.mktemp("videos")
    context = browser.new_context(
        record_video_dir=str(video_dir) if video_setting == "on" else None,
        viewport=BROWSER_CONFIG.get("viewport")
    )

    if trace_setting == "on":
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context

    if trace_setting == "on":
        trace_dir = os.path.join("reports", "traces")
        os.makedirs(trace_dir, exist_ok=True)
        context.tracing.stop(path=os.path.join(trace_dir, f"{test_name}_trace.zip"))

    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(10000)
    yield page
    page.close()
