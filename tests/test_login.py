import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Login")
class TestLogin:
    @allure.story("Успешный логин")
    def test_success_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.expect_opened()

    @allure.story("Неверный пароль")
    def test_wrong_password(self, page):
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "wrong_pass")
        login.expect_error("Username and password do not match")

    @allure.story("Заблокированный пользователь")
    def test_locked_user(self, page):
        login = LoginPage(page)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        login.expect_error("locked out")

    @allure.story("Пустые поля")
    def test_empty_fields(self, page):
        login = LoginPage(page)
        login.open()
        login.login("", "")
        login.expect_error("Username is required")

    @allure.story("Performance glitch user")
    def test_performance_user(self, page):
        login = LoginPage(page)
        login.open()
        login.login("performance_glitch_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.expect_opened()