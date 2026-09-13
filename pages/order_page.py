from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

# Класс страницы оформления заказа
class OrderPage(BasePage):

    # Заполнить первый этап заказа
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

    # Выбоать станцию метро
    def select_metro(self, metro):
        self.fill(
            OrderPageLocators.METRO,
            metro
        )

        option = (
            By.XPATH,
            "//li[contains(@class, 'select-search__row')]"
            "//button[contains(@class, 'select-search__option')]"
            f"[.//div[contains(@class, 'Order_Text__2broi') "
            f"and normalize-space()='{metro}']]"
        )

        self.click(option)

    # Перейти ко вторму этапу заказа
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    # Выбрать дату
    def select_delivery_date(self, day):
        
        self.click(OrderPageLocators.DELIVERY_DATE)

        date_locator = (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day')"
            f" and not(contains(@class, 'outside-month'))"
            f" and normalize-space()='{day}']"
        )

        self.click(date_locator)

    # Выбрать срок аренды
    def select_rental_period(self, period):
        
        self.click(OrderPageLocators.RENTAL_PERIOD)

        option = (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option')"
            f" and normalize-space()='{period}']"
        )

        self.click(option)

    # Выбрать цвет
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
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    # Подтвердить оформление заказа
    def confirm_order(self):
        self.scroll_to(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)
