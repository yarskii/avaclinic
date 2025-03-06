import allure
import requests
from jsonschema import validate

from utils.schemas import all_posts, post
from utils.config_posts_api import request_url, log_request, new_post, logger


class PostsAPI:
    @allure.step('Получение всех постов')
    def get_all_posts(self):
        response = requests.get(request_url)
        response_json = response.json()

        log_request('GET', request_url, response)

        assert response.status_code == 200
        assert len(response_json) > 0

        validate(response_json, schema=all_posts)

    @allure.step('Получение поста по ID {post_id}')
    def get_post_by_id(self, post_id):
        url = f'{request_url}/{post_id}'
        response = requests.get(url)
        response_json = response.json()

        log_request('GET', url, response, post_id)

        assert response.status_code == 200, f'Пост ID {post_id} не существует'

        validate(response_json, schema=post)

    @allure.step('Создание нового поста')
    def create_post(self):
        response = requests.post(request_url, json=new_post)
        response_json = response.json()

        log_request('POST', request_url, response, response_json['id'])

        assert response.status_code == 201
        assert isinstance(response_json, dict)
        assert response_json['userId'] == new_post['userId']
        assert response_json['title'] == new_post['title']
        assert response_json['body'] == new_post['body']
        assert response_json['id'] == 101

        validate(response_json, schema=post)

    @allure.step('Полное обновление поста ID {post_id}')
    def update_post(self, post_id):
        url = f'{request_url}/{post_id}'
        response = requests.put(url, json=new_post)
        response_json = response.json()

        log_request('PUT', url, response, post_id)

        assert response.status_code == 200
        assert isinstance(response_json, dict)
        assert response_json['userId'] == new_post['userId']
        assert response_json['title'] == new_post['title']
        assert response_json['body'] == new_post['body']

        validate(response_json, schema=post)

    @allure.step('Частичное обновление поста ID {post_id}')
    def partial_update_post(self, post_id):
        url = f'{request_url}/{post_id}'
        partial_data = {'title': 'partial title'}
        response = requests.patch(url, json=partial_data)
        response_json = response.json()

        log_request('PATCH', url, response, post_id)

        assert response.status_code == 200
        assert isinstance(response_json, dict)
        assert response_json['userId'] > 0, f'Данного юзера не существует'
        assert response_json['title'] == partial_data['title']

        validate(response_json, schema=post)

    @allure.step('Удаление поста ID {post_id}')
    def delete_post(self, post_id):
        url = f'{request_url}/{post_id}'
        response = requests.delete(url)

        log_request('DELETE', url, response, post_id)

        assert response.status_code == 200

        get_response = requests.get(url)
        get_response_json = get_response.json()

        logger.info(f'Отправляем GET запрос для проверки удаления: {url}')
        logger.info(f'Получаем статус код: {get_response.status_code}')
        logger.info(f'Пост id={post_id}: {get_response_json}')

        assert get_response.status_code == 404, 'Пост не был удален!'


posts_api = PostsAPI()
