import allure

from selenium.webdriver.support.ui import WebDriverWait

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

        with allure.step(
            "Проверить URL главной страницы"
        ):
            assert (
                driver.current_url.rstrip("/")
                == BASE_URL.rstrip("/")
            )

    @allure.feature("Навигация")
    @allure.story("Логотип Яндекс")
    @allure.title("Переход по логотипу Яндекс в Дзен")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(BASE_URL)

        original_window = driver.current_window_handle
        old_windows = driver.window_handles

        with allure.step("Нажать логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия нового окна"):
            WebDriverWait(driver, 15).until(
                lambda d: len(d.window_handles) > len(old_windows)
            )

        with allure.step("Переключиться в новое окно"):
            new_window = next(
                window
                for window in driver.window_handles
                if window != original_window
            )

            driver.switch_to.window(new_window)

        with allure.step("Проверить переход в Дзен"):
            WebDriverWait(driver, 15).until(
                lambda d: DZEN_URL_PART in d.current_url
            )

            assert DZEN_URL_PART in driver.current_url
