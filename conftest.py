import pytest
import helpers

@pytest.fixture
def courier_account(): 
    courier_info = helpers.create_courier()
    yield courier_info
    helpers.delete_courier(courier_info)

@pytest.fixture
def created_courier_account(): 
    courier_info = helpers.create_courier(register=True)
    yield courier_info
    helpers.delete_courier(courier_info)