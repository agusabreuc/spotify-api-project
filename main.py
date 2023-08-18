import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests
import os


if __name__ == "__main__":
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    headers = {
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
    }
    response_token = requests.post(url="https://accounts.spotify.com/api/token", headers=headers, data=data, auth=(client_id, client_secret))
    token = response_token.json()["access_token"]
    api = swagger_client.ApiClient()
    api_search = swagger_client.SearchApi(api)
    api_artist = swagger_client.ArtistsApi(api)
    api.configuration.access_token = token
    try:
        response = api_artist.get_an_artist(id="5jTtGLk1mGFMY5lQOvJYUj")
        pprint(response)
    except ApiException as e:
        print('Exception when calling ArtistAPI')
        print(e)