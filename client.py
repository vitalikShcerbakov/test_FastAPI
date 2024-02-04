import json

import requests
from requests.auth import HTTPBasicAuth


# USERNAME = "johndoe"
# PASSWORD = "johndoe"
# EMAIL = 'johndoe@gmail.com'

USERNAME = "test_clietn"
PASSWORD = "test_clietn"
EMAIL = 'test_clietn@gmail.com'


def get_register():
    url = "http://localhost:8000/v1/users/"
    response = requests.post(url, json=({
                        "username": USERNAME,
                        "email": EMAIL,
                        "password": PASSWORD
    }))
    return response.text


def get_token():
    auth = HTTPBasicAuth(username=USERNAME, password=PASSWORD)
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.post(
        url="http://localhost:8000/token", auth=auth, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    return response.text


def main():
    get_register()
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    for i in range(10):
        requests.post(
            'http://127.0.0.1:8000/v1/users/items/',
            data=json.dumps(
                {"title": f"test_title {i}",
                 "description": f"test_description {i}"
                 }
            ), headers=headers)

    response = requests.get(
        'http://127.0.0.1:8000/v1/users/items/', headers=headers)
    print(response.text)


if __name__ == '__main__':
    main()
