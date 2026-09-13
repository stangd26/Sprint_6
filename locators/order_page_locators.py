from selenium.webdriver.common.by import By

# Локаторы страницы оформления заказа
class OrderPageLocators:
    
    # Первый шаг оформления заказа
    FIRST_NAME = (
        By.CSS_SELECTOR,
        "input[placeholder='* Имя']"
    )

    LAST_NAME = (
        By.CSS_SELECTOR,
        "input[placeholder='* Фамилия']"
    )

    ADDRESS = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']"
    )

    METRO = (
        By.CSS_SELECTOR,
        "input[placeholder='* Станция метро']"
    )

    PHONE = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Далее']"
    )

    # Станция метро
    METRO = (
        By.CSS_SELECTOR,
        "input[placeholder='* Станция метро']"
    )

    METRO_DROPDOWN = (
        By.CSS_SELECTOR,
        "div.select-search__select"
    )

    METRO_OPTIONS = (
        By.CSS_SELECTOR,
        "li.select-search__row button.select-search__option"
    )

  # Второй шаг оформления заказа
    DELIVERY_DATE = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']"
    )

    CALENDAR = (
        By.CSS_SELECTOR,
        ".react-datepicker__month-container"
    )

    CALENDAR_NEXT_MONTH = (
        By.CSS_SELECTOR,
        "button.react-datepicker__navigation--next"
    )

    CALENDAR_PREVIOUS_MONTH = (
        By.CSS_SELECTOR,
        "button.react-datepicker__navigation--previous"
    )

    CALENDAR_DAYS = (
        By.CSS_SELECTOR,
        ".react-datepicker__day:not(.react-datepicker__day--outside-month)"
    )

    RENTAL_PERIOD = (
        By.CSS_SELECTOR,
        "div.Dropdown-placeholder"
    )

    RENTAL_PERIOD_OPTIONS = (
        By.CSS_SELECTOR,
        "div.Dropdown-option[role='option']"
    )

    BLACK_COLOR = (
        By.ID,
        "black"
    )

    GREY_COLOR = (
        By.ID,
        "grey"
    )

    COMMENT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]"
        "//button[normalize-space()='Заказать']"
    )

    BACK_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Назад']"
    )

    # Окно подтверждения
    ORDER_OVERLAY = (
        By.CSS_SELECTOR, "div.Order_Overlay__3KW-T"
    )

    CONFIRM_ORDER_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'Order_Modal')]"
    "//button[normalize-space()='Да']"
)

    CANCEL_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]"
        "//button[normalize-space()='Нет']"
    )