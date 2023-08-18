# CurrentlyPlayingObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **AllOfCurrentlyPlayingObjectContext** | A Context Object. Can be &#x60;null&#x60;. | [optional] 
**timestamp** | **int** | Unix Millisecond Timestamp when data was fetched | [optional] 
**progress_ms** | **int** | Progress into the currently playing track or episode. Can be &#x60;null&#x60;. | [optional] 
**is_playing** | **bool** | If something is currently playing, return &#x60;true&#x60;. | [optional] 
**item** | **OneOfCurrentlyPlayingObjectItem** | The currently playing track or episode. Can be &#x60;null&#x60;. | [optional] 
**currently_playing_type** | **str** | The object type of the currently playing item. Can be one of &#x60;track&#x60;, &#x60;episode&#x60;, &#x60;ad&#x60; or &#x60;unknown&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

