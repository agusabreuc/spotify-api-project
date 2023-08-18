# CurrentlyPlayingContextObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **AllOfCurrentlyPlayingContextObjectDevice** | The device that is currently active.  | [optional] 
**repeat_state** | **str** | off, track, context | [optional] 
**shuffle_state** | **bool** | If shuffle is on or off. | [optional] 
**context** | **AllOfCurrentlyPlayingContextObjectContext** | A Context Object. Can be &#x60;null&#x60;. | [optional] 
**timestamp** | **int** | Unix Millisecond Timestamp when data was fetched. | [optional] 
**progress_ms** | **int** | Progress into the currently playing track or episode. Can be &#x60;null&#x60;. | [optional] 
**is_playing** | **bool** | If something is currently playing, return &#x60;true&#x60;. | [optional] 
**item** | **OneOfCurrentlyPlayingContextObjectItem** | The currently playing track or episode. Can be &#x60;null&#x60;. | [optional] 
**currently_playing_type** | **str** | The object type of the currently playing item. Can be one of &#x60;track&#x60;, &#x60;episode&#x60;, &#x60;ad&#x60; or &#x60;unknown&#x60;.  | [optional] 
**actions** | **AllOfCurrentlyPlayingContextObjectActions** | Allows to update the user interface based on which playback actions are available within the current context.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

