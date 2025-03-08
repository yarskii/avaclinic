import logging
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('WEB_URL')
api_url = os.getenv('API_URL')
endpoint = 'posts'
request_url = f'{api_url}/{endpoint}'

title = os.getenv('TITLE')
body = os.getenv('BODY')
user_id = int(os.getenv('USER_ID'))

new_post = {
    'userId': user_id,
    'title': title,
    'body': body
}

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def log_request(method, url, response, post_id=None):
    logger.info(f'Отправляем {method} запрос: {url}')
    logger.info(f'Получаем статус код: {response.status_code}')
    if post_id is not None:
        logger.info(f'Пост id={post_id}: {response.json()}')
