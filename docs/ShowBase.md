# ShowBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_markets** | **list[str]** | A list of the countries in which the show can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.  | 
**copyrights** | [**list[CopyrightObject]**](CopyrightObject.md) | The copyright statements of the show.  | 
**description** | **str** | A description of the show. HTML tags are stripped away from this field, use &#x60;html_description&#x60; field in case HTML tags are needed.  | 
**html_description** | **str** | A description of the show. This field may contain HTML tags.  | 
**explicit** | **bool** | Whether or not the show has explicit content (true &#x3D; yes it does; false &#x3D; no it does not OR unknown).  | 
**external_urls** | **AllOfShowBaseExternalUrls** | External URLs for this show.  | 
**href** | **str** | A link to the Web API endpoint providing full details of the show.  | 
**id** | **str** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the show.  | 
**images** | [**list[ImageObject]**](ImageObject.md) | The cover art for the show in various sizes, widest first.  | 
**is_externally_hosted** | **bool** | True if all of the shows episodes are hosted outside of Spotify&#x27;s CDN. This field might be &#x60;null&#x60; in some cases.  | 
**languages** | **list[str]** | A list of the languages used in the show, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.  | 
**media_type** | **str** | The media type of the show.  | 
**name** | **str** | The name of the episode.  | 
**publisher** | **str** | The publisher of the show.  | 
**type** | **str** | The object type.  | 
**uri** | **str** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the show.  | 
**total_episodes** | **int** | The total number of episodes in the show.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

