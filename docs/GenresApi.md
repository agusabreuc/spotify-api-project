# swagger_client.GenresApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recommendation_genres**](GenresApi.md#get_recommendation_genres) | **GET** /recommendations/available-genre-seeds | Get Available Genre Seeds 

# **get_recommendation_genres**
> InlineResponse20014 get_recommendation_genres()

Get Available Genre Seeds 

Retrieve a list of available genres seed parameter values for [recommendations](/documentation/web-api/reference/get-recommendations). 

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
api_instance = swagger_client.GenresApi(swagger_client.ApiClient(configuration))

try:
    # Get Available Genre Seeds 
    api_response = api_instance.get_recommendation_genres()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenresApi->get_recommendation_genres: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

