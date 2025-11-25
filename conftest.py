import pytest
from fixtures.browser_fixture import page
from fixtures.allure_fixture import attach_allure_artifacts
from fixtures.test_data_fixture import login_test_data

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        setattr(item, "test_outcome", rep)

