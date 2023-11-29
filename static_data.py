class APIUrls:
    main_url = 'https://stellarburgers.nomoreparties.site'
    signup_url = '/api/auth/register'
    signin_url = '/api/auth/login'
    user_url = '/api/auth/user'
    order_url = '/api/orders'

class APIErrors:
    error_create_user_exist = "User already exists"
    error_create_required_fields = "Email, password and name are required fields"
    error_login_no_such_user = "email or password are incorrect"
    error_update_no_auth = "You should be authorised"
    error_receive_no_auth = "You should be authorised"
    error_order_no_data = "Ingredient ids must be provided"


class TestUser:
    create_no_login_user = {"password": "test_password!", "name": "Anyname"}
    create_no_password_user = {"email": "wrong_user1234@ya.ru", "name": "Anyname"}
    create_empty_login = {"email": "", "password": "test_password!", "name": "Anyname"}
    create_empty_password = {"email": "wrong_user1234@ya.ru", "password": "", "name": "Anyname"}


class TestOrder:
    good_order = {"ingredients":  ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6d"]}
    wrong_hash_order = {"ingredients":  ["aa1234", "bb12345", "cc1233"]}

