# swagger_client.PlaylistsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tracks_to_playlist**](PlaylistsApi.md#add_tracks_to_playlist) | **POST** /playlists/{playlist_id}/tracks | Add Items to Playlist 
[**change_playlist_details**](PlaylistsApi.md#change_playlist_details) | **PUT** /playlists/{playlist_id} | Change Playlist Details 
[**check_if_user_follows_playlist**](PlaylistsApi.md#check_if_user_follows_playlist) | **GET** /playlists/{playlist_id}/followers/contains | Check if Users Follow Playlist 
[**create_playlist**](PlaylistsApi.md#create_playlist) | **POST** /users/{user_id}/playlists | Create Playlist 
[**follow_playlist**](PlaylistsApi.md#follow_playlist) | **PUT** /playlists/{playlist_id}/followers | Follow Playlist 
[**get_a_categories_playlists**](PlaylistsApi.md#get_a_categories_playlists) | **GET** /browse/categories/{category_id}/playlists | Get Category&#x27;s Playlists 
[**get_a_list_of_current_users_playlists**](PlaylistsApi.md#get_a_list_of_current_users_playlists) | **GET** /me/playlists | Get Current User&#x27;s Playlists 
[**get_featured_playlists**](PlaylistsApi.md#get_featured_playlists) | **GET** /browse/featured-playlists | Get Featured Playlists 
[**get_list_users_playlists**](PlaylistsApi.md#get_list_users_playlists) | **GET** /users/{user_id}/playlists | Get User&#x27;s Playlists 
[**get_playlist**](PlaylistsApi.md#get_playlist) | **GET** /playlists/{playlist_id} | Get Playlist 
[**get_playlist_cover**](PlaylistsApi.md#get_playlist_cover) | **GET** /playlists/{playlist_id}/images | Get Playlist Cover Image 
[**get_playlists_tracks**](PlaylistsApi.md#get_playlists_tracks) | **GET** /playlists/{playlist_id}/tracks | Get Playlist Items 
[**remove_tracks_playlist**](PlaylistsApi.md#remove_tracks_playlist) | **DELETE** /playlists/{playlist_id}/tracks | Remove Playlist Items 
[**reorder_or_replace_playlists_tracks**](PlaylistsApi.md#reorder_or_replace_playlists_tracks) | **PUT** /playlists/{playlist_id}/tracks | Update Playlist Items 
[**unfollow_playlist**](PlaylistsApi.md#unfollow_playlist) | **DELETE** /playlists/{playlist_id}/followers | Unfollow Playlist 
[**upload_custom_playlist_cover**](PlaylistsApi.md#upload_custom_playlist_cover) | **PUT** /playlists/{playlist_id}/images | Add Custom Playlist Cover Image 

# **add_tracks_to_playlist**
> InlineResponse2008 add_tracks_to_playlist(playlist_id, body=body, position=position, uris=uris)

Add Items to Playlist 

Add one or more items to a user's playlist. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)
position = 56 # int |  (optional)
uris = 'uris_example' # str |  (optional)

try:
    # Add Items to Playlist 
    api_response = api_instance.add_tracks_to_playlist(playlist_id, body=body, position=position, uris=uris)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->add_tracks_to_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 
 **position** | **int**|  | [optional] 
 **uris** | **str**|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Change Playlist Details 
    api_instance.change_playlist_details(playlist_id, body=body)
except ApiException as e:
    print("Exception when calling PlaylistsApi->change_playlist_details: %s\n" % e)
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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
ids = 'ids_example' # str | 

try:
    # Check if Users Follow Playlist 
    api_response = api_instance.check_if_user_follows_playlist(playlist_id, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->check_if_user_follows_playlist: %s\n" % e)
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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Create Playlist 
    api_response = api_instance.create_playlist(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->create_playlist: %s\n" % e)
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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Follow Playlist 
    api_instance.follow_playlist(playlist_id, body=body)
except ApiException as e:
    print("Exception when calling PlaylistsApi->follow_playlist: %s\n" % e)
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

# **get_a_categories_playlists**
> PagingFeaturedPlaylistObject get_a_categories_playlists(category_id, country=country, limit=limit, offset=offset)

Get Category's Playlists 

Get a list of Spotify playlists tagged with a particular category. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
category_id = 'category_id_example' # str | 
country = 'country_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Category's Playlists 
    api_response = api_instance.get_a_categories_playlists(category_id, country=country, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_a_categories_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **country** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingFeaturedPlaylistObject**](PagingFeaturedPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Current User's Playlists 
    api_response = api_instance.get_a_list_of_current_users_playlists(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_a_list_of_current_users_playlists: %s\n" % e)
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

# **get_featured_playlists**
> PagingFeaturedPlaylistObject get_featured_playlists(country=country, locale=locale, timestamp=timestamp, limit=limit, offset=offset)

Get Featured Playlists 

Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab). 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Featured Playlists 
    api_response = api_instance.get_featured_playlists(country=country, locale=locale, timestamp=timestamp, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_featured_playlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingFeaturedPlaylistObject**](PagingFeaturedPlaylistObject.md)

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Playlists 
    api_response = api_instance.get_list_users_playlists(user_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_list_users_playlists: %s\n" % e)
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

# **get_playlist**
> PlaylistObject get_playlist(playlist_id, market=market, fields=fields, additional_types=additional_types)

Get Playlist 

Get a playlist owned by a Spotify user. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
market = 'market_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
additional_types = 'additional_types_example' # str |  (optional)

try:
    # Get Playlist 
    api_response = api_instance.get_playlist(playlist_id, market=market, fields=fields, additional_types=additional_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **market** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **additional_types** | **str**|  | [optional] 

### Return type

[**PlaylistObject**](PlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_cover**
> list[ImageObject] get_playlist_cover(playlist_id)

Get Playlist Cover Image 

Get the current image associated with a specific playlist. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 

try:
    # Get Playlist Cover Image 
    api_response = api_instance.get_playlist_cover(playlist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_playlist_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 

### Return type

[**list[ImageObject]**](ImageObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlists_tracks**
> PagingPlaylistTrackObject get_playlists_tracks(playlist_id, market=market, fields=fields, limit=limit, offset=offset, additional_types=additional_types)

Get Playlist Items 

Get full details of the items of a playlist owned by a Spotify user. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
market = 'market_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)
additional_types = 'additional_types_example' # str |  (optional)

try:
    # Get Playlist Items 
    api_response = api_instance.get_playlists_tracks(playlist_id, market=market, fields=fields, limit=limit, offset=offset, additional_types=additional_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->get_playlists_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **market** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **additional_types** | **str**|  | [optional] 

### Return type

[**PagingPlaylistTrackObject**](PagingPlaylistTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tracks_playlist**
> InlineResponse2008 remove_tracks_playlist(playlist_id, body=body)

Remove Playlist Items 

Remove one or more items from a user's playlist. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = swagger_client.PlaylistIdTracksBody2() # PlaylistIdTracksBody2 |  (optional)

try:
    # Remove Playlist Items 
    api_response = api_instance.remove_tracks_playlist(playlist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->remove_tracks_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **body** | [**PlaylistIdTracksBody2**](PlaylistIdTracksBody2.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_or_replace_playlists_tracks**
> InlineResponse2008 reorder_or_replace_playlists_tracks(playlist_id, body=body, uris=uris)

Update Playlist Items 

Either reorder or replace items in a playlist depending on the request's parameters. To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body. To replace items, include `uris` as either a query parameter or in the request's body. Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist. <br/> **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters. These operations can't be applied together in a single request. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)
uris = 'uris_example' # str |  (optional)

try:
    # Update Playlist Items 
    api_response = api_instance.reorder_or_replace_playlists_tracks(playlist_id, body=body, uris=uris)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaylistsApi->reorder_or_replace_playlists_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 
 **uris** | **str**|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 

try:
    # Unfollow Playlist 
    api_instance.unfollow_playlist(playlist_id)
except ApiException as e:
    print("Exception when calling PlaylistsApi->unfollow_playlist: %s\n" % e)
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

# **upload_custom_playlist_cover**
> upload_custom_playlist_cover(playlist_id, body=body)

Add Custom Playlist Cover Image 

Replace the image used to represent a specific playlist. 

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
api_instance = swagger_client.PlaylistsApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Add Custom Playlist Cover Image 
    api_instance.upload_custom_playlist_cover(playlist_id, body=body)
except ApiException as e:
    print("Exception when calling PlaylistsApi->upload_custom_playlist_cover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: image/jpeg
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

