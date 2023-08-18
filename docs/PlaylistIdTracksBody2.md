# PlaylistIdTracksBody2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracks** | [**list[PlaylistsplaylistIdtracksTracks]**](PlaylistsplaylistIdtracksTracks.md) | An array of objects containing [Spotify URIs](/documentation/web-api/concepts/spotify-uris-ids) of the tracks or episodes to remove. For example: &#x60;{ \&quot;tracks\&quot;: [{ \&quot;uri\&quot;: \&quot;spotify:track:4iV5W9uYEdYUVa79Axb7Rh\&quot; },{ \&quot;uri\&quot;: \&quot;spotify:track:1301WleyT98MSxVHPZCA6M\&quot; }] }&#x60;. A maximum of 100 objects can be sent at once.  | 
**snapshot_id** | **str** | The playlist&#x27;s snapshot ID against which you want to make the changes. The API will validate that the specified items exist and in the specified positions and make the changes, even if more recent changes have been made to the playlist.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

