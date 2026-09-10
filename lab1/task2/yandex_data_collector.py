import requests
import json

YANDEX_TOKEN = "токен"

def get_yandex_disk_info():
    url = "https://cloud-api.yandex.net/v1/disk/"
    headers = {
        "Authorization": f"OAuth {YANDEX_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open("yandex_repos.json", "w", encoding="utf-8") as json_file:
        json.dump(response.json(), json_file, indent='\t', ensure_ascii=False)

    print(response.json().get("user", {}))