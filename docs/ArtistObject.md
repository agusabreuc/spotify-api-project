# ArtistObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_urls** | **AllOfArtistObjectExternalUrls** | Known external URLs for this artist.  | [optional] 
**followers** | **AllOfArtistObjectFollowers** | Information about the followers of the artist.  | [optional] 
**genres** | **list[str]** | A list of the genres the artist is associated with. If not yet classified, the array is empty.  | [optional] 
**href** | **str** | A link to the Web API endpoint providing full details of the artist.  | [optional] 
**id** | **str** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the artist.  | [optional] 
**images** | [**list[ImageObject]**](ImageObject.md) | Images of the artist in various sizes, widest first.  | [optional] 
**name** | **str** | The name of the artist.  | [optional] 
**popularity** | **int** | The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist&#x27;s popularity is calculated from the popularity of all the artist&#x27;s tracks.  | [optional] 
**type** | **str** | The object type.  | [optional] 
**uri** | **str** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the artist.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

