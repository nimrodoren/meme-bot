import requests
from loguru import logger

from models.repositories import Repository


def get_repositories(access_token: str, org_id: str) -> list[Repository]:
    repos_url = f"https://api.github.com/orgs/{org_id}/repos"
    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {access_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("GET", repos_url, headers=headers, data=payload)
    response.raise_for_status()
    logger.info(response.text)
    repo=[Repository.model_validate(repo_json) for repo_json in response.json()]
    return repo


def get_webhook_by_repo(org_id: str, repo_name: str, access_token: str) -> dict:
    webhook_url = f"https://api.github.com/repos/{org_id}/{repo_name}/hooks"
    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {access_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("GET", webhook_url, headers=headers, data=payload)
    response.raise_for_status()
    logger.info(response.text)
    return response.json()


def get_webhook_deliverables(org_id: str, hook_id,repo_name: str, access_token: str) -> dict:
    webhook_url = f"https://api.github.com/repos/{org_id}/{repo_name}/hooks/{hook_id}/deliveries"
    payload = {}
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {access_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("GET", webhook_url, headers=headers, data=payload)
    response.raise_for_status()
    logger.info(response.text)
    return response.json()




if __name__ == '__main__':
    from auth import get_jwt_token
    from infrastructure.installation import get_installation_ids, get_access_token

    bearer_token = get_jwt_token()
    installation_ids = get_installation_ids(bearer_token=bearer_token)
    access_token = get_access_token(bearer_token=bearer_token, installation_id=installation_ids[0])
    repositories = get_repositories(access_token=access_token, org_id="nimrodoren")
    webhooks = get_webhook_by_repo(org_id="nimrodoren", repo_name="meme-bot", access_token=access_token)
    deliverables = get_webhook_deliverables(org_id="nimrodoren", access_token=access_token, repo_name="meme-bot",hook_id=webhooks[0]['id'])
    pass
