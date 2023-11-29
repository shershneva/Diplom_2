import pytest
import allure
import requests
from conftest import create_user
from static_data import APIUrls, APIErrors


class TestGetOrders:
    @allure.title('Успешное получение списка заказов пользователя с авторизацией')
    def test_get_orders_with_auth_success(self, create_user):
        token = {'Authorization': create_user[2]}
        bun_1 = "61c0c5a71d1f82001bdaaa6d"
        filling_2 = "61c0c5a71d1f82001bdaaa70"
        order = {"ingredients": [bun_1, filling_2, bun_1]}
        post_order = requests.post(APIUrls.main_url + APIUrls.order_url, headers=token, data=order)
        get_order = requests.get(APIUrls.main_url + APIUrls.order_url, headers=token)

        assert get_order.status_code == 200 and get_order.json()['orders'][0]['number'] == post_order.json()['order']['number']

    @allure.title('Получение списка заказов пользователя без авторизации')
    def test_get_orders_without_auth_fail(self, create_user):
        bun_1 = "61c0c5a71d1f82001bdaaa6d"
        filling_2 = "61c0c5a71d1f82001bdaaa70"
        order = {"ingredients": [bun_1, filling_2, bun_1]}
        post_order = requests.post(APIUrls.main_url + APIUrls.order_url, data=order)
        get_order = requests.get(APIUrls.main_url + APIUrls.order_url)
        assert get_order.status_code == 401 and get_order.json()['message'] == APIErrors.error_receive_no_auth

