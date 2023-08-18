# swagger_client.UsersApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_current_user_follows**](UsersApi.md#check_current_user_follows) | **GET** /me/following/contains | Check If User Follows Artists or Users 
[**check_if_user_follows_playlist**](UsersApi.md#check_if_user_follows_playlist) | **GET** /playlists/{playlist_id}/followers/contains | Check if Users Follow Playlist 
[**follow_artists_users**](UsersApi.md#follow_artists_users) | **PUT** /me/following | Follow Artists or Users 
[**follow_playlist**](UsersApi.md#follow_playlist) | **PUT** /playlists/{playlist_id}/followers | Follow Playlist 
[**get_current_users_profile**](UsersApi.md#get_current_users_profile) | **GET** /me | Get Current User&#x27;s Profile 
[**get_followed**](UsersApi.md#get_followed) | **GET** /me/following | Get Followed Artists 
[**get_list_users_playlists**](UsersApi.md#get_list_users_playlists) | **GET** /users/{user_id}/playlists | Get User&#x27;s Playlists 
[**get_users_profile**](UsersApi.md#get_users_profile) | **GET** /users/{user_id} | Get User&#x27;s Profile 
[**get_users_top_artists_and_tracks**](UsersApi.md#get_users_top_artists_and_tracks) | **GET** /me/top/{type} | Get User&#x27;s Top Items 
[**unfollow_artists_users**](UsersApi.md#unfollow_artists_users) | **DELETE** /me/following | Unfollow Artists or Users 
[**unfollow_playlist**](UsersApi.md#unfollow_playlist) | **DELETE** /playlists/{playlist_id}/followers | Unfollow Playlist 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 

try:
    # Check If User Follows Artists or Users 
    api_response = api_instance.check_current_user_follows(type, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->check_current_user_follows: %s\n" % e)
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

# **check_if_user_follows_playlist**
> list[bool] check_if_user_follows_playlist(playlist_id, ids)

Check if Users Follow Playlist 

Check to see if one or more Spotify users are following a specified playlist. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
ids = 'ids_example' # str | 

try:
    # Check if Users Follow Playlist 
    api_response = api_instance.check_if_user_follows_playlist(playlist_id, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->check_if_user_follows_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **ids** | **str**|  | 

### Return type

**list[bool]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Follow Artists or Users 
    api_instance.follow_artists_users(type, ids, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->follow_artists_users: %s\n" % e)
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

# **follow_playlist**
> follow_playlist(playlist_id, body=body)

Follow Playlist 

Add the current user as a follower of a playlist. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Follow Playlist 
    api_instance.follow_playlist(playlist_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->follow_playlist: %s\n" % e)
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

# **get_current_users_profile**
> PrivateUserObject get_current_users_profile()

Get Current User's Profile 

Get detailed profile information about the current user (including the current user's username). 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get Current User's Profile 
    api_response = api_instance.get_current_users_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_users_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrivateUserObject**](PrivateUserObject.md)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    # Get Followed Artists 
    api_response = api_instance.get_followed(type, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_followed: %s\n" % e)
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

# **get_list_users_playlists**
> PagingPlaylistObject get_list_users_playlists(user_id, limit=limit, offset=offset)

Get User's Playlists 

Get a list of the playlists owned or followed by a Spotify user. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Playlists 
    api_response = api_instance.get_list_users_playlists(user_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_list_users_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **get_users_profile**
> PublicUserObject get_users_profile(user_id)

Get User's Profile 

Get public profile information about a Spotify user. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Get User's Profile 
    api_response = api_instance.get_users_profile(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**PublicUserObject**](PublicUserObject.md)

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
time_range = 'medium_term' # str |  (optional) (default to medium_term)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Top Items 
    api_response = api_instance.get_users_top_artists_and_tracks(type, time_range=time_range, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_top_artists_and_tracks: %s\n" % e)
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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Unfollow Artists or Users 
    api_instance.unfollow_artists_users(type, ids, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->unfollow_artists_users: %s\n" % e)
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

# **unfollow_playlist**
> unfollow_playlist(playlist_id)

Unfollow Playlist 

Remove the current user as a follower of a playlist. 

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 

try:
    # Unfollow Playlist 
    api_instance.unfollow_playlist(playlist_id)
except ApiException as e:
    print("Exception when calling UsersApi->unfollow_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

