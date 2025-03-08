import allure
from mobile.screens.mobile_app import mobile
from mobile.screens.verify import VerifyInformationMobileApp


@allure.tag('mobile')
@allure.epic('Мобильное приложение "Skandinavia"')
@allure.feature('Функционал записи на прием')
@allure.story('Запись на диагностику к урологу')
@allure.title('Запись на УЗИ мочевого пузыря через мобильное приложение')
@allure.description('Тест проверяет возможность записи на УЗИ мочевого пузыря через мобильное приложение "Skandinavia"')
@allure.label('owner', 'Ярослав Гусев')
def test_record_for_urology_diagnostic(mobile_management):
    with allure.step('Переход на вкладку "Запись"'):
        mobile.select_main_tab()

    with allure.step('Пропуск информативного экрана'):
        mobile.skip_screen()

    with allure.step('Выбор пациента: "Взрослый"'):
        mobile.select_adult()

    with allure.step('Выбор вида приема: "Диагностика"'):
        mobile.select_diagnostic()

    with allure.step('Поиск направления "Уролог"'):
        mobile.search_direction('уролог')

    with allure.step('Выбор первого результата из списка'):
        mobile.select_first_variant()

    with allure.step('Выбор услуги: "УЗИ мочевого пузыря с определением остаточной мочи"'):
        mobile.select_service()

    with allure.step('Проверка наличия кнопки "Любое отделение" на странице выбора клиники'):
        VerifyInformationMobileApp().should_any_department_button()
