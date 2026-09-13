from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Класс базовых операций с элементами страницы
class BasePage:
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Найти видимый элемент
    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # Найти все элементы
    def find_all(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # Нажать на кликабельный элемент
    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Очистить поле и ввести значение
    def fill(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    # Получить текст элемента
    def get_text(self, locator):
        return self.find(locator).text

    # Прокрутить страницу до элемента
    def scroll_to(self, locator):
        element = self.find(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
