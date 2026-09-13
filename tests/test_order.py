import allure
import pytest

from data import BASE_URL, ORDER_DATA, ORDER_ENTRY_POINTS
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.success_page import SuccessPage


ORDER_SCENARIOS = [
    pytest.param(
        ORDER_ENTRY_POINTS[0][0],
        ORDER_ENTRY_POINTS[0][1],
        ORDER_DATA[0],
        id="header_button_data_1"
    ),
    pytest.param(
        ORDER_ENTRY_POINTS[1][0],
        ORDER_ENTRY_POINTS[1][1],
        ORDER_DATA[1],
        id="bottom_button_data_2"
    ),
]

# Тесты оформления заказа
class TestOrder:
    
    @pytest.mark.parametrize(
        "entry_name, entry_point, order_data",
        ORDER_SCENARIOS
    )
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий")
    @allure.title("Успешное оформление заказа — {entry_name}")
    def test_create_order(
        self,
        driver,
        entry_name,
        entry_point,
        order_data
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        success_page = SuccessPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(BASE_URL)

        with allure.step(
            f"Нажать точку входа: {entry_name}"
        ):
            if entry_point == "header":
                main_page.click_order_header()

            elif entry_point == "bottom":
                main_page.click_order_bottom()

            else:
                raise ValueError(
                    f"Неизвестная точка входа: {entry_point}"
                )

        with allure.step("Заполнить данные пользователя"):
            order_page.fill_customer_data(order_data)

        with allure.step("Перейти ко второму шагу"):
            order_page.click_next()

        with allure.step("Заполнить данные заказа"):
            order_page.fill_order_details(order_data)

        with allure.step("Нажать кнопку «Заказать»"):
            order_page.click_order()

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step(
            "Проверить сообщение об успешном создании заказа"
        ):
            assert success_page.is_order_created()
