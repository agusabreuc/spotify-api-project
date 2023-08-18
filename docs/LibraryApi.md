# swagger_client.LibraryApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_playlist_details**](LibraryApi.md#change_playlist_details) | **PUT** /playlists/{playlist_id} | Change Playlist Details 
[**check_current_user_follows**](LibraryApi.md#check_current_user_follows) | **GET** /me/following/contains | Check If User Follows Artists or Users 
[**check_users_saved_albums**](LibraryApi.md#check_users_saved_albums) | **GET** /me/albums/contains | Check User&#x27;s Saved Albums 
[**check_users_saved_audiobooks**](LibraryApi.md#check_users_saved_audiobooks) | **GET** /me/audiobooks/contains | Check User&#x27;s Saved Audiobooks 
[**check_users_saved_episodes**](LibraryApi.md#check_users_saved_episodes) | **GET** /me/episodes/contains | Check User&#x27;s Saved Episodes 
[**check_users_saved_shows**](LibraryApi.md#check_users_saved_shows) | **GET** /me/shows/contains | Check User&#x27;s Saved Shows 
[**check_users_saved_tracks**](LibraryApi.md#check_users_saved_tracks) | **GET** /me/tracks/contains | Check User&#x27;s Saved Tracks 
[**create_playlist**](LibraryApi.md#create_playlist) | **POST** /users/{user_id}/playlists | Create Playlist 
[**follow_artists_users**](LibraryApi.md#follow_artists_users) | **PUT** /me/following | Follow Artists or Users 
[**get_a_list_of_current_users_playlists**](LibraryApi.md#get_a_list_of_current_users_playlists) | **GET** /me/playlists | Get Current User&#x27;s Playlists 
[**get_followed**](LibraryApi.md#get_followed) | **GET** /me/following | Get Followed Artists 
[**get_users_saved_albums**](LibraryApi.md#get_users_saved_albums) | **GET** /me/albums | Get User&#x27;s Saved Albums 
[**get_users_saved_audiobooks**](LibraryApi.md#get_users_saved_audiobooks) | **GET** /me/audiobooks | Get User&#x27;s Saved Audiobooks 
[**get_users_saved_episodes**](LibraryApi.md#get_users_saved_episodes) | **GET** /me/episodes | Get User&#x27;s Saved Episodes 
[**get_users_saved_shows**](LibraryApi.md#get_users_saved_shows) | **GET** /me/shows | Get User&#x27;s Saved Shows 
[**get_users_saved_tracks**](LibraryApi.md#get_users_saved_tracks) | **GET** /me/tracks | Get User&#x27;s Saved Tracks 
[**get_users_top_artists_and_tracks**](LibraryApi.md#get_users_top_artists_and_tracks) | **GET** /me/top/{type} | Get User&#x27;s Top Items 
[**remove_albums_user**](LibraryApi.md#remove_albums_user) | **DELETE** /me/albums | Remove Users&#x27; Saved Albums 
[**remove_audiobooks_user**](LibraryApi.md#remove_audiobooks_user) | **DELETE** /me/audiobooks | Remove User&#x27;s Saved Audiobooks 
[**remove_episodes_user**](LibraryApi.md#remove_episodes_user) | **DELETE** /me/episodes | Remove User&#x27;s Saved Episodes 
[**remove_shows_user**](LibraryApi.md#remove_shows_user) | **DELETE** /me/shows | Remove User&#x27;s Saved Shows 
[**remove_tracks_user**](LibraryApi.md#remove_tracks_user) | **DELETE** /me/tracks | Remove User&#x27;s Saved Tracks 
[**save_albums_user**](LibraryApi.md#save_albums_user) | **PUT** /me/albums | Save Albums for Current User 
[**save_audiobooks_user**](LibraryApi.md#save_audiobooks_user) | **PUT** /me/audiobooks | Save Audiobooks for Current User 
[**save_episodes_user**](LibraryApi.md#save_episodes_user) | **PUT** /me/episodes | Save Episodes for Current User 
[**save_shows_user**](LibraryApi.md#save_shows_user) | **PUT** /me/shows | Save Shows for Current User 
[**save_tracks_user**](LibraryApi.md#save_tracks_user) | **PUT** /me/tracks | Save Tracks for Current User 
[**unfollow_artists_users**](LibraryApi.md#unfollow_artists_users) | **DELETE** /me/following | Unfollow Artists or Users 

# **change_playlist_details**
> change_playlist_details(playlist_id, body=body)

Change Playlist Details 

Change a playlist's name and public/private state. (The user must, of course, own the playlist.) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Change Playlist Details 
    api_instance.change_playlist_details(playlist_id, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->change_playlist_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_current_user_follows**
> list[bool] check_current_user_follows(type, ids)

Check If User Follows Artists or Users 

Check to see if the current user is following one or more artists or other Spotify users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 

try:
    # Check If User Follows Artists or Users 
    api_response = api_instance.check_current_user_follows(type, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->check_current_user_follows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_users_saved_albums**
> list[bool] check_users_saved_albums(ids)

Check User's Saved Albums 

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Albums 
    api_response = api_instance.check_users_saved_albums(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->check_users_saved_albums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_users_saved_audiobooks**
> list[bool] check_users_saved_audiobooks(ids)

Check User's Saved Audiobooks 

Check if one or more audiobooks are already saved in the current Spotify user's library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Audiobooks 
    api_response = api_instance.check_users_saved_audiobooks(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->check_users_saved_audiobooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_users_saved_episodes**
> list[bool] check_users_saved_episodes(ids)

Check User's Saved Episodes 

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/> This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Episodes 
    api_response = api_instance.check_users_saved_episodes(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->check_users_saved_episodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_users_saved_shows**
> list[bool] check_users_saved_shows(ids)

Check User's Saved Shows 

Check if one or more shows is already saved in the current Spotify user's library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Shows 
    api_response = api_instance.check_users_saved_shows(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->check_users_saved_shows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_users_saved_tracks**
> list[bool] check_users_saved_tracks(ids)

Check User's Saved Tracks 

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Tracks 
    api_response = api_instance.check_users_saved_tracks(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->check_users_saved_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_playlist**
> PlaylistObject create_playlist(user_id, body=body)

Create Playlist 

Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Create Playlist 
    api_response = api_instance.create_playlist(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->create_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

[**PlaylistObject**](PlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_artists_users**
> follow_artists_users(type, ids, body=body)

Follow Artists or Users 

Add the current user as a follower of one or more artists or other Spotify users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Follow Artists or Users 
    api_instance.follow_artists_users(type, ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->follow_artists_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_list_of_current_users_playlists**
> PagingPlaylistObject get_a_list_of_current_users_playlists(limit=limit, offset=offset)

Get Current User's Playlists 

Get a list of the playlists owned or followed by the current Spotify user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Current User's Playlists 
    api_response = api_instance.get_a_list_of_current_users_playlists(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_a_list_of_current_users_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingPlaylistObject**](PagingPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_followed**
> InlineResponse20012 get_followed(type, after=after, limit=limit)

Get Followed Artists 

Get the current user's followed artists. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    # Get Followed Artists 
    api_response = api_instance.get_followed(type, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_followed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_saved_albums**
> PagingSavedAlbumObject get_users_saved_albums(limit=limit, offset=offset, market=market)

Get User's Saved Albums 

Get a list of the albums saved in the current Spotify user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)
market = 'market_example' # str |  (optional)

try:
    # Get User's Saved Albums 
    api_response = api_instance.get_users_saved_albums(limit=limit, offset=offset, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_users_saved_albums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **market** | **str**|  | [optional] 

### Return type

[**PagingSavedAlbumObject**](PagingSavedAlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_saved_audiobooks**
> PagingSimplifiedAudiobookObject get_users_saved_audiobooks(limit=limit, offset=offset)

Get User's Saved Audiobooks 

Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Audiobooks 
    api_response = api_instance.get_users_saved_audiobooks(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_users_saved_audiobooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedAudiobookObject**](PagingSimplifiedAudiobookObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_saved_episodes**
> PagingSavedEpisodeObject get_users_saved_episodes(market=market, limit=limit, offset=offset)

Get User's Saved Episodes 

Get a list of the episodes saved in the current Spotify user's library.<br/> This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Episodes 
    api_response = api_instance.get_users_saved_episodes(market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_users_saved_episodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSavedEpisodeObject**](PagingSavedEpisodeObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_saved_shows**
> PagingSavedShowObject get_users_saved_shows(limit=limit, offset=offset)

Get User's Saved Shows 

Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the number of shows returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Shows 
    api_response = api_instance.get_users_saved_shows(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_users_saved_shows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSavedShowObject**](PagingSavedShowObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_saved_tracks**
> PagingSavedTrackObject get_users_saved_tracks(market=market, limit=limit, offset=offset)

Get User's Saved Tracks 

Get a list of the songs saved in the current Spotify user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Tracks 
    api_response = api_instance.get_users_saved_tracks(market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_users_saved_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSavedTrackObject**](PagingSavedTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_top_artists_and_tracks**
> InlineResponse2009 get_users_top_artists_and_tracks(type, time_range=time_range, limit=limit, offset=offset)

Get User's Top Items 

Get the current user's top artists or tracks based on calculated affinity. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
time_range = 'medium_term' # str |  (optional) (default to medium_term)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Top Items 
    api_response = api_instance.get_users_top_artists_and_tracks(type, time_range=time_range, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LibraryApi->get_users_top_artists_and_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **time_range** | **str**|  | [optional] [default to medium_term]
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_albums_user**
> remove_albums_user(ids, body=body)

Remove Users' Saved Albums 

Remove one or more albums from the current user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Remove Users' Saved Albums 
    api_instance.remove_albums_user(ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->remove_albums_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_audiobooks_user**
> remove_audiobooks_user(ids)

Remove User's Saved Audiobooks 

Remove one or more audiobooks from the Spotify user's library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Remove User's Saved Audiobooks 
    api_instance.remove_audiobooks_user(ids)
except ApiException as e:
    print("Exception when calling LibraryApi->remove_audiobooks_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_episodes_user**
> remove_episodes_user(ids, body=body)

Remove User's Saved Episodes 

Remove one or more episodes from the current user's library.<br/> This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Remove User's Saved Episodes 
    api_instance.remove_episodes_user(ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->remove_episodes_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shows_user**
> remove_shows_user(ids, market=market)

Remove User's Saved Shows 

Delete one or more shows from current Spotify user's library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Remove User's Saved Shows 
    api_instance.remove_shows_user(ids, market=market)
except ApiException as e:
    print("Exception when calling LibraryApi->remove_shows_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tracks_user**
> remove_tracks_user(ids, body=body)

Remove User's Saved Tracks 

Remove one or more tracks from the current user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Remove User's Saved Tracks 
    api_instance.remove_tracks_user(ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->remove_tracks_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_albums_user**
> save_albums_user(ids, body=body)

Save Albums for Current User 

Save one or more albums to the current user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Save Albums for Current User 
    api_instance.save_albums_user(ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->save_albums_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_audiobooks_user**
> save_audiobooks_user(ids)

Save Audiobooks for Current User 

Save one or more audiobooks to the current Spotify user's library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Save Audiobooks for Current User 
    api_instance.save_audiobooks_user(ids)
except ApiException as e:
    print("Exception when calling LibraryApi->save_audiobooks_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_episodes_user**
> save_episodes_user(ids, body=body)

Save Episodes for Current User 

Save one or more episodes to the current user's library.<br/> This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Save Episodes for Current User 
    api_instance.save_episodes_user(ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->save_episodes_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_shows_user**
> save_shows_user(ids)

Save Shows for Current User 

Save one or more shows to current Spotify user's library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Save Shows for Current User 
    api_instance.save_shows_user(ids)
except ApiException as e:
    print("Exception when calling LibraryApi->save_shows_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_tracks_user**
> save_tracks_user(ids, body=body)

Save Tracks for Current User 

Save one or more tracks to the current user's 'Your Music' library. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Save Tracks for Current User 
    api_instance.save_tracks_user(ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->save_tracks_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfollow_artists_users**
> unfollow_artists_users(type, ids, body=body)

Unfollow Artists or Users 

Remove the current user as a follower of one or more artists or other Spotify users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth_2_0
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LibraryApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Unfollow Artists or Users 
    api_instance.unfollow_artists_users(type, ids, body=body)
except ApiException as e:
    print("Exception when calling LibraryApi->unfollow_artists_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **ids** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

