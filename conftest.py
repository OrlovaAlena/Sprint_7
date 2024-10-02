
import pytest
from src.helper import register_new_courier_and_return_login_password


@pytest.fixture
def create_new_courier():
    courier = register_new_courier_and_return_login_password()
    return courier
