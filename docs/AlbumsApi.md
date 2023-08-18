# swagger_client.AlbumsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_users_saved_albums**](AlbumsApi.md#check_users_saved_albums) | **GET** /me/albums/contains | Check User&#x27;s Saved Albums 
[**get_an_album**](AlbumsApi.md#get_an_album) | **GET** /albums/{id} | Get Album 
[**get_an_albums_tracks**](AlbumsApi.md#get_an_albums_tracks) | **GET** /albums/{id}/tracks | Get Album Tracks 
[**get_an_artists_albums**](AlbumsApi.md#get_an_artists_albums) | **GET** /artists/{id}/albums | Get Artist&#x27;s Albums 
[**get_multiple_albums**](AlbumsApi.md#get_multiple_albums) | **GET** /albums | Get Several Albums 
[**get_new_releases**](AlbumsApi.md#get_new_releases) | **GET** /browse/new-releases | Get New Releases 
[**get_users_saved_albums**](AlbumsApi.md#get_users_saved_albums) | **GET** /me/albums | Get User&#x27;s Saved Albums 
[**remove_albums_user**](AlbumsApi.md#remove_albums_user) | **DELETE** /me/albums | Remove Users&#x27; Saved Albums 
[**save_albums_user**](AlbumsApi.md#save_albums_user) | **PUT** /me/albums | Save Albums for Current User 

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Albums 
    api_response = api_instance.check_users_saved_albums(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->check_users_saved_albums: %s\n" % e)
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

# **get_an_album**
> AlbumObject get_an_album(id, market=market)

Get Album 

Get Spotify catalog information for a single album. 

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Album 
    api_response = api_instance.get_an_album(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->get_an_album: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**AlbumObject**](AlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_albums_tracks**
> PagingSimplifiedTrackObject get_an_albums_tracks(id, market=market, limit=limit, offset=offset)

Get Album Tracks 

Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number of tracks returned. 

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Album Tracks 
    api_response = api_instance.get_an_albums_tracks(id, market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->get_an_albums_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedTrackObject**](PagingSimplifiedTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_artists_albums**
> PagingSimplifiedAlbumObject get_an_artists_albums(id, include_groups=include_groups, market=market, limit=limit, offset=offset)

Get Artist's Albums 

Get Spotify catalog information about an artist's albums. 

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
include_groups = 'include_groups_example' # str |  (optional)
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Artist's Albums 
    api_response = api_instance.get_an_artists_albums(id, include_groups=include_groups, market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->get_an_artists_albums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_groups** | **str**|  | [optional] 
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedAlbumObject**](PagingSimplifiedAlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_albums**
> InlineResponse200 get_multiple_albums(ids, market=market)

Get Several Albums 

Get Spotify catalog information for multiple albums identified by their Spotify IDs. 

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Several Albums 
    api_response = api_instance.get_multiple_albums(ids, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->get_multiple_albums: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_new_releases**
> InlineResponse20011 get_new_releases(country=country, limit=limit, offset=offset)

Get New Releases 

Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab). 

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
country = 'country_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get New Releases 
    api_response = api_instance.get_new_releases(country=country, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->get_new_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)
market = 'market_example' # str |  (optional)

try:
    # Get User's Saved Albums 
    api_response = api_instance.get_users_saved_albums(limit=limit, offset=offset, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlbumsApi->get_users_saved_albums: %s\n" % e)
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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Remove Users' Saved Albums 
    api_instance.remove_albums_user(ids, body=body)
except ApiException as e:
    print("Exception when calling AlbumsApi->remove_albums_user: %s\n" % e)
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
api_instance = swagger_client.AlbumsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Save Albums for Current User 
    api_instance.save_albums_user(ids, body=body)
except ApiException as e:
    print("Exception when calling AlbumsApi->save_albums_user: %s\n" % e)
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

