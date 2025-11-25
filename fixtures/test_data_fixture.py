import pytest
from utils.excel_reader import get_excel_data

@pytest.fixture(scope="module")
def login_test_data():
    # Excel -> sheet "ValidLogin"
    return get_excel_data("ValidLogin")
