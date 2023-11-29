import pytest
import requests
from generator import *
from static_data import APIUrls


@pytest.fixture
def create_user():
    response, login_pass, token = create_new_user()
    yield response, login_pass, token
    requests.delete(APIUrls.main_url + APIUrls.user_url, headers={'Authorization': f'{token}'})

