from typing import Any

import requests


def get_installation_data(bearer_token: str) -> dict[str, Any]:
    url = "https://api.github.com/app/installations"

    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {bearer_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.raise_for_status()
    return response.json()


def get_installation_ids(bearer_token: str) -> list:
    repo_data = get_installation_data(bearer_token)
    return [installation["id"] for installation in repo_data]




def get_access_token(bearer_token: str, installation_id: str):
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"

    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {bearer_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response.raise_for_status()

    return response.json()['token']


if __name__ == '__main__':
    from auth import get_jwt_token

    bearer_token = get_jwt_token()
    installation_ids = get_installation_ids(bearer_token=bearer_token)
    access_token = get_access_token(bearer_token=bearer_token, installation_id=installation_ids[0])
