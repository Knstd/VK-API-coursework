import requests
import json
from tqdm import tqdm


class Yandex:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_directory(self, dir_name):
        headers = self.get_headers()
        params = {'path': dir_name}
        requests.put(self.url, headers=headers, params=params)
        return dir_name

    def upload_file(self, dir_name, files_list):
        upload_link = self.url + 'upload'
        upload_info = []
        for photo in tqdm(files_list):
            filename = photo['file_name']
            params = {'path': f'{dir_name}/{filename}', 'url': photo['url']}
            response = requests.post(upload_link, headers=self.get_headers(), params=params)
            upload_list = {'file_name': filename + '.jpg', 'size': photo['size']}
            upload_info.append(upload_list)
        with open('info.json', 'a', encoding='utf-8') as result:
            json.dump(upload_info, result, indent=0)

        response.raise_for_status()
        if response.status_code < 400:
            print('Файлы загружены')
