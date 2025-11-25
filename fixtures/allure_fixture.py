import os
import allure
import pytest

@pytest.fixture(autouse=True)
def attach_allure_artifacts(request, page):
    yield
    if request.node.rep_call.failed:  # handled via hook in conftest
        test_name = request.node.name.replace("/", "_").replace(" ", "_")
        screenshot_path = os.path.join("reports", "screenshots", f"{test_name}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        page.screenshot(path=screenshot_path, full_page=True)

        with open(screenshot_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=f"{test_name}_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
