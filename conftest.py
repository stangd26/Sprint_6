import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Создание и закрытие драйвера
@pytest.fixture
def driver():
    
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()
