# EpisodeBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_preview_url** | **str** | A URL to a 30 second preview (MP3 format) of the episode. &#x60;null&#x60; if not available.  | 
**description** | **str** | A description of the episode. HTML tags are stripped away from this field, use &#x60;html_description&#x60; field in case HTML tags are needed.  | 
**html_description** | **str** | A description of the episode. This field may contain HTML tags.  | 
**duration_ms** | **int** | The episode length in milliseconds.  | 
**explicit** | **bool** | Whether or not the episode has explicit content (true &#x3D; yes it does; false &#x3D; no it does not OR unknown).  | 
**external_urls** | **AllOfEpisodeBaseExternalUrls** | External URLs for this episode.  | 
**href** | **str** | A link to the Web API endpoint providing full details of the episode.  | 
**id** | **str** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the episode.  | 
**images** | [**list[ImageObject]**](ImageObject.md) | The cover art for the episode in various sizes, widest first.  | 
**is_externally_hosted** | **bool** | True if the episode is hosted outside of Spotify&#x27;s CDN.  | 
**is_playable** | **bool** | True if the episode is playable in the given market. Otherwise false.  | 
**language** | **str** | The language used in the episode, identified by a [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code. This field is deprecated and might be removed in the future. Please use the &#x60;languages&#x60; field instead.  | [optional] 
**languages** | **list[str]** | A list of the languages used in the episode, identified by their [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639) code.  | 
**name** | **str** | The name of the episode.  | 
**release_date** | **str** | The date the episode was first released, for example &#x60;\&quot;1981-12-15\&quot;&#x60;. Depending on the precision, it might be shown as &#x60;\&quot;1981\&quot;&#x60; or &#x60;\&quot;1981-12\&quot;&#x60;.  | 
**release_date_precision** | **str** | The precision with which &#x60;release_date&#x60; value is known.  | 
**resume_point** | **AllOfEpisodeBaseResumePoint** | The user&#x27;s most recent position in the episode. Set if the supplied access token is a user token and has the scope &#x27;user-read-playback-position&#x27;.  | 
**type** | **str** | The object type.  | 
**uri** | **str** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the episode.  | 
**restrictions** | **AllOfEpisodeBaseRestrictions** | Included in the response when a content restriction is applied.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

