import allure

from data import BASE_URL, DZEN_URL_PART
from pages.main_page import MainPage

# Тесты навигации по главной странице
class TestNavigation:
    
    @allure.feature("Навигация")
    @allure.story("Логотип Самокат")
    @allure.title("Переход на главную страницу по логотипу Самокат")
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(BASE_URL)

        with allure.step("Нажать логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить URL главной страницы"):
            assert (
                main_page.get_current_url().rstrip("/")
                == BASE_URL.rstrip("/")
            )

    @allure.feature("Навигация")
    @allure.story("Логотип Яндекс")
    @allure.title("Переход по логотипу Яндекс в Дзен")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(BASE_URL)

        with allure.step("Запомнить открытые окна"):
            old_windows = main_page.get_window_handles()

        with allure.step("Нажать логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия нового окна"):
            main_page.wait_for_new_window(old_windows)

        with allure.step("Переключиться в новое окно"):
            main_page.switch_to_new_window(old_windows)

        with allure.step("Дождаться перехода в Дзен"):
            main_page.wait_for_url_contains(DZEN_URL_PART)

        with allure.step("Проверить переход в Дзен"):
            assert main_page.is_url_contains(DZEN_URL_PART)
