import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_valid_login(page, login_test_data):
    # Take only the first row for now
    test_row = login_test_data[0]
    username = test_row["username"]
    password = test_row["password"]

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    #login_page.assert_login_success()
