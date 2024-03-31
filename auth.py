import time

from jwt import JWT, jwk_from_pem

from settings import settings


def get_jwt_token():
    # Open PEM
    with open(settings.pem_file_location, 'rb') as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time (10 minutes maximum)
        'exp': int(time.time()) + 600,
        # GitHub App's identifier
        'iss': settings.app_id
    }

    # Create JWT
    jwt_instance = JWT()
    encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')

    print(f"JWT:  {encoded_jwt}")
    return encoded_jwt


if __name__ == '__main__':
    get_jwt_token()
