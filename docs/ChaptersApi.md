# swagger_client.ChaptersApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_a_chapter**](ChaptersApi.md#get_a_chapter) | **GET** /chapters/{id} | Get a Chapter 
[**get_audiobook_chapters**](ChaptersApi.md#get_audiobook_chapters) | **GET** /audiobooks/{id}/chapters | Get Audiobook Chapters 
[**get_several_chapters**](ChaptersApi.md#get_several_chapters) | **GET** /chapters | Get Several Chapters 

# **get_a_chapter**
> ChapterObject get_a_chapter(id, market=market)

Get a Chapter 

Get Spotify catalog information for a single chapter.<br /> **Note: Chapters are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

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
api_instance = swagger_client.ChaptersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get a Chapter 
    api_response = api_instance.get_a_chapter(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChaptersApi->get_a_chapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**ChapterObject**](ChapterObject.md)

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
api_instance = swagger_client.ChaptersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Audiobook Chapters 
    api_response = api_instance.get_audiobook_chapters(id, market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChaptersApi->get_audiobook_chapters: %s\n" % e)
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

# **get_several_chapters**
> InlineResponse2006 get_several_chapters(ids, market=market)

Get Several Chapters 

Get Spotify catalog information for several chapters identified by their Spotify IDs.<br /> **Note: Chapters are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

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
api_instance = swagger_client.ChaptersApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Several Chapters 
    api_response = api_instance.get_several_chapters(ids, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChaptersApi->get_several_chapters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

