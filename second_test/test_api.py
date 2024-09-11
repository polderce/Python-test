from dotenv import load_dotenv
import os
import requests

load_dotenv()


API = os.getenv('API_KEY')
username = os.getenv('username')
name_repo = os.getenv('name_repo')

base_url = "https://api.github.com"


def create_repo(access_token, repo_name):
    url = f"{base_url}/user/repos"

    headers = {
        "Authorization": f"token {access_token}",
    }

    # create json data to send using the post request
    data = {
        "name": repo_name
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        repo_data = response.json()
        return repo_data
    else:
        return None


new_repo = create_repo(API, name_repo)

if new_repo:
    print(f"Новый публичный репозиторий создан!")
else:
    print("Неудачная попытка создания публичного репозитория.")


def delete_repo(access_token, user, repo_name):
    url = f"{base_url}/repos/{user}/{repo_name}"

    headers = {
        "Authorization": f"token {access_token}",
    }
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Репозиторий успешно удален. Статус код: {response.status_code}.")
    elif response.status_code == 404:
        print(f"Репозиторий не найден или уже был удален. Статус код: {response.status_code}.")
    else:
        print(f"Неудачная попытка удаления репозитория. Статус код: {response.status_code}.")


delete_repo(API, username, name_repo)