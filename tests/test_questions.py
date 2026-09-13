import allure
import pytest

from data import BASE_URL, FAQ_ANSWERS
from pages.main_page import MainPage

# Тесты раздела вопросов и ответов
class TestQuestions:
    
    @pytest.mark.parametrize(
        "question_index, expected_answer",
        [
            pytest.param(
                0,
                FAQ_ANSWERS[0],
                id="question_1"
            ),
            pytest.param(
                1,
                FAQ_ANSWERS[1],
                id="question_2"
            ),
            pytest.param(
                2,
                FAQ_ANSWERS[2],
                id="question_3"
            ),
            pytest.param(
                3,
                FAQ_ANSWERS[3],
                id="question_4"
            ),
            pytest.param(
                4,
                FAQ_ANSWERS[4],
                id="question_5"
            ),
            pytest.param(
                5,
                FAQ_ANSWERS[5],
                id="question_6"
            ),
            pytest.param(
                6,
                FAQ_ANSWERS[6],
                id="question_7"
            ),
            pytest.param(
                7,
                FAQ_ANSWERS[7],
                id="question_8"
            ),
        ]
    )
    @allure.feature("Вопросы о важном")
    @allure.story("Раскрытие ответа")
    @allure.title("Открытие ответа на вопрос")
    def test_faq_answer(
        self,
        driver,
        question_index,
        expected_answer
    ):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(BASE_URL)

        with allure.step(
            f"Открыть вопрос №{question_index + 1}"
        ):
            main_page.click_faq_question(question_index)

        with allure.step("Проверить текст ответа"):
            actual_answer = main_page.get_faq_answer(
                question_index
            )

            assert actual_answer == expected_answer
