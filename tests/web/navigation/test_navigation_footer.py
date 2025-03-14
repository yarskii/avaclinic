import allure
import pytest

from web.components.navigation import Navigation
from web.components.verify import Verify


@pytest.mark.parametrize(('section', 'title'),
                         [('О компании', 'О компании'),
                          ('Вакансии', 'Присоединяйтесь к нашей команде'),
                          ('Отзывы клиентов', 'Отзывы')],
                         ids=['about', 'vacancy', 'reviews'])
def test_navigation_footer(browser_management, section, title):
    with allure.step('Открываем главную страницу'):
        Navigation.open_home_page()

    with allure.step(f'Выбираем секцию "{section}"'):
        Navigation().select_footer_section(section)

    with allure.step(f'Проверяем информацию на открывшейся странице "{title}"'):
        Verify().verify_information_on_page(title)
