import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path: str):
        params = {'path': 'Без имени.png', 'overwrite': 'true'}
        headers = {'Authorization': f'OAuth {token}'}
        response = requests.get(url, params=params, headers=headers)

        href = response.json()['href']

        with open(path, 'rb') as f:
            response = requests.put(href, files={'file': f})

        if response.status_code == 201:
            print('Файл успешно загружен на Яндекс.Диск.')
        else:
            print('Произошла ошибка при загрузке файла на Яндекс.Диск.')


if __name__ == '__main__':
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    path_to_file = r'C:\Users\mrdim\OneDrive\Рабочий стол\Без имени.png'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
