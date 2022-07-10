import json
from datetime import datetime
import requests


class Vk:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, user_id, version):
        self.params = {
            'owner_id': user_id,
            'access_token': token,
            'v': version
        }

    def get_photos(self):
        count = int(input('Введите количество фотографий: '))
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {
            'extended': 1,
            'photo_sizes': 1,
            'album_id': 'wall',
            'count': count
        }
        res = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        if res.get('error', ''):
            print('Ошибка доступа к аккаунту')
        else:
            return res['response']['items']

    def save_info(self, file_name):
        saved_info = []
        for photo in self.get_photos():
            photo_info = {}
            photo_name = str(photo['likes']['count'])
            for name in saved_info:
                if name['file_name'] == photo_name:
                    photo_name += f'_{(datetime.utcfromtimestamp(photo["date"]).strftime("%Y-%m-%d"))}'
            photo_info['file_name'] = photo_name
            photo_info['size'] = photo['sizes'][-1]['type']
            photo_info['url'] = photo['sizes'][-1]['url']
            saved_info.append(photo_info)

        with open(file_name, 'a', encoding='utf-8') as result:
            json.dump(saved_info, result)
        return saved_info
