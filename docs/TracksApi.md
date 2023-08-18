# swagger_client.TracksApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tracks_to_playlist**](TracksApi.md#add_tracks_to_playlist) | **POST** /playlists/{playlist_id}/tracks | Add Items to Playlist 
[**check_users_saved_tracks**](TracksApi.md#check_users_saved_tracks) | **GET** /me/tracks/contains | Check User&#x27;s Saved Tracks 
[**get_an_albums_tracks**](TracksApi.md#get_an_albums_tracks) | **GET** /albums/{id}/tracks | Get Album Tracks 
[**get_an_artists_top_tracks**](TracksApi.md#get_an_artists_top_tracks) | **GET** /artists/{id}/top-tracks | Get Artist&#x27;s Top Tracks 
[**get_audio_analysis**](TracksApi.md#get_audio_analysis) | **GET** /audio-analysis/{id} | Get Track&#x27;s Audio Analysis 
[**get_audio_features**](TracksApi.md#get_audio_features) | **GET** /audio-features/{id} | Get Track&#x27;s Audio Features 
[**get_playlists_tracks**](TracksApi.md#get_playlists_tracks) | **GET** /playlists/{playlist_id}/tracks | Get Playlist Items 
[**get_recommendations**](TracksApi.md#get_recommendations) | **GET** /recommendations | Get Recommendations 
[**get_several_audio_features**](TracksApi.md#get_several_audio_features) | **GET** /audio-features | Get Tracks&#x27; Audio Features 
[**get_several_tracks**](TracksApi.md#get_several_tracks) | **GET** /tracks | Get Several Tracks 
[**get_track**](TracksApi.md#get_track) | **GET** /tracks/{id} | Get Track 
[**get_users_saved_tracks**](TracksApi.md#get_users_saved_tracks) | **GET** /me/tracks | Get User&#x27;s Saved Tracks 
[**get_users_top_artists_and_tracks**](TracksApi.md#get_users_top_artists_and_tracks) | **GET** /me/top/{type} | Get User&#x27;s Top Items 
[**remove_tracks_playlist**](TracksApi.md#remove_tracks_playlist) | **DELETE** /playlists/{playlist_id}/tracks | Remove Playlist Items 
[**remove_tracks_user**](TracksApi.md#remove_tracks_user) | **DELETE** /me/tracks | Remove User&#x27;s Saved Tracks 
[**reorder_or_replace_playlists_tracks**](TracksApi.md#reorder_or_replace_playlists_tracks) | **PUT** /playlists/{playlist_id}/tracks | Update Playlist Items 
[**save_tracks_user**](TracksApi.md#save_tracks_user) | **PUT** /me/tracks | Save Tracks for Current User 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)
position = 56 # int |  (optional)
uris = 'uris_example' # str |  (optional)

try:
    # Add Items to Playlist 
    api_response = api_instance.add_tracks_to_playlist(playlist_id, body=body, position=position, uris=uris)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->add_tracks_to_playlist: %s\n" % e)
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

# **check_users_saved_tracks**
> list[bool] check_users_saved_tracks(ids)

Check User's Saved Tracks 

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Check User's Saved Tracks 
    api_response = api_instance.check_users_saved_tracks(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->check_users_saved_tracks: %s\n" % e)
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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get Album Tracks 
    api_response = api_instance.get_an_albums_tracks(id, market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_an_albums_tracks: %s\n" % e)
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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Artist's Top Tracks 
    api_response = api_instance.get_an_artists_top_tracks(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_an_artists_top_tracks: %s\n" % e)
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

# **get_audio_analysis**
> AudioAnalysisObject get_audio_analysis(id)

Get Track's Audio Analysis 

Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Track's Audio Analysis 
    api_response = api_instance.get_audio_analysis(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_audio_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AudioAnalysisObject**](AudioAnalysisObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_features**
> AudioFeaturesObject get_audio_features(id)

Get Track's Audio Features 

Get audio feature information for a single track identified by its unique Spotify ID. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Track's Audio Features 
    api_response = api_instance.get_audio_features(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_audio_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AudioFeaturesObject**](AudioFeaturesObject.md)

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling TracksApi->get_playlists_tracks: %s\n" % e)
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

# **get_recommendations**
> RecommendationsObject get_recommendations(seed_artists, seed_genres, seed_tracks, limit=limit, market=market, min_acousticness=min_acousticness, max_acousticness=max_acousticness, target_acousticness=target_acousticness, min_danceability=min_danceability, max_danceability=max_danceability, target_danceability=target_danceability, min_duration_ms=min_duration_ms, max_duration_ms=max_duration_ms, target_duration_ms=target_duration_ms, min_energy=min_energy, max_energy=max_energy, target_energy=target_energy, min_instrumentalness=min_instrumentalness, max_instrumentalness=max_instrumentalness, target_instrumentalness=target_instrumentalness, min_key=min_key, max_key=max_key, target_key=target_key, min_liveness=min_liveness, max_liveness=max_liveness, target_liveness=target_liveness, min_loudness=min_loudness, max_loudness=max_loudness, target_loudness=target_loudness, min_mode=min_mode, max_mode=max_mode, target_mode=target_mode, min_popularity=min_popularity, max_popularity=max_popularity, target_popularity=target_popularity, min_speechiness=min_speechiness, max_speechiness=max_speechiness, target_speechiness=target_speechiness, min_tempo=min_tempo, max_tempo=max_tempo, target_tempo=target_tempo, min_time_signature=min_time_signature, max_time_signature=max_time_signature, target_time_signature=target_time_signature, min_valence=min_valence, max_valence=max_valence, target_valence=target_valence)

Get Recommendations 

Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.  For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
seed_artists = 'seed_artists_example' # str | 
seed_genres = 'seed_genres_example' # str | 
seed_tracks = 'seed_tracks_example' # str | 
limit = 20 # int |  (optional) (default to 20)
market = 'market_example' # str |  (optional)
min_acousticness = 1.2 # float |  (optional)
max_acousticness = 1.2 # float |  (optional)
target_acousticness = 1.2 # float |  (optional)
min_danceability = 1.2 # float |  (optional)
max_danceability = 1.2 # float |  (optional)
target_danceability = 1.2 # float |  (optional)
min_duration_ms = 56 # int |  (optional)
max_duration_ms = 56 # int |  (optional)
target_duration_ms = 56 # int |  (optional)
min_energy = 1.2 # float |  (optional)
max_energy = 1.2 # float |  (optional)
target_energy = 1.2 # float |  (optional)
min_instrumentalness = 1.2 # float |  (optional)
max_instrumentalness = 1.2 # float |  (optional)
target_instrumentalness = 1.2 # float |  (optional)
min_key = 56 # int |  (optional)
max_key = 56 # int |  (optional)
target_key = 56 # int |  (optional)
min_liveness = 1.2 # float |  (optional)
max_liveness = 1.2 # float |  (optional)
target_liveness = 1.2 # float |  (optional)
min_loudness = 1.2 # float |  (optional)
max_loudness = 1.2 # float |  (optional)
target_loudness = 1.2 # float |  (optional)
min_mode = 56 # int |  (optional)
max_mode = 56 # int |  (optional)
target_mode = 56 # int |  (optional)
min_popularity = 56 # int |  (optional)
max_popularity = 56 # int |  (optional)
target_popularity = 56 # int |  (optional)
min_speechiness = 1.2 # float |  (optional)
max_speechiness = 1.2 # float |  (optional)
target_speechiness = 1.2 # float |  (optional)
min_tempo = 1.2 # float |  (optional)
max_tempo = 1.2 # float |  (optional)
target_tempo = 1.2 # float |  (optional)
min_time_signature = 56 # int |  (optional)
max_time_signature = 56 # int |  (optional)
target_time_signature = 56 # int |  (optional)
min_valence = 1.2 # float |  (optional)
max_valence = 1.2 # float |  (optional)
target_valence = 1.2 # float |  (optional)

try:
    # Get Recommendations 
    api_response = api_instance.get_recommendations(seed_artists, seed_genres, seed_tracks, limit=limit, market=market, min_acousticness=min_acousticness, max_acousticness=max_acousticness, target_acousticness=target_acousticness, min_danceability=min_danceability, max_danceability=max_danceability, target_danceability=target_danceability, min_duration_ms=min_duration_ms, max_duration_ms=max_duration_ms, target_duration_ms=target_duration_ms, min_energy=min_energy, max_energy=max_energy, target_energy=target_energy, min_instrumentalness=min_instrumentalness, max_instrumentalness=max_instrumentalness, target_instrumentalness=target_instrumentalness, min_key=min_key, max_key=max_key, target_key=target_key, min_liveness=min_liveness, max_liveness=max_liveness, target_liveness=target_liveness, min_loudness=min_loudness, max_loudness=max_loudness, target_loudness=target_loudness, min_mode=min_mode, max_mode=max_mode, target_mode=target_mode, min_popularity=min_popularity, max_popularity=max_popularity, target_popularity=target_popularity, min_speechiness=min_speechiness, max_speechiness=max_speechiness, target_speechiness=target_speechiness, min_tempo=min_tempo, max_tempo=max_tempo, target_tempo=target_tempo, min_time_signature=min_time_signature, max_time_signature=max_time_signature, target_time_signature=target_time_signature, min_valence=min_valence, max_valence=max_valence, target_valence=target_valence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seed_artists** | **str**|  | 
 **seed_genres** | **str**|  | 
 **seed_tracks** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **market** | **str**|  | [optional] 
 **min_acousticness** | **float**|  | [optional] 
 **max_acousticness** | **float**|  | [optional] 
 **target_acousticness** | **float**|  | [optional] 
 **min_danceability** | **float**|  | [optional] 
 **max_danceability** | **float**|  | [optional] 
 **target_danceability** | **float**|  | [optional] 
 **min_duration_ms** | **int**|  | [optional] 
 **max_duration_ms** | **int**|  | [optional] 
 **target_duration_ms** | **int**|  | [optional] 
 **min_energy** | **float**|  | [optional] 
 **max_energy** | **float**|  | [optional] 
 **target_energy** | **float**|  | [optional] 
 **min_instrumentalness** | **float**|  | [optional] 
 **max_instrumentalness** | **float**|  | [optional] 
 **target_instrumentalness** | **float**|  | [optional] 
 **min_key** | **int**|  | [optional] 
 **max_key** | **int**|  | [optional] 
 **target_key** | **int**|  | [optional] 
 **min_liveness** | **float**|  | [optional] 
 **max_liveness** | **float**|  | [optional] 
 **target_liveness** | **float**|  | [optional] 
 **min_loudness** | **float**|  | [optional] 
 **max_loudness** | **float**|  | [optional] 
 **target_loudness** | **float**|  | [optional] 
 **min_mode** | **int**|  | [optional] 
 **max_mode** | **int**|  | [optional] 
 **target_mode** | **int**|  | [optional] 
 **min_popularity** | **int**|  | [optional] 
 **max_popularity** | **int**|  | [optional] 
 **target_popularity** | **int**|  | [optional] 
 **min_speechiness** | **float**|  | [optional] 
 **max_speechiness** | **float**|  | [optional] 
 **target_speechiness** | **float**|  | [optional] 
 **min_tempo** | **float**|  | [optional] 
 **max_tempo** | **float**|  | [optional] 
 **target_tempo** | **float**|  | [optional] 
 **min_time_signature** | **int**|  | [optional] 
 **max_time_signature** | **int**|  | [optional] 
 **target_time_signature** | **int**|  | [optional] 
 **min_valence** | **float**|  | [optional] 
 **max_valence** | **float**|  | [optional] 
 **target_valence** | **float**|  | [optional] 

### Return type

[**RecommendationsObject**](RecommendationsObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_several_audio_features**
> InlineResponse20013 get_several_audio_features(ids)

Get Tracks' Audio Features 

Get audio features for multiple tracks based on their Spotify IDs. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 

try:
    # Get Tracks' Audio Features 
    api_response = api_instance.get_several_audio_features(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_several_audio_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_several_tracks**
> InlineResponse2002 get_several_tracks(ids, market=market)

Get Several Tracks 

Get Spotify catalog information for multiple tracks based on their Spotify IDs. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Several Tracks 
    api_response = api_instance.get_several_tracks(ids, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_several_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track**
> TrackObject get_track(id, market=market)

Get Track 

Get Spotify catalog information for a single track identified by its unique Spotify ID. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
market = 'market_example' # str |  (optional)

try:
    # Get Track 
    api_response = api_instance.get_track(id, market=market)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **market** | **str**|  | [optional] 

### Return type

[**TrackObject**](TrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_saved_tracks**
> PagingSavedTrackObject get_users_saved_tracks(market=market, limit=limit, offset=offset)

Get User's Saved Tracks 

Get a list of the songs saved in the current Spotify user's 'Your Music' library. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
market = 'market_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Saved Tracks 
    api_response = api_instance.get_users_saved_tracks(market=market, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_users_saved_tracks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PagingSavedTrackObject**](PagingSavedTrackObject.md)

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
time_range = 'medium_term' # str |  (optional) (default to medium_term)
limit = 20 # int |  (optional) (default to 20)
offset = 0 # int |  (optional) (default to 0)

try:
    # Get User's Top Items 
    api_response = api_instance.get_users_top_artists_and_tracks(type, time_range=time_range, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->get_users_top_artists_and_tracks: %s\n" % e)
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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = swagger_client.PlaylistIdTracksBody2() # PlaylistIdTracksBody2 |  (optional)

try:
    # Remove Playlist Items 
    api_response = api_instance.remove_tracks_playlist(playlist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->remove_tracks_playlist: %s\n" % e)
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

# **remove_tracks_user**
> remove_tracks_user(ids, body=body)

Remove User's Saved Tracks 

Remove one or more tracks from the current user's 'Your Music' library. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Remove User's Saved Tracks 
    api_instance.remove_tracks_user(ids, body=body)
except ApiException as e:
    print("Exception when calling TracksApi->remove_tracks_user: %s\n" % e)
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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
playlist_id = 'playlist_id_example' # str | 
body = NULL # dict(str, object) |  (optional)
uris = 'uris_example' # str |  (optional)

try:
    # Update Playlist Items 
    api_response = api_instance.reorder_or_replace_playlists_tracks(playlist_id, body=body, uris=uris)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->reorder_or_replace_playlists_tracks: %s\n" % e)
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

# **save_tracks_user**
> save_tracks_user(ids, body=body)

Save Tracks for Current User 

Save one or more tracks to the current user's 'Your Music' library. 

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
api_instance = swagger_client.TracksApi(swagger_client.ApiClient(configuration))
ids = 'ids_example' # str | 
body = NULL # dict(str, object) |  (optional)

try:
    # Save Tracks for Current User 
    api_instance.save_tracks_user(ids, body=body)
except ApiException as e:
    print("Exception when calling TracksApi->save_tracks_user: %s\n" % e)
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

