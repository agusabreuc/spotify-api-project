# swagger_client.ArtistsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_current_user_follows**](ArtistsApi.md#check_current_user_follows) | **GET** /me/following/contains | Check If User Follows Artists or Users 
[**follow_artists_users**](ArtistsApi.md#follow_artists_users) | **PUT** /me/following | Follow Artists or Users 
[**get_an_artist**](ArtistsApi.md#get_an_artist) | **GET** /artists/{id} | Get Artist 
[**get_an_artists_albums**](ArtistsApi.md#get_an_artists_albums) | **GET** /artists/{id}/albums | Get Artist&#x27;s Albums 
[**get_an_artists_related_artists**](ArtistsApi.md#get_an_artists_related_artists) | **GET** /artists/{id}/related-artists | Get Artist&#x27;s Related Artists 
[**get_an_artists_top_tracks**](ArtistsApi.md#get_an_artists_top_tracks) | **GET** /artists/{id}/top-tracks | Get Artist&#x27;s Top Tracks 
[**get_followed**](ArtistsApi.md#get_followed) | **GET** /me/following | Get Followed Artists 
[**get_multiple_artists**](ArtistsApi.md#get_multiple_artists) | **GET** /artists | Get Several Artists 
[**unfollow_artists_users**](ArtistsApi.md#unfollow_artists_users) | **DELETE** /me/following | Unfollow Artists or Users 

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 

try:
    # Check If User Follows Artists or Users 
    api_response = api_instance.check_current_user_follows(type, ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtistsApi->check_current_user_follows: %s\n" % e)
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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Follow Artists or Users 
    api_instance.follow_artists_users(type, ids, body=body)
except ApiException as e:
    print("Exception when calling ArtistsApi->follow_artists_users: %s\n" % e)
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

# **get_an_artist**
> ArtistObject get_an_artist(id)

Get Artist 

Get Spotify catalog information for a single artist identified by their unique Spotify ID. 

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Artist 
    api_response = api_instance.get_an_artist(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtistsApi->get_an_artist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ArtistObject**](ArtistObject.md)

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ArtistsApi->get_an_artists_albums: %s\n" % e)
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

# **get_an_artists_related_artists**
> InlineResponse2001 get_an_artists_related_artists(id)

Get Artist's Related Artists 

Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of the Spotify community's listening history. 

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Artist's Related Artists 
    api_response = api_instance.get_an_artists_related_artists(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtistsApi->get_an_artists_related_artists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_artists_top_tracks**
> InlineResponse2002 get_an_artists_top_tracks(id, market=market)

Get Artist's Top Tracks 

Get Spotify catalog information about an artist's top tracks by country. 

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Artist's Top Tracks 
    api_response = api_instance.get_an_artists_top_tracks(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtistsApi->get_an_artists_top_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    # Get Followed Artists 
    api_response = api_instance.get_followed(type, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtistsApi->get_followed: %s\n" % e)
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

# **get_multiple_artists**
> InlineResponse2001 get_multiple_artists(ids)

Get Several Artists 

Get Spotify catalog information for several artists based on their Spotify IDs. 

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Get Several Artists 
    api_response = api_instance.get_multiple_artists(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtistsApi->get_multiple_artists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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
api_instance = swagger_client.ArtistsApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Unfollow Artists or Users 
    api_instance.unfollow_artists_users(type, ids, body=body)
except ApiException as e:
    print("Exception when calling ArtistsApi->unfollow_artists_users: %s\n" % e)
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

