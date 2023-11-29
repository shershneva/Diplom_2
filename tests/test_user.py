import pytest
import allure
import requests
from conftest import create_user
from static_data import APIUrls, APIErrors, TestUser
from generator import generate_random_string


class TestUserCreate:
    @allure.title('Успешная регистрация юзера')
    def test_create_user_new_user_success(self, create_user):
        user = create_user[0]

        assert user.status_code == 200 and user.json()['success'] == True

    @allure.title('Создание существующего юзера')
    def test_create_user_exist_user_fail(self, create_user):
        exist_user = {
            "email": create_user[1][0],
            "password": create_user[1][1],
            "name": create_user[1][2]
        }
        response = requests.post(APIUrls.main_url + APIUrls.signup_url, data=exist_user)

        assert response.status_code == 403 and response.json()['success'] == False and response.json()['message'] == APIErrors.error_create_user_exist

    @allure.title('Создание юзера  без обязательных полей')
    @pytest.mark.parametrize('user_data', (
    TestUser.create_no_login_user, TestUser.create_no_password_user, TestUser.create_empty_login,
    TestUser.create_empty_password))
    def test_create_user_without_required_fields_fail(self, user_data):
        response = requests.post(APIUrls.main_url + APIUrls.signup_url, data=user_data)

        assert response.status_code == 403 and response.json()['message'] == APIErrors.error_create_required_fields


class TestUserLogin:
    @allure.title('Успешная авторизация существующего юзера')
    def test_user_login_success(self, create_user):
        login_user = {"email": create_user[1][0],
                    "password": create_user[1][1]}
        response = requests.post(APIUrls.main_url + APIUrls.signin_url, data=login_user)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Вход с несуществующим юзером')
    def test_user_login_no_such_user_fail(self, create_user):
        login_user = {"email": create_user[1][1],
                        "password": create_user[1][0]}
        response = requests.post(APIUrls.main_url + APIUrls.signin_url, data=login_user)

        assert response.status_code == 401 and response.json()['message'] == APIErrors.error_login_no_such_user


class TestUserUpdate:
    @allure.title('Успешное изменение имени с авторизацией')
    def test_update_user_name_with_auth_success(self, create_user):
        user = create_user
        new_name = generate_random_string(6)
        update_user = {
            "name": new_name
        }
        token = {'Authorization': user[2]}
        response = requests.patch(APIUrls.main_url + APIUrls.user_url, headers=token, data=update_user)

        assert response.json()['success'] == True and response.json()['user']['email'] == user[1][0] and response.json()['user']['name'] == new_name

    @allure.title('Успешное изменение емейла юзера')
    def test_update_user_email_with_auth_success(self, create_user):
        user = create_user
        new_email = f'{generate_random_string(6)}@ya.ru'
        update_user = {
            "email": new_email
        }
        token = {'Authorization': user[2]}
        response = requests.patch(APIUrls.main_url + APIUrls.user_url, headers=token, data=update_user)

        assert response.json()['success'] == True and response.json()['user']['email'] == new_email

    @allure.title('Успешное изменение пароля с авторизацией')
    def test_update_user_password_with_auth_success(self, create_user):
        user = create_user
        new_password = generate_random_string(6)
        update_user = {
            "password": new_password
        }
        token = {'Authorization': user[2]}
        response = requests.patch(APIUrls.main_url + APIUrls.user_url, headers=token, data=update_user)

        assert response.json()['success'] == True and response.json()['user']['email'] == user[1][0] and response.json()['user']['name'] == user[1][2]

    @allure.title('Изменение данных юзера без авторизации')
    @pytest.mark.parametrize('user_data', [
        {'email': f'{generate_random_string(6)}@ya.ru'},
        {'password': generate_random_string(6)},
        {'name': generate_random_string(6)}
    ])
    def test_update_user_data_without_auth_fail(self, user_data):
        response = requests.patch(APIUrls.main_url + APIUrls.user_url, data=user_data)

        assert response.status_code == 401 and response.json()['message'] == APIErrors.error_update_no_auth
