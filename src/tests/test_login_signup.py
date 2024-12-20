from src.driver.driver import Driver
from src.pages.login_signup import LoginSignup


class TestLoginSignup(Driver):

    #Test Login Tên Đăng Nhập và mật khẩu chính xác
    def test_login(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("leminhkhoi.cuchi@gmail.com", "123456789")
        login.click_login()
        login.click_menu()
        # Kiểm tra tên hiển thị đúng
        name = login.get_name()
        assert name == "My Account: Lê Minh Khôi", f"Expected name not found. Got {name}."

    def test_login_without_username_and_password(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("", "")
        login.click_login()
        # Kiểm tra tên hiển thị đúng
        alert_message = login.get_alert_message()
        assert alert_message == "The email field is required.\nThe password field is required.", f"Expected name not found. Got {alert_message}."

    def test_login_without_username(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("leminhkhoi.cuchi@gmail.com", "")
        login.click_login()
        # Kiểm tra tên hiển thị đúng
        alert_message = login.get_alert_message()
        assert alert_message == "The password field is required.", f"Expected name not found. Got {alert_message}."

    def test_login_without_password(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("", "123456789")
        login.click_login()
        # Kiểm tra tên hiển thị đúng
        alert_message = login.get_alert_message()
        assert alert_message == "The email field is required.", f"Expected name not found. Got {alert_message}."

    def test_signup_fail_email_exist(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_register()
        login.fill_email_name_and_password("MinhKhoi", "leminhkhoi.cuchi@gmail.com", "123456789", "123456789")
        login.click_signup()
        alert_message = login.get_alert_message()
        assert alert_message == "The email has already been taken.", f"Expected name not found. Got {alert_message}"

    def test_signup_fail_not_match_pass(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_register()
        login.fill_email_name_and_password("MinhKhoi", "leminhkhoi.cuchi@gmail.comm", "123456789", "12345678")
        login.click_signup()
        alert_message = login.get_alert_message()
        assert alert_message == "The password confirmation field must match password.", f"Expected name not found. Got {alert_message}"

    def test_signup_fail_not_enough_infor_field(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_register()
        login.fill_email_name_and_password("", "", "", "")
        login.click_signup()
        alert_message = login.get_alert_message()
        assert alert_message == "The name field is required.\nThe email field is required.\nThe password field is required.\nThe password confirmation field is required.", f"Expected name not found. Got {alert_message}"

    def test_signup_fail_lower_boundary(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_register()
        login.fill_email_name_and_password("MinhKhoi", "leminhkhoi.cuchi@gmail.comm", "9999", "9999")
        login.click_signup()
        alert_message = login.get_alert_message()
        assert alert_message == "The password field must be at least 6 characters.", f"Expected name not found. Got {alert_message}"

    def test_signup_success(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_register()
        login.fill_email_name_and_password("MinhKhoi", "hyhy.cuchi@gmail.com", "123456789", "123456789")
        login.click_signup()
        alert_message = login.get_alert_success_message()
        assert alert_message == "Register successfully", f"Expected name not found. Got {alert_message}"

    def test_forgot_password(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_forgot_password()
        login.fill_email("leminhkhoi.cuchi@gmail.com")
        login.click_confirm()
        login.fill_password("123456789", "123456789")
        login.click_change_password()
        alert_message = login.get_alert_success_message()
        assert alert_message == "Password has been reset successfully!", f"Expected name not found. Got {alert_message}"

    def test_forgot_password_not_match(self, driver):
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_forgot_password()
        login.fill_email("leminhkhoi.cuchi@gmail.com")
        login.click_confirm()
        login.fill_password("123456789", "123456")
        login.click_change_password()
        alert_message = login.get_alert_message()
        assert alert_message == "The password field confirmation does not match.", f"Expected name not found. Got {alert_message}"

    def test_logout(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.click_register()

    def login_ex(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("leminhkhoi.cuchi@gmail.com", "123456789")
        login.click_login()
        login.click_menu()

    def login_exx(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("dugiatien14@gmail.com", "02062003")
        login.click_login()
        login.click_menu()

    def login_exxx(self, driver):
        # Navigate to the home page
        driver.get("http://localhost:8000/")
        login = LoginSignup(driver)
        login.click_menu()
        login.click_account()
        login.fill_name_and_password("dugiatienfg@gmail.com", "02062003")
        login.click_login()
        login.click_menu()