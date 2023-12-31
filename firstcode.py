import requests
import base64

# Replace with your own Client ID and Client Secret
CLIENT_ID = '321f6f02bd3f46a3b20609e96cb3ee4a'
CLIENT_SECRET = '53ac6c8a04a14d9ab8b4a8755129dd95'

# Base64 encode the client ID and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64encode(client_credentials.encode())

# Request the access token
token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {client_credentials_base64.decode()}'
}
data = {
    'grant_type': 'client_credentials'
}
response = requests.post(token_url, data=data, headers=headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained successfully.")
    print(access_token)
else:
    print("Error obtaining access token.")
    exit()