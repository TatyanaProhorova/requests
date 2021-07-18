import requests

class YaUploader:

    def __init__(self, file_path_and_name: str):  # принимает путь к файлу на компъютере  - строку
        self.file_path = file_path_and_name

    def upload(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format("AQ...")}
        params = {"path": "test.txt", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        put_href = response.json()["href"]
        r = requests.put(put_href, data=open(self.file_path, "rb"))
        r.raise_for_status()
        if r.status_code == 201:
            print(f"Файл загружен")
        return (f"Файл загружен", r.status_code)

file_path_and_name = "D:/test.txt"
uploader = YaUploader(file_path_and_name)
result = uploader.upload()
