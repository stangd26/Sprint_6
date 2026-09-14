import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

# Класс главной страницы
class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self, url):
        self.driver.get(url)

    # Нажать верхнюю кнопку Заказать
    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    # Нажать нижнюю кнопку заказать
    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_bottom(self):
        self.scroll_to(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # Открыть вопрос по индексу
    @allure.step("Открыть вопрос FAQ №{index}")
    def click_faq_question(self, index):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                MainPageLocators.FAQ_QUESTIONS
            )
        )

        question = buttons[index]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.FAQ_QUESTIONS
            )
        )

        question.click()

    # Получить ответ на вопрос по индексу
    @allure.step("Получить ответ FAQ №{index}")
    def get_faq_answer(self, index):
        panels = self.wait.until(
            EC.presence_of_all_elements_located(
                MainPageLocators.FAQ_ANSWERS
            )
        )

        return panels[index].text

    # Нажать на лого Самокат
    @allure.step("Нажать на лого Самокат")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    # Нажать на лого Яндекс
    @allure.step("Нажать на лого Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
