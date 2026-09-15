import allure

from pages.base_page import BasePage
from locators.success_page_locators import SuccessPageLocators

# Класс страницы успешного оформления заказа
class SuccessPage(BasePage):
    
    # Проверить появление сообщения об успешном заказе
    @allure.step("Проверить появление сообщения об успешном заказе")
    def is_order_created(self):
        return self.find(
            SuccessPageLocators.SUCCESS_MODAL
        ).is_displayed()

    # Получить текст сообщения об успешном заказе
    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(
            SuccessPageLocators.SUCCESS_MODAL
        )
    