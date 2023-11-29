# Diplom_2
## Автотесты для API сайта Stellar Burgers ## 
Используются библиотеки random и string для тестовых данных. 
Для запросов используются библиотеки json и requests.
Для генерации отчетов используется библиотека allure, для запуска тестов pytest.

### Файл generator содержит функции: ###
generate_random_string - генерация строки заданной длины
create_new_user - генерация нового пользователя

### Файл static_data: ###
содержит тестовые ссылки, тексты ошибок и другие статические данные

## TestUserCreate ##
* test_create_user_new_user_success — Успешная регистрация юзера
* test_create_user_exist_user_fail — Создание существующего юзера
* test_create_user_without_required_fields_fail — Создание юзера  без обязательных полей


## TestUserLogin ##
* test_user_login_success — Успешная авторизация существующего юзера
* test_user_login_no_such_user_fail — Вход с несуществующим юзером


## TestUserUpdate ##
* test_update_user_name_with_auth_success — Успешное изменение пароля с авторизацией
* test_update_user_email_with_auth_success — Успешное изменение емейла с авторизацией
* test_update_user_password_with_auth_success — Успешное изменение имени с авторизацией
* test_update_user_data_without_auth_fail — Изменение данных юзера без авторизации


## TestCreateOrder ##
* test_create_order_with_auth_success — Успешное создание заказа с авторизацией
* test_create_order_without_auth_success — Успешное cоздание заказа без авторизации
* test_create_order_without_ingredients_fail — Создание заказа без ингредиентов
* test_create_order_wrong_hash_fail — Создание заказа при неверном хеше ингредиентов


## TestGetOrders ##
* test_get_orders_with_auth_success — Успешное получение списка заказов пользователя с авторизацией
* test_get_orders_without_auth_fail — Получение списка заказов пользователя без авторизации

