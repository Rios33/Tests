from playwright.sync_api import Page, expect


class InventoryPage:
    URL_PART = "/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")

    def expect_opened(self):
        # Упростим проверку URL - проверяем конкретно
        expect(self.page).to_have_url(f"https://www.saucedemo.com{self.URL_PART}")
        # Или просто проверяем, что на странице есть нужные элементы
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Products")
        expect(self.items.first).to_be_visible()