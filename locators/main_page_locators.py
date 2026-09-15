from selenium.webdriver.common.by import By

# Локаторы главной страницы
class MainPageLocators:
    
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]"
        "//button[normalize-space()='Заказать']"
    )

    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]"
        "//button[normalize-space()='Заказать']"
    )

    # Логотипы
    SCOOTER_LOGO = (
        By.CSS_SELECTOR,
        "a.Header_LogoScooter__3lsAR"
    )

    YANDEX_LOGO = (
        By.CSS_SELECTOR,
        "a.Header_LogoYandex__3TSOI"
    )

    # Вопросы раздела «Вопросы о важном»
    FAQ_QUESTIONS = (
        By.CSS_SELECTOR,
        "div.accordion__button"
    )

    # Ответы раздела «Вопросы о важном»
    FAQ_ANSWERS = (
        By.CSS_SELECTOR,
        "div.accordion__panel"
    )
