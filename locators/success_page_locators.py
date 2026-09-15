from selenium.webdriver.common.by import By

# Локаторы окна успешного оформления заказа
class SuccessPageLocators:
    
    SUCCESS_MODAL = (
        By.CSS_SELECTOR,
        ".Order_ModalHeader__3FDaJ"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".Order_Text__2broi"
    )

    STATUS_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Посмотреть статус']"
    )
