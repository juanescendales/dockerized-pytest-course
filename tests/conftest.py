"""
Note:
Fixtures with @pytest.fixture(scope="session", autouse=True) must remain in this file
"""
pytest_plugins = [
    "tests.utility.cities",
    "tests.utility.data_processing",
 ]
