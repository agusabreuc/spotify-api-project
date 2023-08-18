# swagger_client.ShowsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_users_saved_shows**](ShowsApi.md#check_users_saved_shows) | **GET** /me/shows/contains | Check User&#x27;s Saved Shows 
[**get_a_show**](ShowsApi.md#get_a_show) | **GET** /shows/{id} | Get Show 
[**get_a_shows_episodes**](ShowsApi.md#get_a_shows_episodes) | **GET** /shows/{id}/episodes | Get Show Episodes 
[**get_multiple_shows**](ShowsApi.md#get_multiple_shows) | **GET** /shows | Get Several Shows 
[**get_users_saved_shows**](ShowsApi.md#get_users_saved_shows) | **GET** /me/shows | Get User&#x27;s Saved Shows 
[**remove_shows_user**](ShowsApi.md#remove_shows_user) | **DELETE** /me/shows | Remove User&#x27;s Saved Shows 
[**save_shows_user**](ShowsApi.md#save_shows_user) | **PUT** /me/shows | Save Shows for Current User 

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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Shows 
    api_response = api_instance.check_users_saved_shows(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShowsApi->check_users_saved_shows: %s\n" % e)
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

# **get_a_show**
> ShowObject get_a_show(id, market=market)

Get Show 

Get Spotify catalog information for a single show identified by its unique Spotify ID. 

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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Show 
    api_response = api_instance.get_a_show(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShowsApi->get_a_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**ShowObject**](ShowObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_shows_episodes**
> PagingSimplifiedEpisodeObject get_a_shows_episodes(id, market=market, limit=limit, offset=offset)

Get Show Episodes 

Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned. 

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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Show Episodes 
    api_response = api_instance.get_a_shows_episodes(id, market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShowsApi->get_a_shows_episodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedEpisodeObject**](PagingSimplifiedEpisodeObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_shows**
> InlineResponse2003 get_multiple_shows(ids, market=market)

Get Several Shows 

Get Spotify catalog information for several shows based on their Spotify IDs. 

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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Several Shows 
    api_response = api_instance.get_multiple_shows(ids, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShowsApi->get_multiple_shows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Shows 
    api_response = api_instance.get_users_saved_shows(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShowsApi->get_users_saved_shows: %s\n" % e)
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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Remove User's Saved Shows 
    api_instance.remove_shows_user(ids, market=market)
except ApiException as e:
    print("Exception when calling ShowsApi->remove_shows_user: %s\n" % e)
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
api_instance = swagger_client.ShowsApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Save Shows for Current User 
    api_instance.save_shows_user(ids)
except ApiException as e:
    print("Exception when calling ShowsApi->save_shows_user: %s\n" % e)
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

