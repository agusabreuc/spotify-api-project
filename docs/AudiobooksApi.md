# swagger_client.AudiobooksApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_users_saved_audiobooks**](AudiobooksApi.md#check_users_saved_audiobooks) | **GET** /me/audiobooks/contains | Check User&#x27;s Saved Audiobooks 
[**get_an_audiobook**](AudiobooksApi.md#get_an_audiobook) | **GET** /audiobooks/{id} | Get an Audiobook 
[**get_audiobook_chapters**](AudiobooksApi.md#get_audiobook_chapters) | **GET** /audiobooks/{id}/chapters | Get Audiobook Chapters 
[**get_multiple_audiobooks**](AudiobooksApi.md#get_multiple_audiobooks) | **GET** /audiobooks | Get Several Audiobooks 
[**get_users_saved_audiobooks**](AudiobooksApi.md#get_users_saved_audiobooks) | **GET** /me/audiobooks | Get User&#x27;s Saved Audiobooks 
[**remove_audiobooks_user**](AudiobooksApi.md#remove_audiobooks_user) | **DELETE** /me/audiobooks | Remove User&#x27;s Saved Audiobooks 
[**save_audiobooks_user**](AudiobooksApi.md#save_audiobooks_user) | **PUT** /me/audiobooks | Save Audiobooks for Current User 

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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Audiobooks 
    api_response = api_instance.check_users_saved_audiobooks(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiobooksApi->check_users_saved_audiobooks: %s\n" % e)
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

# **get_an_audiobook**
> AudiobookObject get_an_audiobook(id, market=market)

Get an Audiobook 

Get Spotify catalog information for a single audiobook.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get an Audiobook 
    api_response = api_instance.get_an_audiobook(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiobooksApi->get_an_audiobook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**AudiobookObject**](AudiobookObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiobook_chapters**
> PagingSimplifiedChapterObject get_audiobook_chapters(id, market=market, limit=limit, offset=offset)

Get Audiobook Chapters 

Get Spotify catalog information about an audiobook's chapters.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Audiobook Chapters 
    api_response = api_instance.get_audiobook_chapters(id, market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiobooksApi->get_audiobook_chapters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedChapterObject**](PagingSimplifiedChapterObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_audiobooks**
> InlineResponse2005 get_multiple_audiobooks(ids, market=market)

Get Several Audiobooks 

Get Spotify catalog information for several audiobooks identified by their Spotify IDs.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Several Audiobooks 
    api_response = api_instance.get_multiple_audiobooks(ids, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiobooksApi->get_multiple_audiobooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Audiobooks 
    api_response = api_instance.get_users_saved_audiobooks(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudiobooksApi->get_users_saved_audiobooks: %s\n" % e)
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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Remove User's Saved Audiobooks 
    api_instance.remove_audiobooks_user(ids)
except ApiException as e:
    print("Exception when calling AudiobooksApi->remove_audiobooks_user: %s\n" % e)
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
api_instance = swagger_client.AudiobooksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Save Audiobooks for Current User 
    api_instance.save_audiobooks_user(ids)
except ApiException as e:
    print("Exception when calling AudiobooksApi->save_audiobooks_user: %s\n" % e)
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

