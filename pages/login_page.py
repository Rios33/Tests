from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(self.URL)
        expect(self.username).to_be_visible()
        expect(self.password).to_be_visible()
        expect(self.login_btn).to_be_visible()

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
        # Добавим небольшую задержку для обработки
        self.page.wait_for_timeout(500)

    def expect_error(self, text_part: str):
        expect(self.error).to_be_visible()
        expect(self.error).to_contain_text(text_part)