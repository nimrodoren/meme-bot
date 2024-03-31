import requests
from loguru import logger


def get_webhook_by_org(org_id: str, access_token: str) -> dict:
    webhook_url = f"https://api.github.com/orgs/{org_id}/hooks"
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


def get_webhook_deliverables(org_id: str, hook_id, access_token: str) -> dict:
    webhook_url = f"https://api.github.com/orgs/{org_id}/hooks/{hook_id}/deliveries"
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
    from installation import get_access_token, get_installation_ids

    bearer_token = get_jwt_token()
    installation_ids = get_installation_ids(bearer_token=bearer_token)
    access_token = get_access_token(bearer_token=bearer_token, installation_id=installation_ids[0])
    webhooks = get_webhook_by_org(org_id="nimrodoren", access_token=access_token)
    deliverables = get_webhook_deliverables(org_id="nimrodoren", access_token=access_token, hook_id=webhooks[0]['id'])
    pass
