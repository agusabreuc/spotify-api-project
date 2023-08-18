# swagger_client.MarketsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_markets**](MarketsApi.md#get_available_markets) | **GET** /markets | Get Available Markets 

# **get_available_markets**
> InlineResponse20016 get_available_markets()

Get Available Markets 

Get the list of markets where Spotify is available. 

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
api_instance = swagger_client.MarketsApi(swagger_client.ApiClient(configuration))

try:
    # Get Available Markets 
    api_response = api_instance.get_available_markets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketsApi->get_available_markets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

