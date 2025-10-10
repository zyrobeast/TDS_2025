import requests
from urllib.parse import urlencode, urlparse, parse_qs

# Deleted Client ID and Secret
client_id = 'client-id'
client_secret = 'secret'
redirect_uri = 'http://localhost:8000/api'

authorization_endpoint = 'https://accounts.google.com/o/oauth2/v2/auth'
token_endpoint = 'https://oauth2.googleapis.com/token'

def get_authorization_url():
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': 'openid email profile',
        'access_type': 'offline',
        'prompt': 'consent'
    }
    url = f"{authorization_endpoint}?{urlencode(params)}"
    print(f"Go to the following URL and authorize the app:\n{url}")
    return url


def get_access_token(authorization_code):
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(token_endpoint, data=data)

    if response.status_code == 200:
        token_data = response.json()
        print({"id_token": token_data['id_token'], "client_id": client_id})
        return token_data
    else:
        print(f"Failed to get access token. Error: {response.status_code}")
        print(response.text)
        return None


def parse_authorization_code_from_redirect_url(redirect_url):
    parsed_url = urlparse(redirect_url)
    query_params = parse_qs(parsed_url.query)
    authorization_code = query_params.get('code', [None])[0]
    return authorization_code


if __name__ == "__main__":
    auth_url = get_authorization_url()
    print("Visit the URL above to authenticate and get the authorization code.")

    redirect_url = input("Enter the full redirect URL you received after authorization: ")

    authorization_code = parse_authorization_code_from_redirect_url(redirect_url)

    if authorization_code:
        get_access_token(authorization_code)
    else:
        print("Authorization code not found in the redirect URL.")
