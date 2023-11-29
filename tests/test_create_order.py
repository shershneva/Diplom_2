import allure
import requests
from conftest import create_user
from static_data import APIUrls, APIErrors, TestOrder


class TestCreateOrder:
    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_with_auth_success(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(APIUrls.main_url + APIUrls.order_url, headers=token, data=TestOrder.good_order)

        assert post_order.status_code == 200 and post_order.json()['success'] == True

    @allure.title('Успешное cоздание заказа без авторизации')
    def test_create_order_without_auth_success(self, create_user):
        post_order = requests.post(APIUrls.main_url + APIUrls.order_url, data=TestOrder.good_order)

        assert post_order.status_code == 200 and post_order.json()['success'] == True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_fail(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(APIUrls.main_url + APIUrls.order_url, headers=token)

        assert post_order.status_code == 400 and post_order.json()['message'] == APIErrors.error_order_no_data

    @allure.title('Создание заказа при неверном хеше ингредиентов')
    def test_create_order_wrong_hash_fail(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(APIUrls.main_url + APIUrls.order_url, headers=token, data=TestOrder.wrong_hash_order)
        assert post_order.status_code == 500
