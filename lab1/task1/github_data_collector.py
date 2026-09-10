import requests
import json

def get_user_repos(user_name):
    url = f"https://api.github.com/users/{user_name}/repos"
    headers = {}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка: {response.status_code}, {response.text}")

    repos = response.json()

    with open(f"{user_name}_repos.json", "w", encoding="utf-8") as json_file:
        json.dump(response.json(), json_file, indent='\t', ensure_ascii=False)

    for repo in repos:
        print(repo['name'])