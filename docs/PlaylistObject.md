# PlaylistObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collaborative** | **bool** | &#x60;true&#x60; if the owner allows other users to modify the playlist.  | [optional] 
**description** | **str** | The playlist description. _Only returned for modified, verified playlists, otherwise_ &#x60;null&#x60;.  | [optional] 
**external_urls** | **AllOfPlaylistObjectExternalUrls** | Known external URLs for this playlist.  | [optional] 
**followers** | **AllOfPlaylistObjectFollowers** | Information about the followers of the playlist. | [optional] 
**href** | **str** | A link to the Web API endpoint providing full details of the playlist.  | [optional] 
**id** | **str** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the playlist.  | [optional] 
**images** | [**list[ImageObject]**](ImageObject.md) | Images for the playlist. The array may be empty or contain up to three images. The images are returned by size in descending order. See [Working with Playlists](/documentation/web-api/concepts/playlists). _**Note**: If returned, the source URL for the image (&#x60;url&#x60;) is temporary and will expire in less than a day._  | [optional] 
**name** | **str** | The name of the playlist.  | [optional] 
**owner** | **AllOfPlaylistObjectOwner** | The user who owns the playlist  | [optional] 
**public** | **bool** | The playlist&#x27;s public/private status: &#x60;true&#x60; the playlist is public, &#x60;false&#x60; the playlist is private, &#x60;null&#x60; the playlist status is not relevant. For more about public/private status, see [Working with Playlists](/documentation/web-api/concepts/playlists)  | [optional] 
**snapshot_id** | **str** | The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version  | [optional] 
**tracks** | **AllOfPlaylistObjectTracks** | The tracks of the playlist.  | [optional] 
**type** | **str** | The object type: \&quot;playlist\&quot;  | [optional] 
**uri** | **str** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the playlist.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

