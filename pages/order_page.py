import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

# Класс страницы оформления заказа
class OrderPage(BasePage):

    # Заполнить первый этап заказа
    @allure.step("Заполнить первый этап заказа")
    def fill_customer_data(self, data):
        
        self.fill(
            OrderPageLocators.FIRST_NAME,
            data["first_name"]
        )

        self.fill(
            OrderPageLocators.LAST_NAME,
            data["last_name"]
        )

        self.fill(
            OrderPageLocators.ADDRESS,
            data["address"]
        )

        self.select_metro(data["metro"])

        self.fill(
            OrderPageLocators.PHONE,
            data["phone"]
        )

    # Выбрать станцию метро
    @allure.step("Выбрать станцию метро: {metro}")
    def select_metro(self, metro):
        self.fill(
            OrderPageLocators.METRO,
            metro
        )

        option = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(
                metro=metro
            )
        )

        self.click(option)

    # Перейти ко вторму этапу заказа
    @allure.step("Перейти ко второму этапу заказа")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    # Выбрать дату
    @allure.step("Выбрать дату доставки: {day}")
    def select_delivery_date(self, day):
        
        self.click(OrderPageLocators.DELIVERY_DATE)

        date_locator = (
            OrderPageLocators.DELIVERY_DATE_OPTION[0],
            OrderPageLocators.DELIVERY_DATE_OPTION[1].format(
                day=day
            )
        )

        self.click(date_locator)

    # Выбрать срок аренды
    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period):
        
        self.click(OrderPageLocators.RENTAL_PERIOD)

        option = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(
                period=period
            )
        )

        self.click(option)

    # Выбрать цвет
    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        
        if color == "black":
            self.click(OrderPageLocators.BLACK_COLOR)

        elif color == "grey":
            self.click(OrderPageLocators.GREY_COLOR)

        else:
            raise ValueError(
                f"Неизвестный цвет самоката: {color}"
            )

    # Заполнить второй этап заказа
    @allure.step("Заполнить второй этап заказа")
    def fill_order_details(self, data):
        
        self.select_delivery_date(
            data["delivery_date"]
        )

        self.select_rental_period(
            data["rental_period"]
        )

        self.select_color(
            data["color"]
        )

        self.fill(
            OrderPageLocators.COMMENT,
            data["comment"]
        )

    # Нажать кнопку оформления заказа
    @allure.step("Нажать кнопку оформления заказа")
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    # Подтвердить оформление заказа
    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.scroll_to(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)
