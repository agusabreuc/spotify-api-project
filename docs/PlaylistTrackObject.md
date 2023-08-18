# PlaylistTrackObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** | The date and time the track or episode was added. _**Note**: some very old playlists may return &#x60;null&#x60; in this field._  | [optional] 
**added_by** | **AllOfPlaylistTrackObjectAddedBy** | The Spotify user who added the track or episode. _**Note**: some very old playlists may return &#x60;null&#x60; in this field._  | [optional] 
**is_local** | **bool** | Whether this track or episode is a [local file](/documentation/web-api/concepts/playlists/#local-files) or not.  | [optional] 
**track** | **OneOfPlaylistTrackObjectTrack** | Information about the track or episode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

