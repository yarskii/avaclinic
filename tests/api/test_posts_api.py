import allure

from api.models.posts_api import posts_api
import pytest


@allure.title('Получение всех постов')
@allure.description('Тест проверяет запрос на получение всех постов, и что список непустой.')
def test_get_all_posts():
    posts_api.get_all_posts()


@allure.title('Получение поста по ID')
@allure.description('Тест проверяет запрос на получение поста по ID, и что данные корректные.')
@pytest.mark.parametrize('post_id', [1, 101])
def test_get_post_by_id(post_id):
    posts_api.get_post_by_id(post_id)


@allure.title('Создание нового поста')
@allure.description('Тест проверяет запрос на создание поста, и что данные корректные.')
def test_create_post():
    posts_api.create_post()


@allure.title('Полное обновление поста')
@allure.description('Тест проверяет запрос на полное обновление поста, и что данные корректные.')
@pytest.mark.parametrize('post_id', [1, 101])
def test_update_post(post_id):
    posts_api.update_post(post_id)


@allure.title('Частичное обновление поста')
@allure.description('Тест проверяет запрос на частичное обновление поста, и что данные корректные.')
@pytest.mark.parametrize('post_id', [1, 101])
def test_partial_update_post(post_id):
    posts_api.partial_update_post(post_id)


@allure.title('Удаление поста')
@allure.description('Тест проверяет запрос на удаление поста, и что пост больше не доступен.')
@pytest.mark.parametrize('post_id', [1, 101])
def test_delete_post(post_id):
    posts_api.delete_post(post_id)
