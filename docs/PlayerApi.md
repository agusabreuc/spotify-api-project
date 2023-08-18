# swagger_client.PlayerApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_queue**](PlayerApi.md#add_to_queue) | **POST** /me/player/queue | Add Item to Playback Queue 
[**get_a_users_available_devices**](PlayerApi.md#get_a_users_available_devices) | **GET** /me/player/devices | Get Available Devices 
[**get_information_about_the_users_current_playback**](PlayerApi.md#get_information_about_the_users_current_playback) | **GET** /me/player | Get Playback State 
[**get_queue**](PlayerApi.md#get_queue) | **GET** /me/player/queue | Get the User&#x27;s Queue 
[**get_recently_played**](PlayerApi.md#get_recently_played) | **GET** /me/player/recently-played | Get Recently Played Tracks 
[**get_the_users_currently_playing_track**](PlayerApi.md#get_the_users_currently_playing_track) | **GET** /me/player/currently-playing | Get Currently Playing Track 
[**pause_a_users_playback**](PlayerApi.md#pause_a_users_playback) | **PUT** /me/player/pause | Pause Playback 
[**seek_to_position_in_currently_playing_track**](PlayerApi.md#seek_to_position_in_currently_playing_track) | **PUT** /me/player/seek | Seek To Position 
[**set_repeat_mode_on_users_playback**](PlayerApi.md#set_repeat_mode_on_users_playback) | **PUT** /me/player/repeat | Set Repeat Mode 
[**set_volume_for_users_playback**](PlayerApi.md#set_volume_for_users_playback) | **PUT** /me/player/volume | Set Playback Volume 
[**skip_users_playback_to_next_track**](PlayerApi.md#skip_users_playback_to_next_track) | **POST** /me/player/next | Skip To Next 
[**skip_users_playback_to_previous_track**](PlayerApi.md#skip_users_playback_to_previous_track) | **POST** /me/player/previous | Skip To Previous 
[**start_a_users_playback**](PlayerApi.md#start_a_users_playback) | **PUT** /me/player/play | Start/Resume Playback 
[**toggle_shuffle_for_users_playback**](PlayerApi.md#toggle_shuffle_for_users_playback) | **PUT** /me/player/shuffle | Toggle Playback Shuffle 
[**transfer_a_users_playback**](PlayerApi.md#transfer_a_users_playback) | **PUT** /me/player | Transfer Playback 

# **add_to_queue**
> add_to_queue(uri, device_id=device_id)

Add Item to Playback Queue 

Add an item to the end of the user's current playback queue. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
uri = 'uri_example' # str | 
device_id = 'device_id_example' # str |  (optional)

try:
    # Add Item to Playback Queue 
    api_instance.add_to_queue(uri, device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->add_to_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**|  | 
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a_users_available_devices**
> InlineResponse20015 get_a_users_available_devices()

Get Available Devices 

Get information about a user’s available devices. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))

try:
    # Get Available Devices 
    api_response = api_instance.get_a_users_available_devices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_a_users_available_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_information_about_the_users_current_playback**
> CurrentlyPlayingContextObject get_information_about_the_users_current_playback(market=market, additional_types=additional_types)

Get Playback State 

Get information about the user’s current playback state, including track or episode, progress, and active device. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
market = 'market_example' # str |  (optional)
additional_types = 'additional_types_example' # str |  (optional)

try:
    # Get Playback State 
    api_response = api_instance.get_information_about_the_users_current_playback(market=market, additional_types=additional_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_information_about_the_users_current_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **additional_types** | **str**|  | [optional] 

### Return type

[**CurrentlyPlayingContextObject**](CurrentlyPlayingContextObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue**
> QueueObject get_queue()

Get the User's Queue 

Get the list of objects that make up the user's queue. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))

try:
    # Get the User's Queue 
    api_response = api_instance.get_queue()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_queue: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueueObject**](QueueObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recently_played**
> CursorPagingPlayHistoryObject get_recently_played(limit=limit, after=after, before=before)

Get Recently Played Tracks 

Get tracks from the current user's recently played tracks. _**Note**: Currently doesn't support podcast episodes._ 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
limit = 20 # int |  (optional) (default to 20)
after = 56 # int |  (optional)
before = 56 # int |  (optional)

try:
    # Get Recently Played Tracks 
    api_response = api_instance.get_recently_played(limit=limit, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_recently_played: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **after** | **int**|  | [optional] 
 **before** | **int**|  | [optional] 

### Return type

[**CursorPagingPlayHistoryObject**](CursorPagingPlayHistoryObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_the_users_currently_playing_track**
> CurrentlyPlayingContextObject get_the_users_currently_playing_track(market=market, additional_types=additional_types)

Get Currently Playing Track 

Get the object currently being played on the user's Spotify account. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
market = 'market_example' # str |  (optional)
additional_types = 'additional_types_example' # str |  (optional)

try:
    # Get Currently Playing Track 
    api_response = api_instance.get_the_users_currently_playing_track(market=market, additional_types=additional_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerApi->get_the_users_currently_playing_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **additional_types** | **str**|  | [optional] 

### Return type

[**CurrentlyPlayingContextObject**](CurrentlyPlayingContextObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_a_users_playback**
> pause_a_users_playback(device_id=device_id)

Pause Playback 

Pause playback on the user's account. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str |  (optional)

try:
    # Pause Playback 
    api_instance.pause_a_users_playback(device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->pause_a_users_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seek_to_position_in_currently_playing_track**
> seek_to_position_in_currently_playing_track(position_ms, device_id=device_id)

Seek To Position 

Seeks to the given position in the user’s currently playing track. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
position_ms = 56 # int | 
device_id = 'device_id_example' # str |  (optional)

try:
    # Seek To Position 
    api_instance.seek_to_position_in_currently_playing_track(position_ms, device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->seek_to_position_in_currently_playing_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_ms** | **int**|  | 
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_repeat_mode_on_users_playback**
> set_repeat_mode_on_users_playback(state, device_id=device_id)

Set Repeat Mode 

Set the repeat mode for the user's playback. Options are repeat-track, repeat-context, and off. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
state = 'state_example' # str | 
device_id = 'device_id_example' # str |  (optional)

try:
    # Set Repeat Mode 
    api_instance.set_repeat_mode_on_users_playback(state, device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->set_repeat_mode_on_users_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | 
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_volume_for_users_playback**
> set_volume_for_users_playback(volume_percent, device_id=device_id)

Set Playback Volume 

Set the volume for the user’s current playback device. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
volume_percent = 56 # int | 
device_id = 'device_id_example' # str |  (optional)

try:
    # Set Playback Volume 
    api_instance.set_volume_for_users_playback(volume_percent, device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->set_volume_for_users_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_percent** | **int**|  | 
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skip_users_playback_to_next_track**
> skip_users_playback_to_next_track(device_id=device_id)

Skip To Next 

Skips to next track in the user’s queue. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str |  (optional)

try:
    # Skip To Next 
    api_instance.skip_users_playback_to_next_track(device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->skip_users_playback_to_next_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skip_users_playback_to_previous_track**
> skip_users_playback_to_previous_track(device_id=device_id)

Skip To Previous 

Skips to previous track in the user’s queue. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
device_id = 'device_id_example' # str |  (optional)

try:
    # Skip To Previous 
    api_instance.skip_users_playback_to_previous_track(device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->skip_users_playback_to_previous_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_a_users_playback**
> start_a_users_playback(body=body, device_id=device_id)

Start/Resume Playback 

Start a new context or resume current playback on the user's active device. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) |  (optional)
device_id = 'device_id_example' # str |  (optional)

try:
    # Start/Resume Playback 
    api_instance.start_a_users_playback(body=body, device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->start_a_users_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_shuffle_for_users_playback**
> toggle_shuffle_for_users_playback(state, device_id=device_id)

Toggle Playback Shuffle 

Toggle shuffle on or off for user’s playback. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
state = true # bool | 
device_id = 'device_id_example' # str |  (optional)

try:
    # Toggle Playback Shuffle 
    api_instance.toggle_shuffle_for_users_playback(state, device_id=device_id)
except ApiException as e:
    print("Exception when calling PlayerApi->toggle_shuffle_for_users_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **bool**|  | 
 **device_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_a_users_playback**
> transfer_a_users_playback(body=body)

Transfer Playback 

Transfer playback to a new device and determine if it should start playing. 

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
api_instance = swagger_client.PlayerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) |  (optional)

try:
    # Transfer Playback 
    api_instance.transfer_a_users_playback(body=body)
except ApiException as e:
    print("Exception when calling PlayerApi->transfer_a_users_playback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

